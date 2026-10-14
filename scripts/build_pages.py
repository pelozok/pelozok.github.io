#!/usr/bin/env python3
"""Generates index.html (es), en/index.html (en) and the canvas geometry CSS.

All page copy lives in the T dictionary below. Edit it, then run from the repo root:

    python3 scripts/build_pages.py

Bump TODAY when content changes (it feeds dateModified and the footer date).
"""
import json, os, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = '2026-10-13'

# ---------------------------------------------------------------- geometry
GW, GH, NW, NH = 760, 600, 158, 96
COL = {'A': 16, 'B': 206, 'C': 396, 'D': 586}
GRAPH = [  # id, col, y, kind, href, extra classes
    ('uam',   'A', 100, 'base',  '#experience', ''),
    ('fin',   'A', 340, 'base',  '#skills', ''),
    ('wp',    'B', 24,  'build', '#work', ''),
    ('rails', 'B', 200, 'build', '#work', ''),
    ('react', 'B', 376, 'build', '#skills', ''),
    ('api',   'C', 92,  'build', '#skills', ''),
    ('infra', 'C', 268, 'ops',   '#skills', ''),
    ('qa',    'C', 444, 'ops',   '#skills', ''),
    ('ai',    'D', 24,  'ai',    '#skills', ''),
    ('fw',    'D', 220, 'ai',    '#finwaise', 'is-output'),
    ('own',   'D', 380, 'base',  '#work', ''),
]
GEDGES = [('uam', 'wp'), ('uam', 'rails'), ('uam', 'react'), ('wp', 'api'), ('wp', 'infra'),
          ('rails', 'api'), ('rails', 'infra'), ('react', 'qa'), ('api', 'ai'), ('infra', 'fw'),
          ('qa', 'fw'), ('ai', 'fw'), ('react', 'own'), ('fin', 'fw')]

FW, FH, FNW = 760, 500, 170
FLOW = [
    ('inv',   20, 40,  'base',  ''),
    ('ocr',   295, 40, 'build', ''),
    ('finy',  570, 40, 'ai',    ''),
    ('ctrl',  570, 196, 'ops',  ''),
    ('erp',   295, 196, 'build', 'is-output'),
    ('brief', 20, 346, 'base',  ''),
    ('gen',   295, 346, 'ai',   ''),
    ('video', 570, 346, 'build', 'is-output'),
]
FEDGES = [('inv', 'ocr'), ('ocr', 'finy'), ('finy', 'ctrl'), ('ctrl', 'erp'), ('brief', 'gen'), ('gen', 'video')]


def gbox(nid):
    for n in GRAPH:
        if n[0] == nid:
            return COL[n[1]], n[2], NW, NH
def fbox(nid):
    for n in FLOW:
        if n[0] == nid:
            return n[1], n[2], FNW, NH

def edge_path(a, b):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    if abs(ax - bx) < 5:  # same column: vertical
        if by > ay:
            sx, sy, tx, ty = ax + aw / 2, ay + ah, bx + bw / 2, by
        else:
            sx, sy, tx, ty = ax + aw / 2, ay, bx + bw / 2, by + bh
        return f'M{sx:.0f} {sy:.0f} V{ty:.0f}', (sx, sy, tx, ty)
    if bx < ax:  # leftwards
        sx, sy, tx, ty = ax, ay + ah / 2, bx + bw, by + bh / 2
    else:
        sx, sy, tx, ty = ax + aw, ay + ah / 2, bx, by + bh / 2
    dx = (tx - sx) / 2
    return f'M{sx:.0f} {sy:.0f} C{sx + dx:.0f} {sy:.0f} {tx - dx:.0f} {ty:.0f} {tx:.0f} {ty:.0f}', (sx, sy, tx, ty)

def bus_path(sx, sy, tx, ty, bx, r=8):
    if abs(sy - ty) < 1:
        return f'M{sx:.0f} {sy:.0f} H{tx:.0f}'
    d = 1 if ty > sy else -1
    return (f'M{sx:.0f} {sy:.0f} H{bx - r:.0f} Q{bx:.0f} {sy:.0f} {bx:.0f} {sy + d * r:.0f} '
            f'V{ty - d * r:.0f} Q{bx:.0f} {ty:.0f} {bx + r:.0f} {ty:.0f} H{tx:.0f}')

GUTTER = {'A': 190, 'B': 380, 'C': 570}

def col_of(nid):
    return next(n[1] for n in GRAPH if n[0] == nid)

def graph_edge(a, b):
    if (a, b) == ('react', 'own'):  # through the free channel between C nodes
        return 'M364 424 H372 Q380 424 380 416 V412 Q380 404 388 404 H562 Q570 404 570 412 V420 Q570 428 578 428 H586'
    if (a, b) == ('fin', 'fw'):  # the long thread: down the first gutter, along the floor, up the last
        return 'M174 388 H182 Q190 388 190 396 V548 Q190 556 198 556 H562 Q570 556 570 548 V276 Q570 268 578 268 H586'
    ax, ay, aw, ah = gbox(a); bx, by, bw, bh = gbox(b)
    if col_of(a) == col_of(b):
        return edge_path(gbox(a), gbox(b))[0]
    return bus_path(ax + aw, ay + ah / 2, bx, by + bh / 2, GUTTER[col_of(a)])

def graph_ports():
    pts = set()
    for a, b in GEDGES:
        d = graph_edge(a, b)
        nums = d.replace('M', ' ').replace('H', ' H ').replace('V', ' V ').split()
        ax, ay, aw, ah = gbox(a); bx, by, bw, bh = gbox(b)
        if col_of(a) == col_of(b):
            continue
        pts.add((ax + aw, ay + ah / 2)); pts.add((bx, by + bh / 2))
    return ''.join(f'<circle class="port" cx="{x:.0f}" cy="{y:.0f}" r="3.5"/>' for x, y in sorted(pts))

def chain(ids, fn):
    d = ''
    for i in range(len(ids) - 1):
        p = fn(ids[i], ids[i + 1])
        d += p if i == 0 else ' ' + p.split(' ', 1)[0].replace('M', 'L') + ' ' + p.split(' ', 1)[1]
    return d

def pct(v, total):
    return f'{v / total * 100:.3f}%'

css = ['/* ---- generated canvas geometry (do not edit by hand) ---- */']
for nid, col, y, *_ in GRAPH:
    css.append(f".graph [data-id='{nid}'] {{ left: {pct(COL[col], GW)}; top: {pct(y, GH)}; width: {pct(NW, GW)}; height: {pct(NH, GH)}; }}")
for nid, x, y, *_ in FLOW:
    css.append(f".flowchart [data-id='{nid}'] {{ left: {pct(x, FW)}; top: {pct(y, FH)}; width: {pct(FNW, FW)}; height: {pct(NH, FH)}; }}")
GEN_CSS = '\n'.join(css) + '\n'

# ---------------------------------------------------------------- content
ARROW = '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M3 9 9 3M4 3h5v5"/></svg>'
DL = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 3v10M5.5 8.5 10 13l4.5-4.5M4 17h12"/></svg>'

T = {
 'es': dict(
  lang='es', path='', cv_file='Kevin-Pelozo-Retamar-CV-2026-ES.pdf', other='/en/', other_label='EN', other_lang='en', other_aria='Read in English',
  title='Kevin Pelozo | Software &amp; AI Engineer en Costa Rica',
  desc='Kevin Pelozo Retamar, Software Engineer en Costa Rica. Full stack (TypeScript, React, WordPress, APIs, AWS) e IA aplicada en producción, hoy en Finwaise.',
  og_desc='Programo de punta a punta y sumo IA en producción. Hoy en Finwaise, un ERP con IA nativa.',
  og_alt='Kevin Pelozo, Software &amp; AI Engineer: su experiencia como un grafo de nodos que converge en Finwaise.',
  locale='es_CR', locale_alt='en_US',
  skip='Saltar al contenido', home='Kevin Pelozo, inicio', navlabel='Principal',
  nav=[('#skills', 'Habilidades'), ('#finwaise', 'Finwaise'), ('#work', 'Proyectos'), ('#experience', 'Experiencia'), ('#contact', 'Contacto')],
  role='Software Engineer · <em>IA aplicada</em>',
  lede='Programo de punta a punta: TypeScript, React, WordPress, APIs e infraestructura en AWS. Hoy sumo IA a todo eso, en producción.',
  cv='Descargar CV', mail='Escribime',
  graph_label='Grafo de mi experiencia: formación, web, plataforma e IA convergen en Finwaise, junto a mis proyectos propios.',
  graph_note='mi experiencia, como un grafo',
  nodes={
   'uam': ('formación', 'Ingeniería en Sistemas', 'UAM, 2015'),
   'fin': ('negocio', 'Finanzas y procesos', 'Control Car BAC'),
   'wp': ('web', 'WordPress · PHP · Amplify', '50+ sitios'),
   'rails': ('backend', 'Bots y backends', 'Ruby on Jets, 2022 - 24'),
   'react': ('frontend', 'TypeScript · React', 'Next.js, interfaces'),
   'api': ('integraciones', 'APIs y datos', 'scraping, Metabase y más'),
   'infra': ('infra', 'AWS · Docker', '99.9% uptime'),
   'qa': ('calidad', 'Testing E2E', 'Playwright'),
   'ai': ('ia', 'IA aplicada', 'LLMs y agentes'),
   'fw': ('hoy', 'Finwaise', 'ERP con IA nativa'),
   'own': ('propios', 'Proyectos propios', 'Iglesia Central, Clear Books'),
  },
  skills_title='Todo el stack, y la IA encima.',
  skills_intro='Programo para clientes reales desde 2019. La IA no reemplaza ese oficio: lo multiplica.',
  ai_kind='ia', ai_h='IA aplicada',
  ai_p='Llevo modelos de lenguaje a producto real: con datos, validación, costos y usuarios de verdad.',
  ai_list=[('IA dentro del producto', 'Finy y el motor de verificación de Finwaise: extraer, clasificar, conciliar y validar antes de tocar los libros.'),
           ('Desarrollo agéntico', 'Claude Code y servidores MCP como forma diaria de trabajo, y adopción de IA en el equipo.'),
           ('IA generativa', 'Campañas de mercadeo con imagen, voz y video generados.'),
           ('Pipelines de documentos', 'OCR, LLMs y APIs de punta a punta, con validación y reintentos.')],
  ai_tools=[('modelos', 'Claude, OpenAI, Gemini, Mistral (vía OpenRouter)'), ('agentes', 'tool use, MCP, prompt engineering'), ('orquestación', 'pipelines de documentos, OCR, integración de APIs'), ('generativa', 'imagen, voz y video'), ('desarrollo', 'Claude Code, Cursor, GitHub Copilot, Lovable')],
  cells=[
   ('cell-5', 'build', 'backend', 'Backend, APIs y datos', 'APIs, integraciones, bots y scraping de datos, con tableros para analizarlos.', [('lenguajes', 'TypeScript, JavaScript, PHP, Ruby'), ('backends', 'APIs REST, WordPress, Ruby on Jets (2022 - 24)'), ('datos', 'PostgreSQL, MySQL, SQL Server, Supabase, Metabase'), ('integraciones', 'WhatsApp Cloud API, Meta, Stripe, Google Maps y muchas más')]),
   ('cell-5', 'build', 'frontend', 'Frontend y WordPress', 'Interfaces en TypeScript, React y Next.js. WordPress a medida, multisite y multilenguaje.', [('interfaces', 'TypeScript, React, Next.js, Tailwind'), ('cms', 'WordPress multisite, temas a medida'), ('despliegue', 'AWS Amplify, Vercel')]),
   ('cell-4', 'ops', 'infra', 'Infraestructura', '50+ entornos productivos con 99.9% de uptime y migraciones sin downtime.', [('cloud', 'AWS (EC2, S3, Lambda, Amplify, Route 53), DigitalOcean'), ('contenedores', 'Docker'), ('servidores', 'Apache, Ubuntu, Hestia'), ('entrega', 'CI/CD, Git')]),
   ('cell-4', 'ops', 'calidad', 'Testing E2E', 'Pruebas end-to-end automatizadas en Finwaise y depuración en el navegador.', [('e2e', 'Playwright'), ('depuración', 'Chrome DevTools'), ('entornos', 'staging y producción')]),
   ('cell-4 cell-tint', 'ai', 'diseño', 'Diseño y contenido', 'Maqueto, edito y animo. Ahora también genero imagen, voz y video con IA.', [('diseño', 'Figma, Illustrator'), ('motion', 'After Effects, Remotion'), ('generativa', 'ElevenLabs, modelos de imagen, Pexels')]),
   ('cell-6', 'base', 'negocio', 'Finanzas y procesos', 'Experiencia en contabilidad, finanzas y mapeo de procesos. Hablo el idioma de un ERP.', [('dominio', 'contabilidad, finanzas, conciliaciones'), ('análisis', 'mapeo de procesos, Tableau')]),
   ('cell-6', 'base', 'equipo', 'Equipo y metodología', 'Trabajo con metodologías ágiles. Manuales y capacitaciones que subieron la eficiencia del equipo un 40%, y formo a nuevos desarrolladores.', [('metodologías', 'Agile, Scrum, Kanban'), ('gestión', 'Jira, Confluence, Bitbucket'), ('práctica', 'documentación, capacitación, onboarding')]),
  ],
  fw_what='ERP con IA nativa para empresas con operaciones financieras complejas.',
  fw_team='Un producto grande, hecho en equipo. Estoy involucrado en todo el proyecto; estas son las partes donde más aporto:',
  involved=[('ai', '<strong>Agente Finy</strong>: extracción, clasificación y conciliación con LLMs.'),
            ('ops', '<strong>Motor de verificación</strong>: 60+ controles fiscales y contables antes de tocar los libros.'),
            ('build', '<strong>Módulos ERP</strong>: cuentas por pagar, ventas, tesorería, contabilidad y reportes.'),
            ('build', '<strong>Pipeline de documentos</strong>: OCR con AWS Textract, estructuración con LLMs y orquestación de workflows.'),
            ('ops', '<strong>Testing E2E</strong> con Playwright y Chrome DevTools.'),
            ('ai', '<strong>Campañas con IA generativa</strong> para la nueva área de mercadeo.'),
            ('base', '<strong>Claude Code y MCP</strong> como forma de trabajo del desarrollo.')],
  flow_label='Dos flujos de Finwaise: facturas que pasan por OCR, el agente Finy y 60+ controles hasta los módulos ERP; y campañas donde un brief se convierte en imagen, voz y video con IA.',
  flow_note='dos flujos de Finwaise, simplificados',
  flow={'inv': ('entrada', 'Factura', 'email, WhatsApp, API'), 'ocr': ('ocr', 'AWS Textract', 'texto y tablas'),
        'finy': ('agente', 'Finy', 'estructura, clasifica, concilia'), 'ctrl': ('validación', '60+ controles', 'CUIT, CAE, IVA, duplicados'),
        'erp': ('salida', 'Módulos ERP', 'libros, IVA, tesorería'), 'brief': ('entrada', 'Brief de campaña', 'mercadeo'),
        'gen': ('generativo', 'Imagen y voz', 'modelos de imagen, ElevenLabs'), 'video': ('salida', 'Video', 'Remotion, Pexels')},
  work_title='Proyectos',
  work_intro='Lo que construí con deLaGuayaba S.A. para sus clientes desde 2019, más mis proyectos propios.',
  groups=[
   ('ai', 'producto e ia', 'Producto, bots e IA', [
     ('Finwaise', 'https://finwaise.io', '', 'ERP con IA nativa. Agente Finy, verificación, módulos ERP, testing E2E y campañas con IA.', 'LLMs · agentes · OCR · AWS · Playwright'),
     ('wasa.app', 'https://wasa.app', '2022 - 2024', 'Chatbot de e-commerce sobre WhatsApp: pedidos, búsqueda de propiedades y panel en React. Scraping con IA para campañas.', 'Ruby on Jets · AWS Lambda · WhatsApp Cloud API · React · Meta'),
     ('Division50', 'https://division50.com', '', 'Chatbot de gestión de campañas en WhatsApp y workflows de scraping para marketing.', 'Ruby on Jets · WhatsApp Cloud API · scraping'),
     ('Licitaciones públicas, Ecuador', '', '', 'Scraping automatizado de portales de compras públicas de Ecuador, con procesamiento y análisis de datos asistido por IA.', 'scraping · LLMs · n8n · Supabase'),
     ('Doorvel', 'https://doorvel.com', '2021 - 2022', 'MVP inmobiliario y e-commerce en México: suscripciones, pagos, 6,000+ propiedades migradas y 200,000+ archivos en la nube. Después, migración a Python y React.', 'WordPress · Google Maps API · cloud storage · React')]),
   ('build', 'plataformas', 'Plataformas y consultoría', [
     ('küikmatch', 'https://kuikmatch.com', '2020 - hoy', 'Plataforma para emprendedores: academia online, comunidades, membresías, directorios georreferenciados y tickets. 3,000+ usuarios y 600+ empresas. Además, inteligencia inmobiliaria: ~12 scrapers automáticos de propiedades de Costa Rica y 8 tableros en Metabase, self-hosted en DigitalOcean.', 'WordPress Multisite · BuddyBoss · LMS · Stripe · scraping · Metabase · DigitalOcean'),
     ('Control Car BAC', '', '2019', 'Consultoría: mapeo de procesos, revisión y fusión de bases de datos, implementación de Intercom y un mapa de 400+ estaciones de servicio en Centroamérica.', 'procesos · SQL · Intercom · Google Maps')]),
   ('ops', 'wordpress + aws', 'Sitios corporativos', [
     ('Cámara de Bancos CR', 'https://camaradebancos.fi.cr', '', 'Gremio bancario de Costa Rica: tema propio, newsletter y datos de Bloomberg.', ''),
     ('ABC Dust', 'https://abcdust.net', '', 'Control de polvo y calidad del aire para minería y construcción, en 4 idiomas.', ''),
     ('Voces Vitales Costa Rica', 'https://vocesvitales.org', '', 'Red de liderazgo femenino: eventos, donaciones y WhatsApp.', ''),
     ('Grupo TLA', 'https://grupotla.com', '', 'Logística y aduanas en Centroamérica, Perú y Miami, sobre AWS EC2.', ''),
     ('Neutral Logistix', 'https://neutral-log.com', '', 'Operador logístico en 11 países, sobre AWS EC2.', ''),
     ('ALPROSA', 'https://alprosaguate.com', '', 'Almacén fiscal en Guatemala, con foco en seguridad.', '')]),
   ('base', 'propios', 'Proyectos propios', [
     ('Iglesia Central AD', 'https://www.iglesiacentralad.org/', '2026', 'Sitio bilingüe y un panel para el equipo: arman el orden de cada servicio, el set de alabanza y los roles por área, con disponibilidad, plantillas y ensayos. El programa se publica como app instalable con recordatorios push, PDF y exportación a Excel.', 'Next.js · TypeScript · Postgres · Auth.js · Web Push · Vercel'),
     ('Clear Books', 'https://pelozok.github.io/clear-books/', '', 'Control de presupuesto y salario: SPA con gráficas y Firebase.', 'React · Vite · Tailwind · Recharts · Firebase')]),
  ],
  xp_title='Experiencia', xp_when='Abr 2019 - hoy', xp_role='Software Developer &amp; AI Solutions Engineer', xp_org='deLaGuayaba S.A., Costa Rica',
  xp_points=[
   'Desarrollo full stack para clientes de Latinoamérica, de la idea a producción: TypeScript, React, WordPress, APIs, datos e infraestructura.',
   'En <strong>Finwaise</strong>, dentro del equipo: agente Finy, motor de verificación, módulos ERP, testing E2E y campañas con IA generativa.',
   'Diseñé el pipeline de documentos: OCR con <strong>AWS Textract</strong>, estructuración con <strong>LLMs</strong> y orquestación de workflows.',
   'Lideré el desarrollo de <strong>küikmatch</strong> (3,000+ usuarios, 600+ empresas) y su inteligencia inmobiliaria: <strong>~12 scrapers</strong> de propiedades y <strong>8 tableros en Metabase</strong>, self-hosted en DigitalOcean.',
   'Scraping y análisis con IA de licitaciones públicas de Ecuador; herramientas internas con n8n, Supabase, Mistral, OpenRouter y Lovable.',
   '<strong>50+ entornos productivos</strong> con 99.9% de uptime y migraciones sin downtime.',
   'Piloteé herramientas de IA con el equipo, recogí feedback y escalé lo que funcionó, incluidas guías de desarrollo asistido por IA.',
   'Documentación y capacitaciones: <strong>+40%</strong> de eficiencia del equipo. Apoyo técnico a ventas: <strong>+63%</strong> de visitas al sitio.'],
  facts=[('educación', ['<strong>Ingeniería en Sistemas</strong>', 'Universidad Americana (UAM), 2011 - 2015']),
         ('certificaciones', ['GitHub para programadores, LinkedIn Learning, 2021', 'Meta Ads (Facebook, Instagram, WhatsApp), 2021', 'JavaScript, Udemy, 2024']),
         ('idiomas', ['<strong>Español</strong> nativo', '<strong>Inglés</strong> B2, profesional']),
         ('ciudadanía', ['<strong>Polaca</strong> y <strong>argentina</strong>', 'Vivo en Costa Rica'])],
  contact_title='<em>Hablemos</em>.',
  contact_lede='Para proyectos, colaboraciones o para conversar sobre software e IA en producción. Respondo rápido por correo o LinkedIn.',
  updated=f'Actualizado el <time datetime="{TODAY}">13 de octubre de 2026</time>.',
 ),
}

EN_NODES = {
 'uam': ('education', 'Systems Engineering', 'UAM, 2015'), 'fin': ('business', 'Finance &amp; processes', 'Control Car BAC'),
 'wp': ('web', 'WordPress · PHP · Amplify', '50+ sites'), 'rails': ('backend', 'Bots &amp; backends', 'Ruby on Jets, 2022 - 24'),
 'react': ('frontend', 'TypeScript · React', 'Next.js, interfaces'), 'api': ('integrations', 'APIs &amp; data', 'scraping, Metabase and more'),
 'infra': ('infra', 'AWS · Docker', '99.9% uptime'), 'qa': ('quality', 'E2E testing', 'Playwright'),
 'ai': ('ai', 'Applied AI', 'LLMs and agents'), 'fw': ('now', 'Finwaise', 'AI-native ERP'), 'own': ('own', 'Own projects', 'Iglesia Central, Clear Books'),
}
es = T['es']
T['en'] = dict(es,
  lang='en', path='en/', cv_file='Kevin-Pelozo-Retamar-CV-2026.pdf', other='/', other_label='ES', other_lang='es', other_aria='Leer en español',
  title='Kevin Pelozo | Software &amp; AI Engineer in Costa Rica',
  desc='Kevin Pelozo Retamar, Software Engineer in Costa Rica. Full stack (TypeScript, React, WordPress, APIs, AWS) and applied AI in production, now at Finwaise.',
  og_desc='I build end to end and bring AI into production. Now at Finwaise, an AI-native ERP.',
  og_alt='Kevin Pelozo, Software &amp; AI Engineer: his experience as a node graph converging on Finwaise.',
  locale='en_US', locale_alt='es_CR',
  skip='Skip to content', home='Kevin Pelozo, home', navlabel='Main',
  nav=[('#skills', 'Skills'), ('#finwaise', 'Finwaise'), ('#work', 'Projects'), ('#experience', 'Experience'), ('#contact', 'Contact')],
  role='Software Engineer · <em>applied AI</em>',
  lede='I build end to end: TypeScript, React, WordPress, APIs and AWS infrastructure. Now I bring AI into all of it, in production.',
  cv='Download CV', mail='Email me',
  graph_label='Graph of my experience: education, web, platform and AI converge on Finwaise, next to my own projects.',
  graph_note='my experience, as a graph',
  nodes=EN_NODES,
  skills_title='The whole stack, with AI on top.',
  skills_intro='I have been shipping for real clients since 2019. AI does not replace that craft: it multiplies it.',
  ai_kind='ai', ai_h='Applied AI',
  ai_p='I take language models into real products: with real data, validation, costs and users.',
  ai_list=[('AI inside the product', 'Finy and the Finwaise verification engine: extract, classify, reconcile and validate before anything reaches the books.'),
           ('Agentic development', 'Claude Code and MCP servers as my daily way of working, and AI adoption across the team.'),
           ('Generative AI', 'Marketing campaigns with generated images, voice and video.'),
           ('Document pipelines', 'OCR, LLMs and APIs end to end, with validation and retries.')],
  ai_tools=[('models', 'Claude, OpenAI, Gemini, Mistral (via OpenRouter)'), ('agents', 'tool use, MCP, prompt engineering'), ('orchestration', 'document pipelines, OCR, API integration'), ('generative', 'image, voice and video'), ('development', 'Claude Code, Cursor, GitHub Copilot, Lovable')],
  cells=[
   ('cell-5', 'build', 'backend', 'Backend, APIs &amp; data', 'APIs, integrations, bots and data scraping, with dashboards to analyse it.', [('languages', 'TypeScript, JavaScript, PHP, Ruby'), ('backends', 'REST APIs, WordPress, Ruby on Jets (2022 - 24)'), ('data', 'PostgreSQL, MySQL, SQL Server, Supabase, Metabase'), ('integrations', 'WhatsApp Cloud API, Meta, Stripe, Google Maps and many more')]),
   ('cell-5', 'build', 'frontend', 'Frontend &amp; WordPress', 'Interfaces in TypeScript, React and Next.js. Custom WordPress, multisite and multilingual.', [('interfaces', 'TypeScript, React, Next.js, Tailwind'), ('cms', 'WordPress multisite, custom themes'), ('deploy', 'AWS Amplify, Vercel')]),
   ('cell-4', 'ops', 'infra', 'Infrastructure', '50+ production environments at 99.9% uptime, with zero-downtime migrations.', [('cloud', 'AWS (EC2, S3, Lambda, Amplify, Route 53), DigitalOcean'), ('containers', 'Docker'), ('servers', 'Apache, Ubuntu, Hestia'), ('delivery', 'CI/CD, Git')]),
   ('cell-4', 'ops', 'quality', 'E2E testing', 'Automated end-to-end tests on Finwaise and in-browser debugging.', [('e2e', 'Playwright'), ('debugging', 'Chrome DevTools'), ('environments', 'staging and production')]),
   ('cell-4 cell-tint', 'ai', 'design', 'Design &amp; content', 'I lay out, edit and animate. Now I also generate images, voice and video with AI.', [('design', 'Figma, Illustrator'), ('motion', 'After Effects, Remotion'), ('generative', 'ElevenLabs, image models, Pexels')]),
   ('cell-6', 'base', 'business', 'Finance &amp; processes', 'Background in accounting, finance and process mapping. I speak the language of an ERP.', [('domain', 'accounting, finance, reconciliations'), ('analysis', 'process mapping, Tableau')]),
   ('cell-6', 'base', 'team', 'Team &amp; methodology', 'I work with agile methodologies. Manuals and training that raised team efficiency by 40%, and I onboard new developers.', [('methodologies', 'Agile, Scrum, Kanban'), ('management', 'Jira, Confluence, Bitbucket'), ('practice', 'documentation, training, onboarding')]),
  ],
  fw_what='An AI-native ERP for companies with complex financial operations.',
  fw_team='A large product, built by a team. I am involved across the whole project; these are the parts where I contribute most:',
  involved=[('ai', '<strong>Finy agent</strong>: extraction, classification and reconciliation with LLMs.'),
            ('ops', '<strong>Verification engine</strong>: 60+ tax and accounting checks before anything reaches the books.'),
            ('build', '<strong>ERP modules</strong>: payables, sales, treasury, accounting and reporting.'),
            ('build', '<strong>Document pipeline</strong>: OCR with AWS Textract, structuring with LLMs and workflow orchestration.'),
            ('ops', '<strong>E2E testing</strong> with Playwright and Chrome DevTools.'),
            ('ai', '<strong>Generative AI campaigns</strong> for the new marketing team.'),
            ('base', '<strong>Claude Code and MCP</strong> as the way development gets done.')],
  flow_label='Two Finwaise flows: invoices go through OCR, the Finy agent and 60+ checks into the ERP modules; and campaigns where a brief becomes AI-generated image, voice and video.',
  flow_note='two Finwaise flows, simplified',
  flow={'inv': ('input', 'Invoice', 'email, WhatsApp, API'), 'ocr': ('ocr', 'AWS Textract', 'text and tables'),
        'finy': ('agent', 'Finy', 'structures, classifies, reconciles'), 'ctrl': ('validation', '60+ checks', 'tax ID, CAE, VAT, duplicates'),
        'erp': ('output', 'ERP modules', 'books, VAT, treasury'), 'brief': ('input', 'Campaign brief', 'marketing'),
        'gen': ('generative', 'Image &amp; voice', 'image models, ElevenLabs'), 'video': ('output', 'Video', 'Remotion, Pexels')},
  work_title='Projects',
  work_intro='What I built with deLaGuayaba S.A. for its clients since 2019, plus my own projects.',
  groups=[
   ('ai', 'product &amp; ai', 'Product, bots &amp; AI', [
     ('Finwaise', 'https://finwaise.io', '', 'AI-native ERP. Finy agent, verification, ERP modules, E2E testing and AI campaigns.', es['groups'][0][3][0][4]),
     ('wasa.app', 'https://wasa.app', '2022 - 2024', 'E-commerce chatbot on WhatsApp: orders, property search and a React admin. AI scraping for campaigns.', es['groups'][0][3][1][4]),
     ('Division50', 'https://division50.com', '', 'WhatsApp chatbot for campaign management, plus scraping workflows for marketing.', es['groups'][0][3][2][4]),
     ('Public procurement, Ecuador', '', '', 'Automated scraping of Ecuador public procurement portals, with AI-assisted data processing and analysis.', 'scraping · LLMs · n8n · Supabase'),
     ('Doorvel', 'https://doorvel.com', '2021 - 2022', 'Real-estate and e-commerce MVP in Mexico: subscriptions, payments, 6,000+ properties migrated and 200,000+ media files in the cloud. Then a migration to Python and React.', es['groups'][0][3][3][4])]),
   ('build', 'platforms', 'Platforms &amp; consulting', [
     ('küikmatch', 'https://kuikmatch.com', '2020 - now', 'A platform for entrepreneurs: online academy, communities, memberships, geo-referenced directories and tickets. 3,000+ users and 600+ companies. Plus real-estate intelligence: ~12 automated scrapers of Costa Rica property listings and 8 Metabase dashboards, self-hosted on DigitalOcean.', 'WordPress Multisite · BuddyBoss · LMS · Stripe · scraping · Metabase · DigitalOcean'),
     ('Control Car BAC', '', '2019', 'Consulting: process mapping, database reviews and merges, an Intercom rollout and a map of 400+ service stations across Central America.', 'processes · SQL · Intercom · Google Maps')]),
   ('ops', 'wordpress + aws', 'Corporate sites', [
     ('Cámara de Bancos CR', 'https://camaradebancos.fi.cr', '', 'Costa Rica banking association: custom theme, newsletter and Bloomberg data.', ''),
     ('ABC Dust', 'https://abcdust.net', '', 'Dust control and air quality for mining and construction, in 4 languages.', ''),
     ('Voces Vitales Costa Rica', 'https://vocesvitales.org', '', 'Women\'s leadership network: events, donations and WhatsApp.', ''),
     ('Grupo TLA', 'https://grupotla.com', '', 'Logistics and customs across Central America, Peru and Miami, on AWS EC2.', ''),
     ('Neutral Logistix', 'https://neutral-log.com', '', 'Logistics operator in 11 countries, on AWS EC2.', ''),
     ('ALPROSA', 'https://alprosaguate.com', '', 'Bonded warehouse in Guatemala, focused on security.', '')]),
   ('base', 'my own', 'My own projects', [
     ('Iglesia Central AD', 'https://www.iglesiacentralad.org/', '2026', 'A bilingual site plus a panel for the team: they build each service order, the worship set and roles per area, with availability, templates and rehearsals. The program ships as an installable app with push reminders, PDF and Excel export.', 'Next.js · TypeScript · Postgres · Auth.js · Web Push · Vercel'),
     ('Clear Books', 'https://pelozok.github.io/clear-books/', '', 'Budget and salary tracking: a SPA with charts and Firebase.', 'React · Vite · Tailwind · Recharts · Firebase')]),
  ],
  xp_title='Experience', xp_when='Apr 2019 - now', xp_org='deLaGuayaba S.A., Costa Rica',
  xp_points=[
   'Full-stack development for clients across Latin America, from idea to production: TypeScript, React, WordPress, APIs, data and infrastructure.',
   'At <strong>Finwaise</strong>, as part of the team: Finy agent, verification engine, ERP modules, E2E testing and generative AI campaigns.',
   'Designed the document pipeline: OCR with <strong>AWS Textract</strong>, structuring with <strong>LLMs</strong> and workflow orchestration.',
   'Led development of <strong>küikmatch</strong> (3,000+ users, 600+ companies) and its real-estate intelligence: <strong>~12 scrapers</strong> of property listings and <strong>8 Metabase dashboards</strong>, self-hosted on DigitalOcean.',
   'AI-assisted scraping and analysis of public procurement in Ecuador; internal tools with n8n, Supabase, Mistral, OpenRouter and Lovable.',
   '<strong>50+ production environments</strong> at 99.9% uptime, with zero-downtime migrations.',
   'Piloted AI tools with the team, gathered feedback and scaled what worked, including guidelines for AI-assisted development.',
   'Documentation and training: <strong>+40%</strong> team efficiency. Technical support for sales: <strong>+63%</strong> site visits.'],
  facts=[('education', ['<strong>Systems Engineering</strong>', 'Universidad Americana (UAM), 2011 - 2015']),
         ('certifications', ['GitHub for developers, LinkedIn Learning, 2021', 'Meta Ads (Facebook, Instagram, WhatsApp), 2021', 'JavaScript, Udemy, 2024']),
         ('languages', ['<strong>Spanish</strong> native', '<strong>English</strong> B2, professional']),
         ('citizenship', ['<strong>Polish</strong> and <strong>Argentinian</strong>', 'Based in Costa Rica'])],
  contact_title='<em>Let\'s talk</em>.',
  contact_lede='For projects, collaborations or a conversation about software and AI in production. I reply quickly by email or LinkedIn.',
  updated=f'Updated <time datetime="{TODAY}">October 13, 2026</time>.',
)

# ---------------------------------------------------------------- render

def render_graph(t):
    out = [f'<figure class="canvas graph" data-canvas aria-label="{t["graph_label"]}">',
           f'  <svg class="canvas-edges" viewBox="0 0 {GW} {GH}" preserveAspectRatio="none" aria-hidden="true" focusable="false">']
    for a, b in GEDGES:
        cls = 'edge' + (' is-ai' if b in ('ai', 'fw') and a in ('ai', 'api', 'infra', 'qa', 'fin') and False else '')
        if (a, b) in (('api', 'ai'), ('ai', 'fw')): cls += ' is-ai'
        if b == 'next': cls += ' is-next'
        out.append(f'    <path class="{cls}" data-from="{a}" data-to="{b}" d="{graph_edge(a, b)}"/>')
    flows = [(['uam', 'rails', 'api', 'ai', 'fw'], 'var(--ai)', '5.5s', '0s'),
             (['wp', 'infra', 'fw'], 'var(--k-build)', '4.2s', '1.2s'),
             (['react', 'qa', 'fw'], 'var(--k-ops)', '4.6s', '2.4s')]
    out.append(f'    <g class="ports">{graph_ports()}</g>')
    out.append('    <g class="flow">')
    for ids, color, dur, begin in flows:
        d = chain(ids, graph_edge)
        out.append(f'      <circle r="4.5" fill="{color}"><animateMotion dur="{dur}" begin="{begin}" repeatCount="indefinite" path="{d}"/></circle>')
    out.append(f'      <circle r="4.5" fill="var(--ink-3)"><animateMotion dur="6s" begin="0.6s" repeatCount="indefinite" path="{graph_edge("fin", "fw")}"/></circle>')
    out.append('    </g>\n  </svg>')
    for nid, col, y, kind, href, extra in GRAPH:
        k, title, sub = t['nodes'][nid]
        cls = 'node' + (' ' + extra if extra else '')
        out.append(f'  <a class="{cls}" data-id="{nid}" data-k="{kind}" href="{href}"><span class="kind">{k}</span><b>{title}</b><small>{sub}</small></a>')
    out.append(f'  <figcaption class="canvas-note">{t["graph_note"]}</figcaption>\n</figure>')
    return '\n'.join('          ' + l for l in out)

def render_flow(t):
    out = [f'<figure class="canvas flowchart" data-canvas aria-label="{t["flow_label"]}">',
           f'  <svg class="canvas-edges" viewBox="0 0 {FW} {FH}" preserveAspectRatio="none" aria-hidden="true" focusable="false">']
    for a, b in FEDGES:
        cls = 'edge' + (' is-ai' if 'finy' in (a, b) or 'gen' in (a, b) else '')
        out.append(f'    <path class="{cls}" data-from="{a}" data-to="{b}" d="{edge_path(fbox(a), fbox(b))[0]}"/>')
    fd = chain(['inv', 'ocr', 'finy', 'ctrl', 'erp'], lambda a, b: edge_path(fbox(a), fbox(b))[0])
    gd = chain(['brief', 'gen', 'video'], lambda a, b: edge_path(fbox(a), fbox(b))[0])
    out.append(f'    <g class="flow"><circle r="4.5" fill="var(--ai)"><animateMotion dur="5s" repeatCount="indefinite" path="{fd}"/></circle>'
               f'<circle r="4.5" fill="var(--k-build)"><animateMotion dur="3.6s" begin="1s" repeatCount="indefinite" path="{gd}"/></circle></g>')
    out.append('  </svg>')
    for nid, x, y, kind, extra in FLOW:
        k, title, sub = t['flow'][nid]
        cls = 'node' + (' ' + extra if extra else '')
        out.append(f'  <div class="{cls}" data-id="{nid}" data-k="{kind}"><span class="kind">{k}</span><b>{title}</b><small>{sub}</small></div>')
    out.append(f'  <figcaption class="canvas-note">{t["flow_note"]}</figcaption>\n</figure>')
    return '\n'.join('          ' + l for l in out)

def ld(t):
    url = 'https://pelozok.github.io/' + t['path']
    graph = {
      '@context': 'https://schema.org',
      '@graph': [
        {'@type': 'WebSite', '@id': 'https://pelozok.github.io/#website', 'url': 'https://pelozok.github.io/', 'name': 'Kevin Pelozo',
         'alternateName': ['Kevin Pelozo Retamar', 'pelozok'], 'inLanguage': ['es', 'en']},
        {'@type': 'ProfilePage', '@id': url + '#profilepage', 'url': url, 'name': t['title'].replace('&amp;', '&'), 'inLanguage': t['lang'],
         'isPartOf': {'@id': 'https://pelozok.github.io/#website'}, 'dateCreated': '2025-05-20', 'dateModified': TODAY,
         'mainEntity': {'@id': 'https://pelozok.github.io/#person'}},
        {'@type': 'Person', '@id': 'https://pelozok.github.io/#person', 'name': 'Kevin Daniel Pelozo Retamar',
         'alternateName': ['Kevin Pelozo', 'Kevin Pelozo Retamar', 'pelozok'], 'givenName': 'Kevin', 'familyName': 'Pelozo Retamar',
         'url': 'https://pelozok.github.io/', 'image': 'https://pelozok.github.io/assets/img/og-image.png', 'email': 'mailto:kevindp2008@gmail.com',
         'jobTitle': 'Software Engineer & AI Engineer', 'description': t['desc'],
         'worksFor': {'@type': 'Organization', 'name': 'deLaGuayaba S.A.'},
         'alumniOf': {'@type': 'CollegeOrUniversity', 'name': 'Universidad Americana (UAM)'},
         'address': {'@type': 'PostalAddress', 'addressCountry': 'CR'},
         'nationality': [{'@type': 'Country', 'name': 'Poland'}, {'@type': 'Country', 'name': 'Argentina'}],
         'knowsLanguage': ['es', 'en'],
         'knowsAbout': ['Software engineering', 'Full-stack development', 'Artificial Intelligence', 'AI agents', 'LLM applications',
                        'Agentic software development', 'Claude Code', 'Model Context Protocol (MCP)', 'OpenAI API', 'Gemini', 'n8n',
                        'AWS Textract', 'TypeScript', 'React', 'Next.js', 'WordPress', 'AWS Amplify', 'Web scraping', 'Metabase', 'Supabase', 'REST APIs', 'WhatsApp Cloud API', 'AWS', 'Docker',
                        'Playwright', 'End-to-end testing', 'Generative AI', 'Agile', 'Scrum'],
         'sameAs': ['https://www.linkedin.com/in/kevin-pelozo/', 'https://github.com/pelozok']},
      ]}
    return json.dumps(graph, ensure_ascii=False, indent=2).replace('\n', '\n  ')

def tools_dl(pairs):
    rows = ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in pairs)
    return f'<dl class="tools">{rows}</dl>'

def page(t):
    url = 'https://pelozok.github.io/' + t['path']
    nav = '\n        '.join(f'<a href="{h}">{l}</a>' for h, l in t['nav'])
    ai_list = '\n'.join(f'                <li><b>{h}</b><span>{p}</span></li>' for h, p in t['ai_list'])
    cells = '\n'.join(
        f'''            <article class="cell {c}" data-k="{k}">
              <h3 class="k-head">{h}</h3>
              <p>{p}</p>
              {tools_dl(tools)}
            </article>''' for c, k, kl, h, p, tools in t['cells'])
    involved = '\n'.join(f'              <li data-k="{k}"><span>{s}</span></li>' for k, s in t['involved'])
    groups = []
    for k, kl, h, items in t['groups']:
        rows = []
        for name, href, when, desc, stack in items:
            nm = f'<a href="{href}" rel="noopener">{name}{ARROW}</a>' if href else name
            rows.append(f'''              <li class="proj{' is-compact' if not stack else ''}">
                <p class="proj-name">{nm}</p>
                {f'<p class="proj-when">{when}</p>' if when else '<span></span>'}
                <p class="proj-desc">{desc}</p>
                {f'<p class="proj-stack">{stack}</p>' if stack else ''}
              </li>''')
        groups.append(f'''          <div class="group" data-k="{k}">
            <div class="group-head"><h3 class="k-head">{h}</h3></div>
            <ul>
{chr(10).join(rows)}
            </ul>
          </div>''')
    points = '\n'.join(f'                <li>{p}</li>' for p in t['xp_points'])
    facts = '\n'.join(f'          <div><dt>{dt}</dt>' + ''.join(f'<dd>{d}</dd>' for d in dds) + '</div>' for dt, dds in t['facts'])
    return f'''<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'none'; manifest-src 'self'; base-uri 'none'; form-action 'none'; object-src 'none'">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>{t['title']}</title>
  <meta name="description" content="{t['desc']}">
  <meta name="author" content="Kevin Daniel Pelozo Retamar">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="es" href="https://pelozok.github.io/">
  <link rel="alternate" hreflang="en" href="https://pelozok.github.io/en/">
  <link rel="alternate" hreflang="x-default" href="https://pelozok.github.io/">

  <meta property="og:type" content="profile">
  <meta property="og:site_name" content="Kevin Pelozo">
  <meta property="og:title" content="Kevin Pelozo | Software &amp; AI Engineer">
  <meta property="og:description" content="{t['og_desc']}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="https://pelozok.github.io/assets/img/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{t['og_alt']}">
  <meta property="og:locale" content="{t['locale']}">
  <meta property="og:locale:alternate" content="{t['locale_alt']}">
  <meta property="profile:first_name" content="Kevin">
  <meta property="profile:last_name" content="Pelozo Retamar">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Kevin Pelozo | Software &amp; AI Engineer">
  <meta name="twitter:description" content="{t['og_desc']}">
  <meta name="twitter:image" content="https://pelozok.github.io/assets/img/og-image.png">

  <link rel="icon" href="/favicon.ico" sizes="48x48">
  <link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#f4f5f7" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0d0f13" media="(prefers-color-scheme: dark)">

  <link rel="preload" href="/assets/fonts/geist-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/css/styles.css">

  <script type="application/ld+json">
  {ld(t)}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">{t['skip']}</a>

  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="#top" aria-label="{t['home']}"><span class="brand-mark" aria-hidden="true"></span><span>Kevin Pelozo</span></a>
      <nav class="site-nav" aria-label="{t['navlabel']}">
        {nav}
      </nav>
      <a class="lang-switch" href="{t['other']}" hreflang="{t['other_lang']}" lang="{t['other_lang']}" aria-label="{t['other_aria']}">{t['other_label']}</a>
    </div>
  </header>

  <main id="main">
    <section class="hero" id="top">
      <div class="wrap hero-grid">
        <div>
          <h1 class="hero-name">Kevin Pelozo</h1>
          <p class="hero-role">{t['role']}</p>
          <p class="hero-lede">{t['lede']}</p>
          <div class="actions">
            <a class="btn" href="/assets/files/{t['cv_file']}" download>{DL}{t['cv']}</a>
            <a class="text-link" href="mailto:kevindp2008@gmail.com">{t['mail']}</a>
          </div>
        </div>
{render_graph(t)}
      </div>
    </section>

    <section class="section" id="skills" aria-labelledby="skillsTitle">
      <div class="wrap">
        <h2 class="section-title" id="skillsTitle">{t['skills_title']}</h2>
        <p class="section-intro">{t['skills_intro']}</p>
        <div class="bento">
            <article class="cell cell-ai" data-k="ai">
              <h3 class="k-head">{t['ai_h']}</h3>
              <p>{t['ai_p']}</p>
              <ul class="ai-list">
{ai_list}
              </ul>
              {tools_dl(t['ai_tools'])}
            </article>
{cells}
        </div>
      </div>
    </section>

    <section class="section" id="finwaise" aria-labelledby="finwaiseTitle">
      <div class="wrap case">
        <div>
          <h2 class="case-name" id="finwaiseTitle">Finwaise</h2>
          <p class="case-what">{t['fw_what']}</p>
          <p class="case-team">{t['fw_team']}</p>
          <ul class="involved">
{involved}
          </ul>
          <a class="text-link" href="https://finwaise.io" rel="noopener">finwaise.io</a>
        </div>
{render_flow(t)}
      </div>
    </section>

    <section class="section" id="work" aria-labelledby="workTitle">
      <div class="wrap">
        <h2 class="section-title" id="workTitle">{t['work_title']}</h2>
        <p class="section-intro">{t['work_intro']}</p>
        <div class="registry">
{chr(10).join(groups)}
        </div>
      </div>
    </section>

    <section class="section" id="experience" aria-labelledby="experienceTitle">
      <div class="wrap">
        <h2 class="section-title" id="experienceTitle">{t['xp_title']}</h2>
        <article class="xp">
          <p class="xp-when">{t['xp_when']}</p>
          <div>
            <h3 class="xp-role">{t['xp_role']}</h3>
            <p class="xp-org">{t['xp_org']}</p>
            <ul class="xp-points">
{points}
            </ul>
          </div>
        </article>
        <dl class="facts">
{facts}
        </dl>
      </div>
    </section>

    <section class="contact" id="contact" aria-labelledby="contactTitle">
      <div class="wrap">
        <h2 class="contact-title" id="contactTitle">{t['contact_title']}</h2>
        <p class="contact-lede">{t['contact_lede']}</p>
        <a class="contact-mail" href="mailto:kevindp2008@gmail.com">kevindp2008@gmail.com</a>
        <ul class="contact-links">
          <li><a href="https://www.linkedin.com/in/kevin-pelozo/" rel="me noopener">LinkedIn</a></li>
          <li><a href="https://github.com/pelozok" rel="me noopener">GitHub</a></li>
          <li><a href="/assets/files/{t['cv_file']}" download>{t['cv']}</a></li>
        </ul>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="wrap footer-inner">
      <p>© 2026 Kevin Daniel Pelozo Retamar</p>
      <p>{t['updated']}</p>
    </div>
  </footer>

  <script src="/assets/js/main.js" defer></script>
</body>
</html>
'''

for lang in ('es', 'en'):
    t = T[lang]
    out = os.path.join(ROOT, t['path'], 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(page(t))
    print('wrote', out)

css_path = os.path.join(ROOT, 'assets/css/styles.css')
css_src = open(css_path, encoding='utf-8').read()
marker = '/* ---- generated canvas geometry (do not edit by hand) ---- */'
if marker in css_src:
    css_src = css_src[:css_src.index(marker)]
open(css_path, 'w', encoding='utf-8').write(css_src.rstrip() + '\n\n' + GEN_CSS)
print('geometry css appended')
