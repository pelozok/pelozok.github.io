(() => {
  'use strict';

  const i18n = {
    es: {
      skipLink: 'Saltar al contenido',
      navWork: 'Trabajo',
      navProjects: 'Proyectos',
      navExperience: 'Experiencia',
      navContact: 'Contacto',

      heroEyebrow: 'Disponible para nuevos proyectos',
      heroRole: 'Software Engineer &amp; AI Engineer',
      heroTagline:
        '<strong>Software Engineer y AI Engineer</strong> con 5+ años diseñando soluciones escalables — especializado en <strong>desarrollo WordPress</strong>, <strong>aplicaciones potenciadas por IA</strong> e <strong>infraestructura cloud</strong>. Curioso, adaptable y con un fuerte <strong>bias hacia la acción</strong>.',
      metaBasedIn: 'Basado en',
      metaExperience: 'Experiencia',
      metaExperienceValue: '5+ años',
      metaCurrent: 'Actualmente',
      ctaSeeWork: 'Ver mi trabajo',
      ctaContact: 'Contactar',
      ctaDownloadCV: 'Descargar CV',

      aboutTitle: 'Sobre mí',
      aboutP1:
        'Soy <strong>Software Engineer y AI Engineer</strong> con más de 5 años diseñando e implementando soluciones escalables. Trabajo en la intersección de tres mundos: <strong>desarrollo WordPress</strong> (sitios individuales y multisite), <strong>IA aplicada</strong> (desarrollo agéntico, prompt engineering, LLM APIs) e <strong>infraestructura cloud</strong> (AWS, Apache, Docker, CI/CD).',
      aboutP2:
        'En <strong>deLaGuayaba S.A.</strong> construí <strong>Finwaise</strong> — una plataforma financiera para PyMEs — casi en su totalidad con Claude Code y múltiples integraciones MCP. Diseñé el pipeline de procesamiento de documentos (AWS Textract + ChatGPT API) y la orquestación con n8n para automatizar la extracción de datos de facturas.',
      aboutP3:
        'También he liderado el desarrollo de plataformas de colaboración a escala (küikmatch con 3,000+ usuarios y 600+ empresas), migraciones zero-downtime y más de 50 entornos productivos con 99.9% de uptime.',
      aboutP4:
        'Me considero un explorador del ecosistema de IA: experimento constantemente con nuevos modelos, frameworks de agentes y herramientas de automatización para integrarlas a productos reales — no como demo, sino con foco en performance, costo y experiencia de usuario.',
      stackTitle: 'Stack',
      stackAI: 'AI Tools',
      stackAutomation: 'Automation',
      stackProgramming: 'Programming',
      stackCloud: 'Cloud &amp; Infra',

      workTitle: 'Trabajo profesional',
      workSub:
        'Productos construidos en <strong>deLaGuayaba S.A.</strong> — desde IA agéntica hasta sitios institucionales.',
      tagFinwaise: 'Fintech · IA aplicada',
      tagKuikmatch: 'Comunidad · EdTech',
      tagCamarabancos: 'Banca · Asociación gremial',
      tagAbcdust: 'Industrial · CleanTech',
      tagVocesvitales: 'ONG · Impacto social',
      tagGrupotla: 'Logística · Cadena de suministro',
      tagNeutrallog: 'Logística · LATAM',
      tagAlprosa: 'Almacén fiscal · Guatemala',
      tagCommunity: 'Comunidad',
      tagSideProject: 'Side project',

      finwaiseDesc:
        'Plataforma fintech con IA para PyMEs: automatización del procesamiento de documentos y extracción de datos financieros. <strong>Lead developer</strong>.',
      kuikmatchDesc:
        'Plataforma para emprendedores con academia online, directorios geo y marketplace. <strong>3,000+ usuarios y 600+ empresas</strong>.',
      camarabancosDesc:
        'Sitio gremial de la Cámara de Bancos e Instituciones Financieras de Costa Rica, con tema custom, newsletter e integración de datos Bloomberg.',
      abcdustDesc:
        'Sitio multiidioma de soluciones industriales de control de polvo y monitoreo de calidad del aire para minería y construcción.',
      vocesvitalesDesc:
        'Capítulo costarricense de la organización global de liderazgo femenino. Storytelling, eventos, donaciones e integración con WhatsApp.',
      grupotlaDesc:
        'Integrador de cadena de suministro: transporte aéreo, marítimo, terrestre y agencia aduanal en Centroamérica, Perú y Miami.',
      neutrallogDesc:
        'Operador logístico con transporte internacional, agenciamiento aduanal y almacén fiscal en 11 países de Centroamérica.',
      alprosaguateDesc:
        'Almacenadora guatemalteca: custodia de mercancía, bonos de prenda y certificados de depósito con seguridad y trazabilidad.',

      personalTitle: 'Proyectos personales',
      personalSub: 'Trabajo independiente — para mi comunidad y para experimentar.',
      iglesiaDesc:
        'Sitio institucional para una comunidad eclesial. Construido en <strong>Next.js</strong> (App Router) sobre Vercel, con i18n ES/EN. Diseño, desarrollo y mantenimiento desde cero.',
      clearbooksDesc:
        'Herramienta personal para el control mensual y quincenal de mi <strong>presupuesto y salario</strong>. SPA en <strong>React + Vite</strong> con Tailwind, gráficas en Recharts y persistencia en Firebase.',

      experienceTitle: 'Experiencia',
      dlgRole: 'Software Developer &amp; AI Solutions Engineer',
      dlgDate: 'Abril 2019 — Presente',
      dlgDesc:
        'Desarrollo full stack y soluciones de IA para clientes en LATAM. Lidero proyectos de concepto a producción, con foco en desarrollo agéntico y automatización de workflows.',
      dlgPoint1:
        'Construí la plataforma <strong>Finwaise</strong> casi por completo con Claude Code y múltiples integraciones MCP, acelerando el delivery de concepto a producción.',
      dlgPoint2:
        'Diseñé pipeline de procesamiento de documentos con <strong>AWS Textract</strong> (OCR) y <strong>ChatGPT API</strong> para estructuración y validación inteligente de datos.',
      dlgPoint3:
        'Implementé <strong>orquestación con n8n</strong> para automatizar el procesamiento de facturas, conectando múltiples APIs en pipelines productivos.',
      dlgPoint4:
        'Desarrollé <strong>küikmatch</strong>, plataforma escalable con 3,000+ usuarios y 600+ empresas, con LMS, directorios georreferenciados y features sociales.',
      dlgPoint5:
        'Diseñé y optimicé <strong>50+ entornos productivos</strong> con 99.9% uptime y seguridad enterprise-level.',
      dlgPoint6:
        'Lideré migraciones de plataforma asegurando transferencia de datos seamless y zero downtime para clientes enterprise.',
      dlgPoint7:
        'Creé documentación técnica y programas de capacitación que mejoraron la eficiencia del equipo en un <strong>40%</strong>.',

      educationTitle: 'Educación &amp; Idiomas',
      eduDegree: 'Ingeniería en Sistemas',
      eduSchool: 'Universidad Americana (UAM) · Costa Rica',
      eduNote:
        'Aprendizaje continuo a través de cursos, documentación oficial y proyectos open source — con foco actual en desarrollo agéntico y MCP.',
      langTitle: 'Idiomas',
      langSpanish: 'Español',
      langSpanishLevel: 'Nativo',
      langEnglish: 'Inglés',
      langEnglishLevel: 'B2 · Profesional',

      contactTitle: 'Contacto',
      contactSub:
        '¿Tenés un proyecto de IA o automatización en mente? Escribime o <a class="inline-link" href="./assets/files/Kevin-Pelozo-Retamar-CV-2026.pdf" download>descargá mi CV</a>.',

      footerBuilt: 'Hecho a mano con HTML, CSS y JS',
      footerUpdated: 'Actualizado:',
      footerUpdatedDate: '20 de mayo de 2026',
    },

    en: {
      skipLink: 'Skip to content',
      navWork: 'Work',
      navProjects: 'Projects',
      navExperience: 'Experience',
      navContact: 'Contact',

      heroEyebrow: 'Available for new projects',
      heroRole: 'Software Engineer &amp; AI Engineer',
      heroTagline:
        '<strong>Software Engineer and AI Engineer</strong> with 5+ years designing scalable solutions — specialized in <strong>WordPress development</strong>, <strong>AI-powered applications</strong>, and <strong>cloud infrastructure</strong>. Curious, adaptable, and with a strong <strong>bias toward action</strong>.',
      metaBasedIn: 'Based in',
      metaExperience: 'Experience',
      metaExperienceValue: '5+ years',
      metaCurrent: 'Currently',
      ctaSeeWork: 'See my work',
      ctaContact: 'Get in touch',
      ctaDownloadCV: 'Download CV',

      aboutTitle: 'About',
      aboutP1:
        'I’m a <strong>Software Engineer and AI Engineer</strong> with 5+ years designing and implementing scalable solutions. I work at the intersection of three worlds: <strong>WordPress development</strong> (individual and multisite environments), <strong>applied AI</strong> (agentic development, prompt engineering, LLM APIs), and <strong>cloud infrastructure</strong> (AWS, Apache, Docker, CI/CD).',
      aboutP2:
        'At <strong>deLaGuayaba S.A.</strong> I built <strong>Finwaise</strong> — a financial platform for SMEs — almost entirely with Claude Code and extensive MCP integrations. I designed the document processing pipeline (AWS Textract + ChatGPT API) and the n8n orchestration to automate invoice data extraction.',
      aboutP3:
        'I’ve also led collaboration platforms at scale (küikmatch with 3,000+ users and 600+ companies), zero-downtime migrations, and 50+ production environments with 99.9% uptime.',
      aboutP4:
        'I see myself as an explorer of the AI ecosystem: I constantly experiment with new models, agent frameworks, and automation tools — not for demos, but to integrate them into real products with a focus on performance, cost, and user experience.',
      stackTitle: 'Stack',
      stackAI: 'AI Tools',
      stackAutomation: 'Automation',
      stackProgramming: 'Programming',
      stackCloud: 'Cloud &amp; Infra',

      workTitle: 'Professional work',
      workSub:
        'Products built at <strong>deLaGuayaba S.A.</strong> — from agentic AI to institutional sites.',
      tagFinwaise: 'Fintech · Applied AI',
      tagKuikmatch: 'Community · EdTech',
      tagCamarabancos: 'Banking · Industry assoc.',
      tagAbcdust: 'Industrial · CleanTech',
      tagVocesvitales: 'Nonprofit · Social impact',
      tagGrupotla: 'Logistics · Supply chain',
      tagNeutrallog: 'Logistics · LATAM',
      tagAlprosa: 'Bonded warehouse · Guatemala',
      tagCommunity: 'Community',
      tagSideProject: 'Side project',

      finwaiseDesc:
        'AI-powered fintech platform for SMBs: document processing automation and financial data extraction. <strong>Lead developer</strong>.',
      kuikmatchDesc:
        'Entrepreneur community platform with online academy, geo-located directories, and marketplace. <strong>3,000+ users and 600+ companies</strong>.',
      camarabancosDesc:
        'Industry association site for Costa Rica’s Chamber of Banks and Financial Institutions, with a custom theme, newsletter, and Bloomberg data integration.',
      abcdustDesc:
        'Multilingual site for industrial dust control and air quality monitoring solutions for mining and construction.',
      vocesvitalesDesc:
        'Costa Rica chapter of the global women’s leadership organization. Storytelling, events, donations, and WhatsApp integration.',
      grupotlaDesc:
        'Supply chain integrator: air, sea, and land freight plus customs brokerage across Central America, Peru, and Miami.',
      neutrallogDesc:
        'Logistics operator providing international transport, customs clearance, and fiscal warehousing across 11 Central American countries.',
      alprosaguateDesc:
        'Guatemalan bonded warehouse: merchandise custody, pledge bonds, and deposit certificates with security and traceability.',

      personalTitle: 'Personal projects',
      personalSub: 'Independent work — for my community and to experiment.',
      iglesiaDesc:
        'Institutional site for a church community. Built with <strong>Next.js</strong> (App Router) on Vercel, with ES/EN i18n. Design, development, and maintenance from scratch.',
      clearbooksDesc:
        'Personal tool to track my <strong>monthly and bi-weekly budget and salary</strong>. An SPA in <strong>React + Vite</strong> with Tailwind, Recharts for charts, and Firebase for persistence.',

      experienceTitle: 'Experience',
      dlgRole: 'Software Developer &amp; AI Solutions Engineer',
      dlgDate: 'April 2019 — Present',
      dlgDesc:
        'Full stack development and AI solutions for clients across LATAM. I lead projects from concept to production, with a focus on agentic development and workflow automation.',
      dlgPoint1:
        'Built the <strong>Finwaise</strong> platform almost entirely with Claude Code and extensive MCP integrations, accelerating delivery from concept to production.',
      dlgPoint2:
        'Designed a document processing pipeline using <strong>AWS Textract</strong> (OCR) and <strong>ChatGPT API</strong> for intelligent data structuring and validation.',
      dlgPoint3:
        'Implemented <strong>n8n workflow orchestration</strong> to automate invoice processing, connecting multiple APIs into production-ready pipelines.',
      dlgPoint4:
        'Developed <strong>küikmatch</strong>, a scalable platform with 3,000+ users and 600+ companies, including LMS, georeferenced directories, and social features.',
      dlgPoint5:
        'Designed and optimized <strong>50+ production environments</strong> with 99.9% uptime and enterprise-level security.',
      dlgPoint6:
        'Led platform migrations ensuring seamless data transfer and zero downtime for enterprise clients.',
      dlgPoint7:
        'Created technical documentation and training programs that improved team efficiency by <strong>40%</strong>.',

      educationTitle: 'Education &amp; Languages',
      eduDegree: 'Bachelor’s Degree in Systems Engineering',
      eduSchool: 'Universidad Americana (UAM) · Costa Rica',
      eduNote:
        'Continuous learning through courses, official docs, and open source — currently focused on agentic development and MCP.',
      langTitle: 'Languages',
      langSpanish: 'Spanish',
      langSpanishLevel: 'Native',
      langEnglish: 'English',
      langEnglishLevel: 'B2 · Professional',

      contactTitle: 'Contact',
      contactSub:
        'Got an AI or automation project in mind? Drop me a line or <a class="inline-link" href="./assets/files/Kevin-Pelozo-Retamar-CV-2026.pdf" download>download my CV</a>.',

      footerBuilt: 'Hand-built with HTML, CSS and JS',
      footerUpdated: 'Last updated:',
      footerUpdatedDate: 'May 20, 2026',
    },
  };

  const STORAGE_KEY = 'kp-lang';
  const DEFAULT_LANG = 'es';

  const getInitialLang = () => {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved && i18n[saved]) return saved;
    const navLang = (navigator.language || '').toLowerCase();
    if (navLang.startsWith('en')) return 'en';
    return DEFAULT_LANG;
  };

  const applyLang = (lang) => {
    const dict = i18n[lang];
    if (!dict) return;

    document.documentElement.lang = lang;

    document.querySelectorAll('[data-i18n]').forEach((el) => {
      const key = el.getAttribute('data-i18n');
      if (dict[key] != null) {
        el.innerHTML = dict[key];
      }
    });

    document.querySelectorAll('.lang-opt').forEach((el) => {
      el.classList.toggle('active', el.dataset.lang === lang);
    });

    localStorage.setItem(STORAGE_KEY, lang);
  };

  document.addEventListener('DOMContentLoaded', () => {
    const yearEl = document.getElementById('year');
    if (yearEl) yearEl.textContent = String(new Date().getFullYear());

    let lang = getInitialLang();
    applyLang(lang);

    const toggle = document.getElementById('langToggle');
    if (toggle) {
      toggle.addEventListener('click', () => {
        lang = lang === 'es' ? 'en' : 'es';
        applyLang(lang);
      });
    }
  });
})();
