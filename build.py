#!/usr/bin/env python3
"""Builds /website/ (EN), /website/es/ and the city pages from one template.

Edit src/ (site.css, site.js, cities.json) or the copy below, then run:  python3 build.py
Re-run after adding photos to /assets so the pages pick them up.
"""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
read = lambda *p: open(os.path.join(ROOT, *p), encoding='utf-8').read()
has = lambda f: os.path.exists(os.path.join(ROOT, 'assets', f))
CSS, JS, CITIES = read('src', 'site.css'), read('src', 'site.js'), json.loads(read('src', 'cities.json'))

APP = 'https://superfast-tires.web.app'
TEL = 'tel:+15612558506'
WA = 'https://wa.me/15612558506?text='
AREA = ['West Palm Beach', 'Lake Worth', 'Greenacres', 'Boynton Beach', 'Delray Beach', 'Boca Raton',
        'Deerfield Beach', 'Parkland', 'Coral Springs', 'Margate', 'Pompano Beach', 'Fort Lauderdale']
CITY_SLUG = {c['name']: c['slug'] for c in CITIES}

T = {
 'en': dict(
  lang='en', title='Mobile Tire Service & Roadside Help 24/7 | Palm Beach & Broward | Super Fast Mobile Tires',
  desc='Flat tire? We come to you in 30–45 min, 24/7 across Palm Beach & Broward. Tire change, flat repair, jump start, lockout, fuel delivery. $89 one-time or $60 for members. Call (561) 255-8506.',
  back='← Back to proposal', switch=('ES', 'Ver en español'),
  nav=[('services', 'Services'), ('pricing', 'Pricing'), ('reviews', 'Reviews'), ('area', 'Service area'), ('faq', 'FAQ')],
  call_top='CALL 24/7', open='Open now · tech available',
  h1="Flat tire? We're there in <em>30–45 minutes.</em>",
  sub='24/7 mobile tire &amp; roadside help across Palm Beach &amp; Broward. <strong>$60 flat for members, same price at 2AM.</strong>',
  cta_call='Call (561) 255-8506', cta_book='Book without signup – $89',
  trust=['5.0 Google', '24/7 dispatch', 'Registered L.L.C.', 'No after-hours fee'], where='Where are you?',
  st_ring='Average arrival time', st=['Most jobs, once we arrive', 'Dispatch, every day', 'Of tips go to your tech'],
  how=('How it works', "Stuck? Three steps and you're rolling.", [
    ('Call or book', 'Call (561) 255-8506 or book online. No account needed for a one-time call.'),
    ('We drive to you', 'Average arrival is 30–45 minutes. Members can follow the tech live on GPS.'),
    ('Back on the road', "Most jobs are done in under 30 minutes, right where you're parked.")]),
  svc=('Services', 'Roadside help, on the spot', '$89 one-time with no signup · $60 flat for members. Same price day or night.'),
  svc_names=['Tire change', 'Flat repair / plug', 'Jump start', 'Lockout', 'Fuel delivery', 'Wheel-lock removal'],
  svc_price='<b>$89</b> one-time · $60 member',
  extras=[('Tow truck', 'Dispatch fee + quote', '$25 dispatch'), ('Mobile mechanic', 'Booking fee + quote', '$20 booking'),
          ('Battery · Used tires · Rims', 'Battery replacement, used tire install, rim damage repair', 'Call for quote')],
  truck=('Our truck', 'This is our truck. Look for it.', 'A black-and-red Ford Transit with flames down the side. Fully equipped, so the repair happens right where you are.'),
  caps=['Side view', 'Rear view', 'On-site tire repair', 'Back on the road'],
  alts=['Super Fast Mobile Tires black and red Ford Transit van, side view', 'Super Fast Mobile Tires van, rear view with phone number', 'Technician repairing a tire on site', 'Technician finishing a roadside tire job'],
  pricing=('Pricing', 'Need help once? Or drive a lot?', 'No signup needed to get help tonight. Membership just makes every call cheaper.'),
  p1=('One-time emergency', 'per call · no signup, no subscription',
      ['Any core service: tire change, flat repair, jump start, lockout, fuel, wheel-lock', 'Open 24/7, same price day or night', 'Avg. arrival 30–45 min'], 'Book without signup – $89'),
  p2=('Save $29 every call', 'Membership', '/month', 'then <b>$60 flat</b> on every core service',
      ['$60 flat, no after-hours surcharge', 'Priority dispatch', 'Live GPS tracking of your tech', 'Cancel anytime, no yearly fee'], 'Become a member – $10/mo'),
  calc=('Is membership worth it for you?', 'How many roadside calls a year?', 'Without membership', 'Member ($120/yr + $60 a call)',
        'You save $X a year as a member.', 'Under 5 calls a year? Pay as you go at $89, no signup.'),
  cmp=(['Member', 'One-time', 'Typical annual plan*'],
       [('No yearly fee', 'Monthly', 'None', 'Yearly'), ('Same price at 2AM', 1, 1, 'Varies'), ('Live GPS tracking', 1, '—', 'Varies'), ('Cancel anytime', 1, 'n/a', 'Varies')],
       '*General comparison with annual roadside memberships; terms differ by provider.', 'Varies'),
  rv=('Reviews', '5.0 stars on Google', '5.0 on Google · 24 reviews', 'Google review', 'Previous review', 'Next review'),
  fleet=('Fleet &amp; rideshare drivers', 'Rideshare, delivery and work trucks: set up a fleet account and get your vehicles back on the road fast.', 'See fleet accounts →'),
  area=('Service area', 'Palm Beach &amp; Broward', 'Based in the Greenacres / Lake Worth area. We cover:'),
  faq_h=('FAQ', 'Quick answers'),
  faq=[('Do I need to sign up to get help?', 'No. Call (561) 255-8506 or book a one-time emergency call for $89. No account, no subscription.'),
       ('Do you charge more at night or on weekends?', 'No. One-time calls are $89 and members pay $60 flat on core services, at 2PM or 2AM.'),
       ('How fast can you get to me?', "Average arrival is 30–45 minutes, and most jobs are finished in under 30 minutes once we're there."),
       ('What does the $10/month membership include?', '$60 flat on tire change, flat repair, jump start, lockout, fuel delivery and wheel-lock removal, no after-hours surcharge, priority dispatch and live GPS tracking. Cancel anytime.'),
       ('Can you tow my car or fix something else?', 'Yes. Tow truck is a $25 dispatch fee plus a quote; mobile mechanic is a $20 booking fee plus a quote. Call for a quote on battery replacement, used tire install and rim repair.'),
       ('Can I message you on WhatsApp?', 'Yes. WhatsApp (561) 255-8506 and send your location. Same number as our 24/7 dispatch line.'),
       ('Where do you work?', 'Palm Beach and Broward counties: ' + ', '.join(AREA[:-1]) + ' and Fort Lauderdale.')],
  final=('Stuck right now?', 'A real dispatcher answers 24/7. Tell us where you are. We come to you.'),
  foot=('We come to you! 24/7 mobile tire &amp; roadside assistance in Palm Beach &amp; Broward counties, FL.', 'Open 24 hours, 7 days',
        'Customers', ['Book a service', 'Member sign in', 'Pricing'], 'Work with us', ['Become a provider', 'Partners', 'Fleet accounts']),
  bar=['Call', 'WhatsApp', 'Book $89'], wa='Hi, I need roadside help. My location is: ',
 ),
 'es': dict(
  lang='es', title='Llantas a domicilio y asistencia en carretera 24/7 | Palm Beach y Broward | Super Fast Mobile Tires',
  desc='¿Llanta ponchada? Llegamos en 30–45 min, 24/7, en Palm Beach y Broward. Cambio de llanta, ponchaduras, paso de corriente, apertura de auto y gasolina. $89 sin registro o $60 para miembros. Llama al (561) 255-8506.',
  back='← Volver a la propuesta', switch=('EN', 'View in English'),
  nav=[('services', 'Servicios'), ('pricing', 'Precios'), ('reviews', 'Reseñas'), ('area', 'Zona'), ('faq', 'Preguntas')],
  call_top='LLAMA 24/7', open='Abierto ahora · técnico disponible',
  h1='¿Llanta ponchada? Llegamos en <em>30–45 minutos.</em>',
  sub='Llantas y asistencia en carretera 24/7 en Palm Beach y Broward. <strong>$60 fijos para miembros, el mismo precio a las 2 AM.</strong>',
  cta_call='Llama al (561) 255-8506', cta_book='Reserva sin registro – $89',
  trust=['5.0 en Google', 'Despacho 24/7', 'L.L.C. registrada', 'Sin recargo nocturno'], where='¿Dónde estás?',
  st_ring='Tiempo promedio de llegada', st=['La mayoría de los trabajos, ya en sitio', 'Despacho, todos los días', 'De las propinas van a tu técnico'],
  how=('Cómo funciona', '¿Varado? Tres pasos y vuelves a rodar.', [
    ('Llama o reserva', 'Llama al (561) 255-8506 o reserva en línea. Para un servicio único no necesitas cuenta.'),
    ('Vamos hacia ti', 'Llegamos en 30–45 minutos en promedio. Los miembros siguen al técnico en vivo por GPS.'),
    ('De vuelta al camino', 'La mayoría de los trabajos toma menos de 30 minutos, ahí donde estás.')]),
  svc=('Servicios', 'Ayuda en carretera, donde estés', '$89 por servicio sin registro · $60 fijos para miembros. Mismo precio de día o de noche.'),
  svc_names=['Cambio de llanta', 'Reparación de ponchadura', 'Paso de corriente', 'Apertura de auto', 'Entrega de gasolina', 'Quitar birlo de seguridad'],
  svc_price='<b>$89</b> sin registro · $60 miembro',
  extras=[('Grúa', 'Cargo de despacho + cotización', '$25 despacho'), ('Mecánico a domicilio', 'Cargo de reserva + cotización', '$20 reserva'),
          ('Batería · Llantas usadas · Rines', 'Cambio de batería, instalación de llanta usada y reparación de rines', 'Llama para cotizar')],
  truck=('Nuestra camioneta', 'Esta es nuestra camioneta. Búscala.', 'Una Ford Transit negra y roja con llamas a los lados. Totalmente equipada: la reparación se hace ahí donde estás.'),
  caps=['Vista lateral', 'Vista trasera', 'Reparación en sitio', 'De vuelta al camino'],
  alts=['Camioneta Ford Transit negra y roja de Super Fast Mobile Tires, vista lateral', 'Camioneta de Super Fast Mobile Tires, vista trasera con el teléfono', 'Técnico reparando una llanta en sitio', 'Técnico terminando un servicio en carretera'],
  pricing=('Precios', '¿Ayuda una vez? ¿O manejas mucho?', 'No necesitas registrarte para recibir ayuda hoy. La membresía solo hace más barato cada servicio.'),
  p1=('Emergencia única', 'por servicio · sin registro ni suscripción',
      ['Cualquier servicio básico: llanta, ponchadura, corriente, apertura, gasolina o birlo', 'Abierto 24/7, mismo precio de día o de noche', 'Llegada promedio de 30–45 min'], 'Reserva sin registro – $89'),
  p2=('Ahorra $29 por servicio', 'Membresía', '/mes', 'luego <b>$60 fijos</b> en cada servicio básico',
      ['$60 fijos, sin recargo nocturno', 'Despacho prioritario', 'Rastreo GPS en vivo de tu técnico', 'Cancela cuando quieras, sin cuota anual'], 'Hazte miembro – $10/mes'),
  calc=('¿Te conviene la membresía?', '¿Cuántos servicios de asistencia al año?', 'Sin membresía', 'Miembro ($120/año + $60 por servicio)',
        'Como miembro ahorras $X al año.', '¿Menos de 5 servicios al año? Paga solo cuando lo necesites: $89, sin registro.'),
  cmp=(['Miembro', 'Único', 'Plan anual típico*'],
       [('Sin cuota anual', 'Mensual', 'Ninguna', 'Anual'), ('Mismo precio a las 2 AM', 1, 1, 'Varía'), ('Rastreo GPS en vivo', 1, '—', 'Varía'), ('Cancela cuando quieras', 1, 'n/a', 'Varía')],
       '*Comparación general con membresías anuales de asistencia; las condiciones varían según el proveedor.', 'Varía'),
  rv=('Reseñas', '5.0 estrellas en Google', '5.0 en Google · 24 reseñas', 'Reseña de Google (en inglés)', 'Reseña anterior', 'Reseña siguiente'),
  fleet=('Flotillas y conductores de apps', 'Rideshare, reparto y camionetas de trabajo: abre una cuenta de flotilla y vuelve a poner tus vehículos en marcha rápido.', 'Ver cuentas de flotilla →'),
  area=('Zona de servicio', 'Palm Beach y Broward', 'Desde la zona de Greenacres / Lake Worth cubrimos:'),
  faq_h=('Preguntas', 'Respuestas rápidas'),
  faq=[('¿Tengo que registrarme para recibir ayuda?', 'No. Llama al (561) 255-8506 o reserva un servicio de emergencia por $89. Sin cuenta y sin suscripción.'),
       ('¿Cobran más de noche o los fines de semana?', 'No. El servicio único cuesta $89 y los miembros pagan $60 fijos en servicios básicos, a las 2 PM o a las 2 AM.'),
       ('¿Qué tan rápido llegan?', 'Llegamos en 30–45 minutos en promedio, y la mayoría de los trabajos se termina en menos de 30 minutos ya en sitio.'),
       ('¿Qué incluye la membresía de $10 al mes?', '$60 fijos en cambio de llanta, ponchaduras, paso de corriente, apertura de auto, gasolina y birlo de seguridad, sin recargo nocturno, con despacho prioritario y rastreo GPS en vivo. Cancela cuando quieras.'),
       ('¿Pueden remolcar mi auto o arreglar otra cosa?', 'Sí. La grúa tiene un cargo de despacho de $25 más cotización; el mecánico a domicilio, $20 de reserva más cotización. Llama para cotizar batería, llanta usada o reparación de rines.'),
       ('¿Puedo escribirles por WhatsApp?', 'Sí. Escríbenos al (561) 255-8506 y mándanos tu ubicación. Es el mismo número del despacho 24/7.'),
       ('¿En qué zonas trabajan?', 'En los condados de Palm Beach y Broward: ' + ', '.join(AREA[:-1]) + ' y Fort Lauderdale.')],
  final=('¿Varado ahora mismo?', 'Un despachador real contesta 24/7. Dinos dónde estás y vamos hacia ti.'),
  foot=('We come to you! Llantas y asistencia en carretera 24/7 en los condados de Palm Beach y Broward, FL.', 'Abierto 24 horas, 7 días',
        'Clientes', ['Reservar un servicio', 'Acceso para miembros', 'Precios'], 'Trabaja con nosotros', ['Hazte proveedor', 'Socios', 'Cuentas de flotilla']),
  bar=['Llamar', 'WhatsApp', 'Reservar $89'], wa='Hola, necesito asistencia en carretera. Mi ubicación es: ',
 ),
}

# Lucide icons (ISC license), inlined as a sprite
ICONS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></symbol>
<symbol id="i-msg" viewBox="0 0 24 24"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></symbol>
<symbol id="i-cal" viewBox="0 0 24 24"><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M9 16l2 2 4-4"/></symbol>
<symbol id="i-star" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></symbol>
<symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/><path d="m9 12 2 2 4-4"/></symbol>
<symbol id="i-moon" viewBox="0 0 24 24"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></symbol>
<symbol id="i-wrench" viewBox="0 0 24 24"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></symbol>
<symbol id="i-tire" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><path d="M12 2v6M12 16v6M2 12h6M16 12h6"/></symbol>
<symbol id="i-lock" viewBox="0 0 24 24"><rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></symbol>
<symbol id="i-key" viewBox="0 0 24 24"><circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6M15.5 7.5l3 3L22 7l-3-3"/></symbol>
<symbol id="i-fuel" viewBox="0 0 24 24"><path d="M3 22h12M4 9h10M14 22V4a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v18"/><path d="M14 13h2a2 2 0 0 1 2 2v2a2 2 0 0 0 4 0V9.83a2 2 0 0 0-.59-1.42L18 5"/></symbol>
<symbol id="i-zap" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></symbol>
<symbol id="i-battery" viewBox="0 0 24 24"><rect width="16" height="10" x="2" y="7" rx="2"/><path d="M22 11v2M6 11v2M10 11v2"/></symbol>
<symbol id="i-truck" viewBox="0 0 24 24"><path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2M15 18H9M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.62l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5"/></symbol>
<symbol id="i-down" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></symbol>
<symbol id="i-left" viewBox="0 0 24 24"><path d="m15 18-6-6 6-6"/></symbol>
<symbol id="i-right" viewBox="0 0 24 24"><path d="m9 18 6-6-6-6"/></symbol>
</svg>'''

ic = lambda name, cls='ic': f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'
SVC_ICONS = ['tire', 'wrench', 'zap', 'lock', 'fuel', 'key']


def photo(R, name, alt, w, h, cap, cls=''):
    """Figure with a tread-pattern fallback. Only references files that exist, so a missing photo never 404s."""
    base = name.rsplit('.', 1)[0]
    img = ''
    if has(name) or has(base + '.webp'):
        webp = f'<source srcset="{R}assets/{base}.webp" type="image/webp">' if has(base + '.webp') else ''
        src = name if has(name) else base + '.webp'
        img = (f'<picture>{webp}<img src="{R}assets/{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async" '
               f'onerror="this.parentNode.remove()"></picture>')
    return f'<figure class="ph tread {cls}">{img}<figcaption>{cap}</figcaption></figure>'


def page(L, R, W, city=None):
    """L: language, R: path to repo root, W: path to /website/."""
    t = T[L]
    title, desc, h1, sub = t['title'], t['desc'], t['h1'], t['sub']
    if city:
        n = city['name']
        title = f'Mobile Tire Service in {n}, FL | 24/7 Roadside Help | Super Fast Mobile Tires'
        desc = f'Mobile tire service in {n}, FL. We come to you in 30–45 min, 24/7. Tire change, flat repair, jump start, lockout, fuel. $89 one-time or $60 for members. Call (561) 255-8506.'
        h1 = f'Mobile Tire Service in {n}, FL. <em>30–45 min, 24/7</em>'
        sub = city['intro'] + ' <strong>$89 one-time, or $60 flat for members.</strong>'
    switch_href = (W + 'es/') if L == 'en' else W
    alt_links = (f'<link rel="alternate" hreflang="en" href="{W}"><link rel="alternate" hreflang="es" href="{W}es/">'
                 f'<link rel="alternate" hreflang="x-default" href="{W}">') if not city else ''

    ld = {"@context": "https://schema.org", "@type": "AutoRepair", "name": "Super Fast Mobile Tires L.L.C.", "slogan": "We come to you!",
          "description": "24/7 mobile tire and roadside assistance across Palm Beach and Broward counties.",
          "telephone": "+1-561-255-8506", "priceRange": "$60–$89",
          "address": {"@type": "PostalAddress", "addressLocality": "Greenacres", "addressRegion": "FL", "addressCountry": "US"},
          "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
             "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}],
          "areaServed": [{"@type": "AdministrativeArea", "name": "Palm Beach County, FL"}, {"@type": "AdministrativeArea", "name": "Broward County, FL"}]
                        + [{"@type": "City", "name": c + ", FL"} for c in AREA],
          "makesOffer": [{"@type": "Offer", "name": "One-time emergency call (no signup)", "price": "89", "priceCurrency": "USD"},
                         {"@type": "Offer", "name": "Membership: $60 flat on core services", "price": "10", "priceCurrency": "USD"}]}
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t['faq']]}

    hero_img = ''
    if has('van-hero-640.webp'):
        ss = ', '.join(f'{R}assets/van-hero-{w}.webp {w}w' for w in (640, 1280, 1600) if has(f'van-hero-{w}.webp'))
        fb = 'van-hero.jpg' if has('van-hero.jpg') else 'van-hero-1600.webp'
        hero_img = (f'<div class="hero-media"><picture><source type="image/webp" srcset="{ss}" sizes="100vw">'
                    f'<img src="{R}assets/{fb}" alt="" width="1600" height="800" fetchpriority="high" decoding="async" onerror="this.parentNode.remove()"></picture></div>')
        preload = f'<link rel="preload" as="image" type="image/webp" imagesrcset="{ss}" imagesizes="100vw" fetchpriority="high">'
    else:
        preload = ''

    logo = (f'<picture><source srcset="{R}assets/logo.webp" type="image/webp"><img src="{R}assets/logo.png" alt="Super Fast Mobile Tires" width="56" height="40" onerror="this.parentNode.remove()"></picture>'
            if has('logo.png') else '')
    wa = WA + t['wa'].replace(' ', '%20').replace(':', '%3A').replace(',', '%2C')
    city_link = lambda c: f'{W}{CITY_SLUG[c]}/' if c in CITY_SLUG else None

    chips = ''.join(f'<a href="#area">{ic("pin")}{c}</a>' for c in AREA)
    trust_ic = [ic('star', 'ic star'), ic('clock'), ic('shield'), ic('moon')]
    trust = ''.join(f'<li>{i}{s}</li>' for i, s in zip(trust_ic, t['trust']))
    steps = ''.join(f'<div class="step"><span class="n">{k}</span><div><h3>{a}</h3><p>{b}</p></div></div>' for k, (a, b) in enumerate(t['how'][2], 1))
    svcs = ''.join(f'<div class="svc">{ic(i)}<h3>{n}</h3><p class="price">{t["svc_price"]}</p></div>' for i, n in zip(SVC_ICONS, t['svc_names']))
    ex = t['extras']
    extras = (f'<div class="row">{ic("truck")}<div><h3>{ex[0][0]}</h3><p>{ex[0][1]}</p></div><span class="tag">{ex[0][2]}</span></div>'
              f'<div class="row">{ic("wrench")}<div><h3>{ex[1][0]}</h3><p>{ex[1][1]}</p></div><span class="tag">{ex[1][2]}</span></div>'
              f'<div class="row">{ic("battery")}<div><h3>{ex[2][0]}</h3><p>{ex[2][1]}</p></div><a class="tag" href="{TEL}">{ex[2][2]}</a></div>')
    caps, alts = t['caps'], t['alts']
    truck = (photo(R, 'van-side.jpg', alts[0], 800, 400, caps[0], 'big') + photo(R, 'van-rear.jpg', alts[1], 800, 533, caps[1])
             + photo(R, 'tech-1.jpg', alts[2], 800, 533, caps[2]) + photo(R, 'tech-2.jpg', alts[3], 800, 533, caps[3]))
    li = lambda xs: ''.join(f'<li>{ic("check")}{x}</li>' for x in xs)
    p1, p2, c = t['p1'], t['p2'], t['calc']
    n0 = 5  # calculator default; static result below is what no-JS visitors see
    cell = lambda v: f'<td class="y">{ic("check")}<span class="sr">✓</span></td>' if v == 1 else (
        f'<td class="x">{v}</td>' if v in ('—', 'n/a', t['cmp'][3], 'Yearly', 'Anual') else f'<td class="y">{v}</td>')
    rows = ''.join(f'<tr><th scope="row">{r[0]}</th>{"".join(cell(v) for v in r[1:])}</tr>' for r in t['cmp'][1])
    star5 = ic('star') * 5
    cities = ''.join(f'<li><a href="{city_link(n)}">{ic("pin")}{n}</a></li>' if city_link(n) and not (city and n == city['name'])
                     else f'<li><span>{ic("pin")}{n}</span></li>' for n in AREA)
    faqs = ''.join(f'<details><summary>{q}{ic("down")}</summary><p>{a}</p></details>' for q, a in t['faq'])
    f = t['foot']
    nav = ''.join(f'<a href="#{h}">{s}</a>' for h, s in t['nav'])

    return f'''<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#0B0B0C">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="{R}assets/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="{R}assets/icon-192.png">
{alt_links}
<link rel="preload" href="{R}assets/fonts/barlow-condensed-800.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{R}assets/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
{preload}
<!-- TRACKING: GA4 / Google Ads / Meta Pixel go here at launch -->
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
<style>{CSS.replace('ROOT', R)}</style>
</head>
<body>
{ICONS}
<a class="preview-only" href="{R}">{t['back']}</a>
<header class="top">
  <div class="wrap">
    <a href="{W if L == 'en' else W + 'es/'}" class="logo" aria-label="Super Fast Mobile Tires">
      <span class="logo-badge">{logo}</span>
      <span class="logo-txt" aria-hidden="true"><b>Super <span>Fast</span></b><small>Mobile Tires · 24/7</small></span>
    </a>
    <nav aria-label="Main">{nav}</nav>
    <div class="top-r">
      <a class="lang" href="{switch_href}" hreflang="{t['switch'][0].lower()}">{t['switch'][0]}<span class="sr"> · {t['switch'][1]}</span></a>
      <a class="call-top" href="{TEL}">{ic('phone')}{t['call_top']}<span class="num">&nbsp;(561) 255-8506</span></a>
    </div>
  </div>
</header>

<main>
  <section class="hero tread">
    {hero_img}
    <div class="wrap"><div class="inner">
      <span class="open-pill"><span class="dot" aria-hidden="true"></span>{t['open']}</span>
      <h1>{h1}</h1>
      <p class="sub">{sub}</p>
      <div class="cta-row">
        <a class="btn btn-red" href="{TEL}">{ic('phone')}{t['cta_call']}</a>
        <a class="btn btn-ghost" href="{APP}/">{ic('cal')}{t['cta_book']}</a>
      </div>
      <ul class="trust">{trust}</ul>
      <div class="where"><p>{t['where']}</p><nav class="chips" aria-label="{t['where']}">{chips}</nav></div>
    </div></div>
  </section>

  <div class="stats" data-anim>
    <div class="wrap grid">
      <div class="ring">
        <svg viewBox="0 0 100 100" aria-hidden="true"><circle class="bg" cx="50" cy="50" r="45"/><circle class="fg" cx="50" cy="50" r="45"/></svg>
        <div><b>30–45 min</b><span>{t['st_ring']}</span></div>
      </div>
      <div class="stat"><b>&lt;<span data-count="30">30</span> min</b><span>{t['st'][0]}</span></div>
      <div class="stat"><b><span data-count="24">24</span>/7</b><span>{t['st'][1]}</span></div>
      <div class="stat"><b><span data-count="100">100</span>%</b><span>{t['st'][2]}</span></div>
    </div>
  </div>

  <section id="how">
    <div class="wrap">
      <span class="eyebrow">{t['how'][0]}</span>
      <h2>{t['how'][1]}</h2>
      <div class="steps">{steps}</div>
    </div>
  </section>

  <section id="services" style="padding-top:0">
    <div class="wrap">
      <span class="eyebrow">{t['svc'][0]}</span>
      <h2>{t['svc'][1]}</h2>
      <p class="lead">{t['svc'][2]}</p>
      <div class="svc-grid">{svcs}</div>
      <div class="extra">{extras}</div>
    </div>
  </section>

  <section class="dark truck">
    <div class="wrap">
      <span class="eyebrow">{t['truck'][0]}</span>
      <h2>{t['truck'][1]}</h2>
      <p class="lead">{t['truck'][2]}</p>
      <div class="grid">{truck}</div>
    </div>
  </section>

  <section id="pricing" class="dark" style="padding-top:0">
    <div class="wrap">
      <span class="eyebrow">{t['pricing'][0]}</span>
      <h2>{t['pricing'][1]}</h2>
      <p class="lead">{t['pricing'][2]}</p>
      <div class="plans">
        <div class="plan">
          <h3>{p1[0]}</h3>
          <div class="amt">$89</div>
          <p class="per">{p1[1]}</p>
          <ul>{li(p1[2])}</ul>
          <a class="btn btn-ghost" href="{APP}/">{p1[3]}</a>
        </div>
        <div class="plan hot">
          <span class="badge">{p2[0]}</span>
          <h3>{p2[1]}</h3>
          <div class="amt">$10<small>{p2[2]}</small></div>
          <p class="per">{p2[3]}</p>
          <ul>{li(p2[4])}</ul>
          <a class="btn btn-red" href="{APP}/">{p2[5]}</a>
        </div>
      </div>

      <div class="calc">
        <h3>{c[0]}</h3>
        <label for="calls">{c[1]} <output id="c-n" for="calls">{n0}</output></label>
        <input type="range" id="calls" min="1" max="6" value="{n0}">
        <div class="res">
          <div><span>{c[2]}</span><b id="c-no">${89 * n0}</b></div>
          <div><span>{c[3]}</span><b id="c-me">${120 + 60 * n0}</b></div>
        </div>
        <p class="verdict save" id="c-v" aria-live="polite" data-save="{c[4]}" data-nosave="{c[5]}">{c[4].replace('X', str(29 * n0 - 120))}</p>
      </div>

      <table class="compare">
        <thead><tr><td></td><th scope="col" class="us">{t['cmp'][0][0]}</th><th scope="col">{t['cmp'][0][1]}</th><th scope="col">{t['cmp'][0][2]}</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
      <p class="compare-note">{t['cmp'][2]}</p>
    </div>
  </section>

  <section id="reviews">
    <div class="wrap">
      <div class="rv-head">
        <div><span class="eyebrow">{t['rv'][0]}</span><h2>{t['rv'][1]}</h2></div>
        <!-- TODO: replace href with the Google Business Profile link -->
        <a class="g-badge" href="#reviews">{ic('star')}{t['rv'][2]}</a>
      </div>
      <div class="carousel">
        <figure class="review">
          <div class="stars" role="img" aria-label="5/5">{star5}</div>
          <blockquote>"He was here super fast, got the tire repaired and back on all within an hour."</blockquote>
          <figcaption><cite>{t['rv'][3]}</cite></figcaption>
        </figure>
        <!-- REVIEW 2: paste real Google review (copy the <figure class="review"> block above) -->
        <!-- REVIEW 3: paste real Google review -->
        <!-- REVIEW 4: paste real Google review -->
      </div>
      <div class="car-nav">
        <button type="button" data-dir="-1" aria-label="{t['rv'][4]}">{ic('left')}</button>
        <button type="button" data-dir="1" aria-label="{t['rv'][5]}">{ic('right')}</button>
      </div>
    </div>
  </section>

  <div class="fleet">
    <div class="wrap">
      <div><h2>{t['fleet'][0]}</h2><p>{t['fleet'][1]}</p></div>
      <a class="btn btn-dark" href="{APP}/fleet">{t['fleet'][2]}</a>
    </div>
  </div>

  <section id="area">
    <div class="wrap">
      <span class="eyebrow">{t['area'][0]}</span>
      <h2>{t['area'][1]}</h2>
      <p class="lead">{t['area'][2]}</p>
      <ul class="cities">{cities}</ul>
    </div>
  </section>

  <section id="faq" style="padding-top:0">
    <div class="wrap">
      <span class="eyebrow">{t['faq_h'][0]}</span>
      <h2>{t['faq_h'][1]}</h2>
      <div class="faq">{faqs}</div>
    </div>
  </section>

  <section class="final">
    <div class="wrap">
      <h2>{t['final'][0]}</h2>
      <p>{t['final'][1]}</p>
      <a class="btn btn-dark" href="{TEL}">{ic('phone')}{t['cta_call']}</a>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <div class="grid">
      <div>
        <h2>Super Fast Mobile Tires L.L.C.</h2>
        <p>{f[0]}</p>
        <p style="margin-top:10px"><a href="{TEL}"><b style="color:#fff">(561) 255-8506</b></a> · {f[1]}</p>
      </div>
      <div>
        <h2>{f[2]}</h2>
        <ul><li><a href="{APP}/">{f[3][0]}</a></li><li><a href="{APP}/">{f[3][1]}</a></li><li><a href="#pricing">{f[3][2]}</a></li></ul>
      </div>
      <div>
        <h2>{f[4]}</h2>
        <ul><li><a href="{APP}/provider">{f[5][0]}</a></li><li><a href="{APP}/partner">{f[5][1]}</a></li><li><a href="{APP}/fleet">{f[5][2]}</a></li></ul>
      </div>
    </div>
    <p class="legal">© 2026 Super Fast Mobile Tires L.L.C. · Greenacres / Lake Worth, FL</p>
  </div>
</footer>

<nav class="bar" aria-label="Quick actions">
  <a class="b-call" href="{TEL}">{ic('phone')}{t['bar'][0]}</a>
  <a class="b-wa" href="{wa}" target="_blank" rel="noopener">{ic('msg')}{t['bar'][1]}</a>
  <a class="b-book" href="{APP}/">{ic('cal')}{t['bar'][2]}</a>
</nav>
<script>{JS}</script>
</body>
</html>
'''


def write(rel, html):
    p = os.path.join(ROOT, 'website', rel, 'index.html')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(html)
    print('wrote', os.path.relpath(p, ROOT))


write('', page('en', '../', './'))
write('es', page('es', '../../', '../'))
for c in CITIES:
    write(c['slug'], page('en', '../../', '../', c))
