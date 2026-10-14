#!/usr/bin/env python3
"""Builds the one-page CV PDFs (EN and ES) from the content below.

    python3 scripts/build_cv.py

Writes scripts/cv/cv-en.html and cv-es.html, then prints them to
assets/files/Kevin-Pelozo-Retamar-CV-2026.pdf (EN) and -ES.pdf (ES) with
headless Google Chrome. Each PDF must stay on a single page.
"""
import os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_HTML = os.path.join(ROOT, 'scripts', 'cv')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

C = {
 'en': dict(
  file='Kevin-Pelozo-Retamar-CV-2026.pdf',
  role='Software Engineer · Applied AI',
  contact=['kevindp2008@gmail.com', '(+506) 7007-3757', 'Costa Rica · open to remote', 'pelozok.github.io', 'linkedin.com/in/kevin-pelozo', 'github.com/pelozok'],
  summary='Software engineer with 7+ years shipping production software end to end: TypeScript, React and Next.js, WordPress and PHP, APIs, data and AWS infrastructure. Today I bring AI into real products: LLMs inside Finwaise, an AI-native ERP, agentic development with Claude Code and MCP, document pipelines, E2E testing and generative AI for marketing. Background in finance and process analysis.',
  h_xp='Experience', h_proj='Own projects', h_skills='Skills', h_edu='Education', h_cert='Certifications', h_lang='Languages', h_cit='Citizenship',
  job='Software Developer &amp; AI Solutions Engineer', org='deLaGuayaba S.A. · Costa Rica', when='Apr 2019 - Present',
  blocks=[
   ('Finwaise · AI-native ERP (team product)', [
     'Contribute across the product, mainly the <b>Finy agent</b> (LLM extraction, classification and bank reconciliation), the <b>verification engine</b> (60+ tax and accounting checks) and <b>ERP modules</b> (payables, sales, treasury, accounting, reporting).',
     'Designed the <b>document pipeline</b>: AWS Textract OCR, LLM structuring and validation, orchestrated as production workflows.',
     '<b>E2E testing</b> with Playwright and Chrome DevTools; <b>agentic development</b> with Claude Code and MCP servers.',
     '<b>Generative AI campaigns</b> for the new marketing team: images, voice (ElevenLabs) and video (Remotion).']),
   ('Client platforms', [
     '<b>küikmatch</b> (2020 - now): led a WordPress multisite platform with 3,000+ users and 600+ companies (LMS, communities, memberships, geo directories), plus real-estate intelligence: ~12 automated property scrapers and 8 Metabase dashboards, self-hosted on DigitalOcean.',
     '<b>wasa.app</b> (2022 - 2024): WhatsApp Cloud API e-commerce chatbot on Ruby on Jets and AWS Lambda, React admin, AI-assisted scraping. <b>Division50</b>: WhatsApp campaign chatbot. <b>Ecuador</b>: AI-assisted scraping of public procurement portals.',
     '<b>Doorvel</b> (2021 - 2022, Mexico): real-estate and e-commerce MVP with subscriptions and payments; migrated 6,000+ properties and 200,000+ media files; trained new developers.',
     '<b>Control Car BAC</b> (2019): process mapping, database review and merge, Intercom rollout, map of 400+ service stations.',
     'Corporate sites on WordPress and AWS: Cámara de Bancos CR, ABC Dust, Voces Vitales, Grupo TLA, Neutral Logistix, ALPROSA.']),
   ('Engineering and team', [
     '<b>50+ production environments</b> at 99.9% uptime, with zero-downtime migrations.',
     'Piloted AI tools with the team and scaled what worked. Documentation and training: <b>+40%</b> team efficiency. Technical support for sales: <b>+63%</b> site visits.']),
  ],
  projects=[
   '<b>Iglesia Central AD</b> (2026): bilingual site plus a team panel for service planning, worship sets, rotas and availability, with push reminders, PDF and Excel export. Next.js, TypeScript, Postgres, Auth.js.',
   '<b>Clear Books</b>: budget and salary tracker. React, Vite, Tailwind, Recharts, Firebase.'],
  skills=[
   ('AI', 'Claude (API, Claude Code), OpenAI, Gemini, Mistral via OpenRouter, MCP, agents and tool use, prompt engineering, OCR and document pipelines, workflow orchestration'),
   ('Generative', 'image models, ElevenLabs, Remotion, Pexels'),
   ('Backend', 'REST APIs, PHP, TypeScript, Ruby on Jets (2022 - 24), PostgreSQL, MySQL, SQL Server'),
   ('Data', 'web scraping, Metabase dashboards, Supabase'),
   ('Integrations', 'WhatsApp Cloud API, Meta, Stripe, Google Maps and many more'),
   ('Frontend', 'TypeScript, React, Next.js, Tailwind, WordPress (multisite, custom themes), AWS Amplify, Vercel'),
   ('Cloud', 'AWS (EC2, S3, Lambda, Amplify, Route 53, Textract), DigitalOcean, Docker, Apache, Ubuntu, CI/CD, Git'),
   ('Quality', 'Playwright, Chrome DevTools'),
   ('Ways of working', 'Agile, Scrum, Kanban, Jira, Confluence, Bitbucket'),
   ('Design', 'Figma, Illustrator, After Effects'),
   ('Business', 'accounting, finance, process mapping, Tableau'),
  ],
  edu=['<b>Systems Engineering</b>', 'Universidad Americana (UAM), 2011 - 2015'],
  certs=['GitHub for developers, LinkedIn Learning, 2021', 'Meta Ads (Facebook, Instagram, WhatsApp), 2021', 'JavaScript, Udemy, 2024'],
  langs=['<b>Spanish</b> native', '<b>English</b> B2, professional'],
  cit=['<b>Polish</b> and <b>Argentinian</b>'],
 ),
 'es': dict(
  file='Kevin-Pelozo-Retamar-CV-2026-ES.pdf',
  role='Software Engineer · IA aplicada',
  contact=['kevindp2008@gmail.com', '(+506) 7007-3757', 'Costa Rica · disponible remoto', 'pelozok.github.io', 'linkedin.com/in/kevin-pelozo', 'github.com/pelozok'],
  summary='Ingeniero de software con más de 7 años llevando software a producción de punta a punta: TypeScript, React y Next.js, WordPress y PHP, APIs, datos e infraestructura en AWS. Hoy sumo IA a productos reales: LLMs en Finwaise, un ERP con IA nativa, desarrollo agéntico con Claude Code y MCP, pipelines de documentos, testing E2E e IA generativa para mercadeo. Base en finanzas y análisis de procesos.',
  h_xp='Experiencia', h_proj='Proyectos propios', h_skills='Habilidades', h_edu='Educación', h_cert='Certificaciones', h_lang='Idiomas', h_cit='Ciudadanía',
  job='Software Developer &amp; AI Solutions Engineer', org='deLaGuayaba S.A. · Costa Rica', when='Abr 2019 - Presente',
  blocks=[
   ('Finwaise · ERP con IA nativa (producto de equipo)', [
     'Participo en todo el producto, sobre todo en el <b>agente Finy</b> (extracción, clasificación y conciliación bancaria con LLMs), el <b>motor de verificación</b> (60+ controles fiscales y contables) y los <b>módulos ERP</b> (cuentas por pagar, ventas, tesorería, contabilidad, reportes).',
     'Diseñé el <b>pipeline de documentos</b>: OCR con AWS Textract, estructuración y validación con LLMs, orquestado como workflows en producción.',
     '<b>Testing E2E</b> con Playwright y Chrome DevTools; <b>desarrollo agéntico</b> con Claude Code y servidores MCP.',
     '<b>Campañas con IA generativa</b> para la nueva área de mercadeo: imagen, voz (ElevenLabs) y video (Remotion).']),
   ('Plataformas para clientes', [
     '<b>küikmatch</b> (2020 - hoy): lideré una plataforma WordPress multisite con 3,000+ usuarios y 600+ empresas (LMS, comunidades, membresías, directorios geo), más inteligencia inmobiliaria: ~12 scrapers automáticos de propiedades y 8 tableros en Metabase, self-hosted en DigitalOcean.',
     '<b>wasa.app</b> (2022 - 2024): chatbot de e-commerce sobre WhatsApp Cloud API con Ruby on Jets y AWS Lambda, panel en React, scraping con IA. <b>Division50</b>: chatbot de campañas en WhatsApp. <b>Ecuador</b>: scraping de licitaciones públicas con análisis asistido por IA.',
     '<b>Doorvel</b> (2021 - 2022, México): MVP inmobiliario y e-commerce con suscripciones y pagos; migré 6,000+ propiedades y 200,000+ archivos; formé a nuevos desarrolladores.',
     '<b>Control Car BAC</b> (2019): mapeo de procesos, revisión y fusión de bases de datos, implementación de Intercom, mapa de 400+ estaciones de servicio.',
     'Sitios corporativos en WordPress y AWS: Cámara de Bancos CR, ABC Dust, Voces Vitales, Grupo TLA, Neutral Logistix, ALPROSA.']),
   ('Ingeniería y equipo', [
     '<b>50+ entornos productivos</b> con 99.9% de uptime y migraciones sin downtime.',
     'Piloteé herramientas de IA con el equipo y escalé lo que funcionó. Documentación y capacitaciones: <b>+40%</b> de eficiencia. Apoyo técnico a ventas: <b>+63%</b> de visitas.']),
  ],
  projects=[
   '<b>Iglesia Central AD</b> (2026): sitio bilingüe y panel para el equipo: planificación de servicios, sets de alabanza, roles y disponibilidad, con recordatorios push, PDF y Excel. Next.js, TypeScript, Postgres, Auth.js.',
   '<b>Clear Books</b>: control de presupuesto y salario. React, Vite, Tailwind, Recharts, Firebase.'],
  skills=[
   ('IA', 'Claude (API, Claude Code), OpenAI, Gemini, Mistral vía OpenRouter, MCP, agentes y tool use, prompt engineering, OCR y pipelines de documentos, orquestación de workflows'),
   ('Generativa', 'modelos de imagen, ElevenLabs, Remotion, Pexels'),
   ('Backend', 'APIs REST, PHP, TypeScript, Ruby on Jets (2022 - 24), PostgreSQL, MySQL, SQL Server'),
   ('Datos', 'web scraping, tableros en Metabase, Supabase'),
   ('Integraciones', 'WhatsApp Cloud API, Meta, Stripe, Google Maps y muchas más'),
   ('Frontend', 'TypeScript, React, Next.js, Tailwind, WordPress (multisite, temas a medida), AWS Amplify, Vercel'),
   ('Cloud', 'AWS (EC2, S3, Lambda, Amplify, Route 53, Textract), DigitalOcean, Docker, Apache, Ubuntu, CI/CD, Git'),
   ('Calidad', 'Playwright, Chrome DevTools'),
   ('Metodologías', 'Agile, Scrum, Kanban, Jira, Confluence, Bitbucket'),
   ('Diseño', 'Figma, Illustrator, After Effects'),
   ('Negocio', 'contabilidad, finanzas, mapeo de procesos, Tableau'),
  ],
  edu=['<b>Ingeniería en Sistemas</b>', 'Universidad Americana (UAM), 2011 - 2015'],
  certs=['GitHub para programadores, LinkedIn Learning, 2021', 'Meta Ads (Facebook, Instagram, WhatsApp), 2021', 'JavaScript, Udemy, 2024'],
  langs=['<b>Español</b> nativo', '<b>Inglés</b> B2, profesional'],
  cit=['<b>Polaca</b> y <b>argentina</b>'],
 ),
}

CSS = '''
@font-face { font-family: 'Geist'; src: url('../../assets/fonts/geist-latin-wght-normal.woff2') format('woff2'); font-weight: 100 900; }
@font-face { font-family: 'Geist'; src: url('../../assets/fonts/geist-latin-ext-wght-normal.woff2') format('woff2'); font-weight: 100 900; unicode-range: U+0100-02BA, U+1E00-1EFF; }
@font-face { font-family: 'Geist Mono'; src: url('../../assets/fonts/geist-mono-latin-wght-normal.woff2') format('woff2'); font-weight: 100 900; }
@page { size: Letter; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; }
body { width: 8.5in; height: 11in; padding: 0.42in 0.5in 0.36in; font-family: 'Geist', sans-serif; font-size: SIZEpt; line-height: 1.38; color: #0e1116; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
h1, h2, h3, p, ul { margin: 0; padding: 0; }
ul { list-style: none; }
b { font-weight: 650; }
header { display: grid; grid-template-columns: 1fr auto; align-items: end; gap: 16px; padding-bottom: 9px; border-bottom: 1.5px solid #0e1116; }
h1 { font-size: 25pt; font-weight: 800; letter-spacing: -0.035em; line-height: 1; }
.role { margin-top: 5px; font-size: 11pt; font-weight: 650; }
.role em { font-style: normal; color: #c63a06; }
.contact { font-family: 'Geist Mono', monospace; font-size: 7.6pt; line-height: 1.55; text-align: right; color: #474f5c; }
.summary { margin: 9px 0 10px; color: #262b33; }
.cols { display: grid; grid-template-columns: minmax(0, 1fr) 2.2in; gap: 0.26in; }
h2 { display: flex; align-items: center; gap: 6px; font-size: 8pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; margin: 0 0 5px; }
h2::before { content: ''; width: 7px; height: 7px; border-radius: 1.5px; background: #ff4f12; }
.job { display: grid; grid-template-columns: 1fr auto; align-items: baseline; }
.job h3 { font-size: 10.5pt; font-weight: 700; }
.when { font-family: 'Geist Mono', monospace; font-size: 7.6pt; color: #474f5c; }
.org { color: #474f5c; margin-bottom: 4px; }
.block { margin-top: 5px; }
.block h4 { margin: 0 0 2px; font-size: SIZEpt; font-weight: 700; color: #0e1116; }
.block li, .side li { position: relative; padding-left: 10px; margin-bottom: 2.2px; color: #262b33; }
.block li::before { content: ''; position: absolute; left: 1px; top: 0.55em; width: 4px; height: 4px; border-radius: 1px; background: #626a77; }
.side section { margin-bottom: 9px; }
.side li { padding-left: 0; }
.skills div { margin-bottom: 3.5px; }
.skills dt { font-family: 'Geist Mono', monospace; font-size: 7.2pt; color: #626a77; }
.skills dd { margin: 0; color: #262b33; }
dl { margin: 0; }
main section + section { margin-top: 8px; }
.facts { display: grid; grid-template-columns: 1.15fr 1fr; gap: 2px 0.22in; margin-top: 10px; padding-top: 9px; border-top: 1px solid #dde1e7; }
.facts section { margin: 0 0 6px; }
'''

def html(t, size):
    blocks = ''.join(f'<div class="block"><h4>{h}</h4><ul>' + ''.join(f'<li>{li}</li>' for li in items) + '</ul></div>' for h, items in t['blocks'])
    skills = ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in t['skills'])
    li = lambda xs: '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
    role = t['role'].replace('· ', '· <em>') + '</em>'
    return f'''<!DOCTYPE html><html lang="{'es' if t is C['es'] else 'en'}"><head><meta charset="utf-8">
<title>Kevin Daniel Pelozo Retamar CV</title><style>{CSS.replace('SIZE', str(size))}</style></head><body>
<header><div><h1>Kevin Daniel Pelozo Retamar</h1><p class="role">{role}</p></div>
<p class="contact">{'<br>'.join(t['contact'])}</p></header>
<p class="summary">{t['summary']}</p>
<div class="cols"><main>
<section><h2>{t['h_xp']}</h2>
<div class="job"><h3>{t['job']}</h3><span class="when">{t['when']}</span></div>
<p class="org">{t['org']}</p>{blocks}</section>
<section><h2>{t['h_proj']}</h2><div class="block"><ul>{''.join(f'<li>{p}</li>' for p in t['projects'])}</ul></div></section>
<div class="facts side">
<section><h2>{t['h_edu']}</h2>{li(t['edu'])}</section>
<section><h2>{t['h_cert']}</h2>{li(t['certs'])}</section>
<section><h2>{t['h_lang']}</h2>{li(t['langs'])}</section>
<section><h2>{t['h_cit']}</h2>{li(t['cit'])}</section>
</div>
</main><aside class="side">
<section><h2>{t['h_skills']}</h2><dl class="skills">{skills}</dl></section>
</aside></div></body></html>'''

def pages(pdf):
    out = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    return int(next(l.split()[-1] for l in out.splitlines() if l.startswith('Pages:')))

os.makedirs(OUT_HTML, exist_ok=True)
for lang, t in C.items():
    pdf = os.path.join(ROOT, 'assets', 'files', t['file'])
    for size in (9.4, 9.2, 9.0, 8.8, 8.6, 8.4):
        src = os.path.join(OUT_HTML, f'cv-{lang}.html')
        open(src, 'w', encoding='utf-8').write(html(t, size))
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                        f'--print-to-pdf={pdf}', 'file://' + src], check=True, capture_output=True)
        n = pages(pdf)
        print(f'{lang}: {size}pt -> {n} page(s)')
        if n == 1:
            break
    else:
        sys.exit(f'{lang}: does not fit on one page')
