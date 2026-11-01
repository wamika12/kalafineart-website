#!/usr/bin/env python3
"""Generates the four HTML pages from one shared template.
Edit text here, then run:  python3 build.py
(You can also just edit the .html files directly and ignore this script.)"""
import json
from pathlib import Path

SITE = "https://kalafineart.com"
ROOT = Path(__file__).parent
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfYFw3JZnRzN8nLyTJm6h2s0l_YPWYItd2CS3rHMZSqQvEaoA/viewform"
IG = "https://www.instagram.com/kalafineart"
TT = "https://www.tiktok.com/t/ZP8mBsE6P/"
PHONE = "+1 425-892-4523"
EMAIL = "kala.fine.artist@gmail.com"

NAV = [("index.html", "Home"), ("live-wedding-painting.html", "Live Wedding Painting"),
       ("guest-portraits.html", "Guest Portraits"), ("custom-orders.html", "Custom Orders"), ("contact.html", "Contact")]

DIVIDER = ('<svg class="divider" viewBox="0 0 104 8" aria-hidden="true"><path d="M0 4H40M64 4H104" '
           'stroke="#555" stroke-width=".8"/><path d="M40 4c4-4 8-4 12 0c4 4 8 4 12 0M46 4c2-2 4-2 6 0c2 2 4 2 6 0" '
           'fill="none" stroke="#555" stroke-width=".9"/></svg>')

ICONS = {
 "phone": '<svg class="icon" viewBox="0 0 52 52" aria-hidden="true"><circle cx="26" cy="26" r="24.5" fill="#fff" stroke="#111" stroke-width="2"/><path d="M19.5 14.5c1-.6 2.3-.4 3 .6l2.4 3.6c.6.9.5 2.1-.3 2.9l-1.7 1.6c1.3 2.9 3.6 5.3 6.5 6.6l1.7-1.7c.8-.8 2-.9 2.9-.3l3.6 2.4c1 .7 1.3 2 .6 3l-1.5 2.4c-.8 1.3-2.4 1.9-3.9 1.4-8.1-2.6-14.4-8.9-17-17-.5-1.5.1-3.1 1.4-3.9z" fill="#111"/></svg>',
 "instagram": '<svg class="icon" viewBox="0 0 52 52" aria-hidden="true"><defs><linearGradient id="ig" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#feda75"/><stop offset=".35" stop-color="#fa7e1e"/><stop offset=".6" stop-color="#d62976"/><stop offset=".85" stop-color="#962fbf"/><stop offset="1" stop-color="#4f5bd5"/></linearGradient></defs><rect x="2" y="2" width="48" height="48" rx="13" fill="url(#ig)"/><rect x="11" y="11" width="30" height="30" rx="9" fill="none" stroke="#fff" stroke-width="3.2"/><circle cx="26" cy="26" r="7" fill="none" stroke="#fff" stroke-width="3.2"/><circle cx="35" cy="17" r="2" fill="#fff"/></svg>',
 "tiktok": '<svg class="icon" viewBox="0 0 52 52" aria-hidden="true"><circle cx="26" cy="26" r="26" fill="#111"/><path d="M29.5 13h4c.3 3 2.3 5.3 5.5 5.6v4.1c-2 0-3.9-.6-5.5-1.7v8.6c0 4.8-3.9 8.4-8.6 8.4s-8.4-3.7-8.4-8.3 3.8-8.4 8.6-8.3v4.2c-2.4-.4-4.5 1.5-4.4 4 0 2.2 1.8 4 4.1 4 2.4 0 4.6-1.7 4.6-4.4z" fill="#fff"/><path d="M28.5 12h4c.3 3 2.3 5.3 5.5 5.6v4.1" fill="none" stroke="#25f4ee" stroke-width=".8" opacity=".7"/></svg>',
 "email": '<svg class="icon" viewBox="0 0 52 52" aria-hidden="true"><circle cx="26" cy="26" r="26" fill="#111"/><rect x="13" y="17" width="26" height="18" rx="2" fill="none" stroke="#fff" stroke-width="2.2"/><path d="M13.5 18 26 28l12.5-10M13.5 34.5l9.5-8.5M38.5 34.5 29 26" fill="none" stroke="#fff" stroke-width="2.2"/></svg>',
}

FONTS = ("https://fonts.googleapis.com/css2?family=League+Spartan:wght@700&family=Marcellus"
         "&family=Monsieur+La+Doulaise&family=Pinyon+Script&display=swap")


def page(slug, title, description, body, schema=None, og_image="assets/images/og-image.jpg", scripts=""):
    url = f"{SITE}/" if slug == "index.html" else f"{SITE}/{slug}"
    nav = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == slug else ""}>{label}</a></li>'
        for href, label in NAV)
    ld = "".join(f'\n<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
                 for s in (schema or []))
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Kala Fine Art">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE}/{og_image}">
<meta name="theme-color" content="#fbf7ee">
<link rel="icon" type="image/png" href="assets/images/kala-fine-art-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="css/style.css">{ld}
</head>
<body>
<nav class="site-nav" aria-label="Main"><ul>{nav}</ul></nav>
<main>
{body}
</main>
<script>
/* Always open a page at the top (unless linking to a section) */
(function () {{
  try {{
    var nav = performance.getEntriesByType("navigation")[0];
    if (location.hash || (nav && nav.type === "back_forward")) return;
    if ("scrollRestoration" in history) history.scrollRestoration = "manual";
    var moved = false;
    ["wheel", "touchstart", "keydown", "mousedown"].forEach(function (e) {{
      addEventListener(e, function () {{ moved = true; }}, {{ once: true, passive: true }});
    }});
    function toTop() {{
      if (moved) return;
      window.scrollTo(0, 0);
      var first = document.querySelector(".site-nav");
      if (first && first.scrollIntoView) first.scrollIntoView({{ block: "start" }});
    }}
    toTop();
    addEventListener("DOMContentLoaded", toTop);
    addEventListener("load", toTop);
    setTimeout(toTop, 150); setTimeout(toTop, 600);
  }} catch (e) {{}}
}})();
</script>{scripts}
</body>
</html>
"""


# ---------------------------------------------------------------- shared schema
BUSINESS = {
    "@context": "https://schema.org", "@type": "ProfessionalService",
    "@id": f"{SITE}/#business", "name": "Kala Fine Art",
    "description": "Live wedding painting, live guest portraits and custom commissioned paintings by artist Wamika Bansal.",
    "url": f"{SITE}/", "image": f"{SITE}/assets/images/og-image.jpg",
    "logo": f"{SITE}/assets/images/kala-fine-art-logo.png",
    "telephone": PHONE, "email": EMAIL,
    "founder": {"@type": "Person", "name": "Wamika Bansal", "jobTitle": "Live Wedding Painter"},
    "address": {"@type": "PostalAddress", "addressRegion": "WA", "addressCountry": "US"},
    "areaServed": [{"@type": "State", "name": "Washington"}, {"@type": "State", "name": "Oregon"}, "Worldwide"],
    "priceRange": "$$$", "sameAs": [IG, TT],
}

FAQS = [
    ("Do you travel for weddings?",
     "I am based in Washington state but happily travel for weddings and events worldwide. Travel and accommodation fees may apply for destinations outside my local area."),
    ("What space do you need to paint?",
     "I require a minimum 5 ft x 5 ft space with ample lighting and cover to ensure the best painting experience."),
    ("Can you include more than just the couple?",
     "Absolutely. I can incorporate family members, wedding party, or even pets into the painting. Additional fees apply depending on the number of subjects."),
    ("Do you paint other events or from photos?",
     "Yes, I love capturing all types of celebrations beyond weddings. I can also create a painting after the event using professional photos."),
]


def breadcrumb(name, slug):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": f"{SITE}/{slug}"}]}


# ---------------------------------------------------------------- HOME
faq_html = "\n".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q, a in FAQS)
home_body = f"""
<header class="home-hero wrap">
  <img class="logo" src="assets/images/kala-fine-art-logo.png" width="400" height="400" alt="Kala Fine Art logo">
  <h1 class="script title-xl"><span>Live Wedding Painting</span><span>&amp; Guest Portraits</span></h1>
</header>

<section class="about wrap" aria-labelledby="about-title">
  <img class="photo" src="assets/images/wamika-bansal-live-wedding-painter.jpg" width="1800" height="2400"
       alt="Wamika Bansal, live wedding painter, standing in a garden surrounded by doves" fetchpriority="high">
  <div>
    <h2 id="about-title" class="script title-md">About me</h2>
    <p>Hello, I’m Wamika Bansal — a live wedding painter who transforms your most meaningful moments into timeless works of art.</p>
    <p>Based in Washington state and serving couples worldwide, I create romantic, fine art keepsakes painted on-site during your celebration. My paintings beautifully complement your wedding photos and film, becoming heirlooms you’ll treasure for a lifetime.</p>
    <p>What sets my work apart is the intimacy I bring to each piece. I capture not just the big moments but also the subtle details — from the bouquet your grandmother grew to the glow of golden hour. I also hide thoughtful “easter eggs” within the artwork, secret touches only the couple knows to look for, making every painting uniquely personal.</p>
  </div>
</section>

<section aria-label="Portfolio">
  <div class="gallery-row one wrap">
    <figure><img src="assets/images/live-wedding-painting-oregon-city.jpg" width="1314" height="1600" loading="lazy"
         alt="Live wedding ceremony painting of a bride and groom under a tree with lavender drapes in Oregon City, Oregon"></figure>
    <figure><img src="assets/images/live-wedding-painting-mercer-island.jpg" width="1599" height="1213" loading="lazy"
         alt="Live wedding painting of a couple's first kiss on a garden deck on Mercer Island, Washington">
      <figcaption class="caption">First: Oregon City, OR<br>Second: Mercer Island, WA</figcaption></figure>
  </div>
  <div class="gallery-row two wrap">
    <figure><img src="assets/images/mount-rainier-couple-painting.jpg" width="1599" height="1240" loading="lazy"
         alt="Custom painting of a couple and their dog in front of Mount Rainier, Washington">
      <figcaption class="caption center">Mount Rainier, WA</figcaption></figure>
    <figure><img src="assets/images/skagit-valley-tulip-engagement-painting.jpg" width="1250" height="1600" loading="lazy"
         alt="Engagement painting of a couple embracing in the Skagit Valley tulip fields">
      <figcaption class="caption center">Skagit Valley Tulip Farm Engagement</figcaption></figure>
  </div>
</section>

<section class="faq" aria-labelledby="faq-title">
  <h2 id="faq-title" class="script title-md">Frequently Asked Questions</h2>
  <div class="faq-list">
{faq_html}
  </div>
</section>

<section class="home-cta">
  <a class="btn" href="contact.html">Contact me</a>
</section>

<img class="full-bleed-photo" src="assets/images/live-painter-at-easel.jpg" width="1200" height="1600" loading="lazy"
     alt="Wamika Bansal setting up her easel and paints for a live outdoor painting">
"""
faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}

# ---------------------------------------------------------------- LIVE WEDDING PAINTING
WED_STEPS = [
    ("1. Private Consultation", "Our journey begins with a personalized consultation to understand your vision. You'll share your wedding details — date, location, and the moment you'd like immortalized on canvas. Whether it’s your walk down the aisle or your first dance, every detail is tailored to reflect your unique story &amp; style."),
    ("2. Preparation &amp; Composition", "Prior to your celebration, I work closely with your planner and venue to ensure a seamless presence. Composition sketches and palette planning are done in advance to create an elegant visual narrative that complements your wedding’s aesthetic and ambiance."),
    ("3. Live Painting on Your Wedding Day", "On the day of your wedding, I arrive early to set up discreetly within the venue. As your day unfolds, I begin painting live — capturing the magic in real time. Guests are enchanted by the process, adding an exclusive touch of artistry to your celebration."),
    ("4. Studio Enhancements", "Following your wedding, the painting returns to my studio for refinement. I add delicate details, enhancements, and a professional protective finish — ensuring your piece is museum-quality and ready to become a treasured heirloom."),
    ("5. White-Glove Delivery", "Within 4-6 months, your completed painting is beautifully packaged and delivered to your home. Each piece is signed, sealed, and ready to grace your space with the elegance and emotion of your wedding day."),
]
WED_PKGS = [
    ("Silver Package", 3000, "A romantic live painting of just the couple, captured in an intimate moment with a softly detailed background.", "18″×24″ canvas, up to 8 hours of live painting, with studio enhancements included."),
    ("Gold Package", 4000, "A refined scene of the couple set within a detailed backdrop of your venue or ceremony space.", "24″×30″ canvas, live painting on-site, finished with studio detailing."),
    ("Platinum Package", 6000, "An immersive painting featuring the couple and more guests, set in a richly detailed environment.", "30″×40″ canvas, painted live with luxurious studio completion."),
]
steps_html = lambda steps: "\n".join(f'<div class="step"><h3>{t}</h3><p>{d}</p></div>' for t, d in steps)
pkgs_html = f"\n{DIVIDER}\n".join(
    f'<div class="package"><h3 class="pkg-name">{n} ~ ${p:,}</h3><p>{d}<br>{s}</p></div>' for n, p, d, s in WED_PKGS)

wed_body = f"""
<header class="page-title wrap"><h1 class="script title-lg">Live Wedding Painting</h1></header>
<section class="intro-split wrap">
  <img src="assets/images/live-wedding-painting-artist-at-work.jpg" width="1599" height="1066" fetchpriority="high"
       alt="Live wedding painter Wamika Bansal painting a canvas on an easel outdoors among the trees">
  <ul class="bullets">
    <li>Hidden "Easter Eggs": Inspired by the Mehendi tradition of hiding the groom’s name in henna for him to discover, I weave secret symbols and personal touches into your canvas, meaningful details only the two of you know to look for.</li>
    <li>Intimate Details: Preserving subtle elements like heirloom florals and soft golden hour light.</li>
    <li>The Atmosphere: Capturing the raw emotion, warmth, and energy of your wedding day.</li>
  </ul>
</section>
<section class="how bg-white" aria-labelledby="how-title">
  <div class="wrap" style="padding-top:20px">
    <h2 id="how-title" class="script title-sm">How it works</h2>
    <p class="lead">A Bespoke Live Painting Experience for Your Wedding Day from the first brushstroke to the final flourish, your love story is transformed into a timeless heirloom.</p>
{steps_html(WED_STEPS)}
  </div>
</section>
<section class="packages wrap" aria-labelledby="pkg-title">
  <h2 id="pkg-title" class="visually-hidden">Live wedding painting packages and pricing</h2>
{pkgs_html}
</section>
"""
wed_schema = [breadcrumb("Live Wedding Painting", "live-wedding-painting.html"), {
    "@context": "https://schema.org", "@type": "Service", "serviceType": "Live wedding painting",
    "name": "Live Wedding Painting", "provider": {"@id": f"{SITE}/#business"},
    "areaServed": ["Washington", "Oregon", "Worldwide"],
    "offers": [{"@type": "Offer", "name": n, "price": p, "priceCurrency": "USD", "description": f"{d} {s}"}
               for n, p, d, s in WED_PKGS]}]

# ---------------------------------------------------------------- GUEST PORTRAITS
GUEST_STEPS = [
    ("1. Custom Stationery Design", "Before your big day I create custom stationery featuring your names, wedding date, and a frame color matched to your palette, setting the tone for the portraits to come."),
    ("2. On-Site Setup", "I set up at your venue, wherever works best for your flow — cocktail hour, reception entrance, or a dedicated portrait corner."),
    ("3. Live Guest Portraits", "As guests arrive, I photograph them and begin their custom portrait right there at the event."),
    ("4. Same-Day Pickup", "Finished pieces are displayed at my booth throughout the celebration, so guests can pick up their portrait before they leave."),
    ("5. Shipped With Care", "Any portraits not picked up, or finished after the event, are carefully packaged and shipped to you."),
]
TIERS = [
    ("The Petite Soirée", "$2,000", 2000, "Guest Count Up to 100", None),
    ("The Garden Party", "$2,500", 2500, "Guest Count 101–150", None),
    ("The Celebration", "$4,000", 4000, "Guest Count 151–200", "Includes a dedicated assistant"),
    ("The Grand Affair", "$5,500", 5500, "Guest Count 201–300", "Includes a dedicated assistant"),
    ("The Gala", "from $9,500", 9500, "Guest Count 301+", "Includes an assistant or second artist"),
]
tiers_html = f"\n{DIVIDER}\n".join(
    f'<div class="tier"><h3 class="pkg-name small">{n} ~ {p}</h3><p>{c}{"<br>" + x if x else ""}</p></div>'
    for n, p, _, c, x in TIERS)
guest_body = f"""
<header class="page-title wrap"><h1 class="script title-lg">Guest Portraits</h1></header>
<section class="intro-split guest-split wrap">
  <div class="tilted">
    <img class="t1" src="assets/images/guest-portrait-sketch-from-phone.png" width="656" height="840" fetchpriority="high"
         alt="Live guest portrait being sketched from a photo on a phone">
    <img class="t2" src="assets/images/guest-portrait-watercolor-couple.png" width="946" height="1378"
         alt="Finished watercolor guest portrait of two women with pink hearts">
  </div>
  <ul class="bullets justify">
    <li>Tailored Stationery: Drawn on custom, heavy-weight paper designed to match your wedding’s color palette and visual theme.</li>
    <li>Flexible Styles: Options ranging from loose watercolor washes and detailed zoomed-in portraits to full-body fashion sketches and shimmering glitter accents.</li>
    <li>The Ultimate Favor: A live, interactive experience that leaves every guest with a one-of-a-kind frameable keepsake from your celebration.</li>
  </ul>
</section>
<section class="how" aria-labelledby="how-title">
  <div class="wrap">
    <h2 id="how-title" class="script title-sm">How it works</h2>
{steps_html(GUEST_STEPS)}
  </div>
</section>
<section class="tiers wrap" aria-labelledby="tiers-title">
  <h2 id="tiers-title" class="visually-hidden">Live guest portrait packages and pricing</h2>
{tiers_html}
</section>
<section class="styles wrap" aria-labelledby="styles-title">
  <h2 id="styles-title" class="script title-sm">Portrait Styles</h2>
  <div class="style-grid">
    <img src="assets/images/guest-portrait-style-full-body-watercolor.png" width="1092" height="1599" loading="lazy"
         alt="Full-body watercolor fashion sketch guest portrait of a couple in formal wear">
    <img src="assets/images/guest-portrait-style-detailed.jpg" width="1147" height="1599" loading="lazy"
         alt="Detailed zoomed-in guest portrait of a couple with pink hearts">
    <img src="assets/images/guest-portrait-style-faceless.jpg" width="1075" height="1599" loading="lazy"
         alt="Loose watercolor faceless guest portrait of a couple">
  </div>
  <div class="style-grid">
    <video src="assets/videos/guest-portraits-booth.mp4" autoplay muted loop playsinline preload="metadata"
           aria-label="Wamika drawing guest portraits at her Kala Fine Art booth"></video>
    <video src="assets/videos/guest-portraits-live-sketch.mp4" autoplay muted loop playsinline preload="metadata"
           aria-label="Guest portrait being sketched live from a phone photo"></video>
    <video src="assets/videos/guest-portraits-happy-guests.mp4" autoplay muted loop playsinline preload="metadata"
           aria-label="Guests receiving their live portrait at an event"></video>
  </div>
</section>
"""
guest_schema = [breadcrumb("Guest Portraits", "guest-portraits.html"), {
    "@context": "https://schema.org", "@type": "Service", "serviceType": "Live event guest portraits",
    "name": "Live Guest Portraits", "provider": {"@id": f"{SITE}/#business"},
    "areaServed": ["Washington", "Oregon", "Worldwide"],
    "offers": [{"@type": "Offer", "name": n, "price": v, "priceCurrency": "USD",
                "description": c + (f". {x}" if x else "")} for n, _, v, c, x in TIERS]}]

# ---------------------------------------------------------------- CUSTOM ORDERS
custom_body = """
<div class="bg-white">
<header class="page-title wrap"><h1 class="script title-lg">Custom Orders</h1></header>
<section class="custom">
  <div class="custom-split">
    <img src="assets/images/custom-portrait-painting.png" width="982" height="1342" fetchpriority="high"
         alt="Custom hand-painted canvas portrait of a couple on an easel">
    <ul class="custom-list">
      <li><h2>Custom Canvases &amp; Portraits:</h2><p>Transforming beloved pets, family photos, and special milestones into hand-painted canvas heirlooms.</p></li>
      <li><h2>Stationery &amp; Prints:</h2><p>Custom wedding invitations and fun, personalized stickers crafted from your favorite themes or photos.</p></li>
      <li><h2>Personalized Touches:</h2><p>Styled to match your aesthetic, complete with options for loose watercolor, fine detail, or hidden "Easter eggs."</p></li>
    </ul>
  </div>
</section>
</div>
"""
custom_schema = [breadcrumb("Custom Orders", "custom-orders.html"), {
    "@context": "https://schema.org", "@type": "Service", "serviceType": "Custom portrait painting",
    "name": "Custom Paintings, Portraits & Stationery", "provider": {"@id": f"{SITE}/#business"}}]

# ---------------------------------------------------------------- CONTACT
contact_body = f"""
<section class="contact contact-page" id="contact" aria-labelledby="contact-title">
  <h1 id="contact-title" class="script title-lg">Contact Details</h1>
  <div class="contact-grid">
    <div class="contact-left">
      <p class="contact-name">Wamika Bansal</p>
      <a class="btn" href="{FORM}" target="_blank" rel="noopener">Contact us</a>
    </div>
    <ul class="contact-list">
      <li>{ICONS['phone']}<a href="tel:+14258924523" style="text-decoration:none">{PHONE}</a></li>
      <li>{ICONS['instagram']}<a href="{IG}" target="_blank" rel="noopener">kalafineart</a></li>
      <li>{ICONS['tiktok']}<a href="{TT}" target="_blank" rel="noopener">kalafineart</a></li>
      <li>{ICONS['email']}<a href="mailto:{EMAIL}" style="text-decoration:none">{EMAIL}</a></li>
    </ul>
  </div>
</section>

"""
contact_schema = [breadcrumb("Contact", "contact.html"), {
    "@context": "https://schema.org", "@type": "ContactPage", "name": "Contact Kala Fine Art",
    "url": f"{SITE}/contact.html", "about": {"@id": f"{SITE}/#business"}}]

PAGES = {
    "index.html": ("Live Wedding Painter in Washington | Kala Fine Art by Wamika Bansal",
                   "Live wedding painting and live guest portraits by Wamika Bansal, a Washington-based wedding painter serving Seattle, the Pacific Northwest and couples worldwide.",
                   home_body, [BUSINESS, faq_schema]),
    "live-wedding-painting.html": ("Live Wedding Painting Packages & Pricing | Kala Fine Art",
                   "Bespoke live wedding paintings created on-site at your ceremony or reception in Washington, Oregon and worldwide. Silver, Gold and Platinum packages from $3,000.",
                   wed_body, wed_schema),
    "guest-portraits.html": ("Live Guest Portraits for Weddings & Events | Kala Fine Art",
                   "Live wedding guest portraits on custom stationery — a one-of-a-kind favor every guest takes home. Watercolor, detailed and fashion-sketch styles. Packages from $2,000.",
                   guest_body, guest_schema),
    "custom-orders.html": ("Custom Pet, Family & Couple Portrait Paintings | Kala Fine Art",
                   "Commission a custom hand-painted canvas of your pets, family or special milestone, plus custom wedding invitations and personalized stickers by Wamika Bansal.",
                   custom_body, custom_schema),
    "contact.html": ("Contact Wamika Bansal | Kala Fine Art Live Wedding Painting",
                   "Contact Wamika Bansal of Kala Fine Art to book live wedding painting, live guest portraits or a custom painting.",
                   contact_body, contact_schema),
}

if __name__ == "__main__":
    for slug, (title, desc, body, schema, *extra) in PAGES.items():
        (ROOT / slug).write_text(page(slug, title, desc, body, schema, scripts=extra[0] if extra else ""), encoding="utf-8")
    # sitemap + robots
    urls = "".join(f"  <url><loc>{SITE}/{'' if s == 'index.html' else s}</loc></url>\n" for s in PAGES)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print("Built", ", ".join(PAGES))
