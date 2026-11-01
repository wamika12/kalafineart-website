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
# Free key from web3forms.com: inquiries are emailed to the address it was created with
WEB3FORMS_KEY = "e812bc80-c707-40c6-a6ef-0ff54de255f9"

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


AREAS = ["Seattle", "Bellevue", "Kirkland", "Redmond", "Mercer Island", "Woodinville", "Tacoma", "Everett", "Snohomish", "Gig Harbor", "Bainbridge Island", "Leavenworth", "San Juan Islands", "Skagit Valley", "Mount Rainier", "Lake Chelan", "Washington"]

# ---------------------------------------------------------------- shared schema
BUSINESS = {
    "@context": "https://schema.org", "@type": "ProfessionalService",
    "@id": f"{SITE}/#business", "name": "Kala Fine Art",
    "description": "Live wedding painting, live guest portraits and custom commissioned paintings by artist Wamika Bansal.",
    "url": f"{SITE}/", "image": f"{SITE}/assets/images/og-image.jpg",
    "logo": f"{SITE}/assets/images/kala-fine-art-logo.png",
    "telephone": PHONE, "email": EMAIL,
    "founder": {"@type": "Person", "name": "Wamika Bansal", "jobTitle": "Live Wedding Painter"},
    "address": {"@type": "PostalAddress", "addressLocality": "Seattle", "addressRegion": "WA", "addressCountry": "US"},
    "areaServed": AREAS,
    "priceRange": "$$$", "sameAs": [IG, TT],
}

FAQS = [
    ("Do you travel for weddings?",
     "Yes! I’m based in the Seattle area and paint weddings all over Washington. Travel is free within 50 miles of Seattle. I also travel worldwide; travel fees may apply depending on the distance."),
    ("What space do you need to paint?",
     "I require a minimum 5 ft x 5 ft space with ample lighting and cover to ensure the best painting experience."),
    ("Can you include more than just the couple?",
     "Absolutely. I can incorporate family members, wedding party, or even pets into the painting. Additional fees apply depending on the number of subjects."),
    ("Can I book live painting and guest portraits for the same event?",
     "Yes! For multi-day celebrations, such as a sangeet or mehendi followed by the wedding, I can paint both myself on different days. For a single event, I bring a second artist so your live painting and guest portraits happen side by side."),
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
  <img class="photo" src="assets/images/wamika-bansal-live-wedding-painter.webp" width="1050" height="1400"
       alt="Wamika Bansal, live wedding painter, standing in a garden surrounded by doves" fetchpriority="high">
  <div>
    <h2 id="about-title" class="script title-md">About me</h2>
    <p>Hello, I’m Wamika Bansal — a live wedding painter who transforms your most meaningful moments into timeless works of art.</p>
    <p>Based in the Seattle area and serving couples across Washington and worldwide, I create romantic, fine art keepsakes painted on-site during your celebration. My paintings beautifully complement your wedding photos and film, becoming heirlooms you’ll treasure for a lifetime.</p>
    <p>What sets my work apart is the intimacy I bring to each piece. I capture not just the big moments but also the subtle details — from the bouquet your grandmother grew to the glow of golden hour. I also hide thoughtful “easter eggs” within the artwork, secret touches only the couple knows to look for, making every painting uniquely personal.</p>
  </div>
</section>

<section aria-label="Portfolio">
  <div class="gallery-row one wrap">
    <figure><img src="assets/images/live-wedding-painting-oregon-city.webp" width="1150" height="1400" loading="lazy"
         alt="Live wedding ceremony painting of a bride and groom under a tree with lavender drapes in Oregon City, Oregon"></figure>
    <figure><img src="assets/images/live-wedding-painting-mercer-island.webp" width="1400" height="1062" loading="lazy"
         alt="Live wedding painting of a couple's first kiss on a garden deck on Mercer Island, Washington">
      <figcaption class="caption">First: Oregon City, OR<br>Second: Mercer Island, WA</figcaption></figure>
  </div>
  <div class="gallery-row two wrap">
    <figure><img src="assets/images/mount-rainier-couple-painting.webp" width="1400" height="1086" loading="lazy"
         alt="Custom painting of a couple and their dog in front of Mount Rainier, Washington">
      <figcaption class="caption center">Mount Rainier, WA</figcaption></figure>
    <figure><img src="assets/images/skagit-valley-tulip-engagement-painting.webp" width="1094" height="1400" loading="lazy"
         alt="Engagement painting of a couple embracing in the Skagit Valley tulip fields">
      <figcaption class="caption center">Skagit Valley Tulip Farm Engagement</figcaption></figure>
  </div>
</section>

<section class="where wrap" aria-labelledby="where-title">
  <h2 id="where-title" class="script title-md">Where I Paint</h2>
  <p class="where-intro">I’m a Seattle-area live wedding painter, and I bring my easel to venues all over Washington. Here are a few favorite places I paint:</p>
  <div class="where-grid">
    <div><h3>Seattle &amp; the Eastside</h3><p>Seattle · Bellevue · Kirkland · Redmond · Mercer Island · Woodinville · and nearby</p></div>
    <div><h3>Greater Puget Sound</h3><p>Tacoma · Everett · Snohomish · Gig Harbor · Bainbridge Island · and nearby</p></div>
    <div><h3>Washington Getaways</h3><p>Leavenworth · San Juan Islands · Skagit Valley · Mount Rainier · Lake Chelan · and more</p></div>
  </div>
  <p class="where-note"><strong>Travel is free within 50 miles of Seattle. Planning a wedding farther away? I travel worldwide. Travel fees may apply depending on the distance.</strong></p>
</section>

<section class="faq" aria-labelledby="faq-title">
  <h2 id="faq-title" class="script title-md">Frequently Asked Questions</h2>
  <div class="faq-list">
{faq_html}
  </div>
</section>

<section class="home-cta">
  <a class="btn" href="contact.html">Book a free consultation</a>
</section>

<img class="full-bleed-photo" src="assets/images/live-painter-at-easel.webp" width="1050" height="1400" loading="lazy"
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
    ("Silver Collection", 2500, "Starting at $2,500", "A romantic live painting of just the couple, captured in an intimate moment with a softly detailed background.", "18″×24″ canvas, up to 8 hours of live painting, with studio enhancements included."),
    ("Gold Collection", 3800, "Starting at $3,800", "A refined scene of the couple set within a detailed backdrop of your venue or ceremony space.", "24″×30″ canvas, live painting on-site, finished with studio detailing."),
    ("Platinum Collection", 5500, "$5,500+", "An immersive painting featuring the couple and more guests, set in a richly detailed environment.", "30″×40″ canvas, painted live with luxurious studio completion."),
]
steps_html = lambda steps: "\n".join(f'<div class="step"><h3>{t}</h3><p>{d}</p></div>' for t, d in steps)
pkgs_html = f"\n{DIVIDER}\n".join(
    f'<div class="package"><h3 class="pkg-name">{n}</h3><p class="price">{label}</p><p>{d}<br>{s}</p></div>' for n, p, label, d, s in WED_PKGS)

wed_body = f"""
<header class="page-title wrap"><h1 class="script title-lg">Live Wedding Painting</h1></header>
<section class="intro-split wrap">
  <img src="assets/images/live-wedding-painting-artist-at-work.webp" width="1400" height="933" fetchpriority="high"
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
    <p class="lead">A Bespoke Live Painting Experience for Your Wedding Day from the first brushstroke to the final flourish, your love story is transformed into a timeless heirloom. I paint weddings across Seattle and all of Washington.</p>
{steps_html(WED_STEPS)}
  </div>
</section>
<section class="packages wrap" aria-labelledby="pkg-title">
  <h2 id="pkg-title" class="script title-sm">Collections</h2>
  <p class="pkg-intro">Every collection includes hidden “Easter eggs” painted just for the two of you, and free travel within 50 miles of Seattle.</p>
{pkgs_html}
<p class="page-cta"><a class="btn" href="contact.html">Book a free consultation</a></p>
</section>
"""
wed_schema = [breadcrumb("Live Wedding Painting", "live-wedding-painting.html"), {
    "@context": "https://schema.org", "@type": "Service", "serviceType": "Live wedding painting",
    "name": "Live Wedding Painting", "provider": {"@id": f"{SITE}/#business"},
    "areaServed": AREAS,
    "offers": [{"@type": "Offer", "name": n, "priceCurrency": "USD", "description": f"{d} {s}",
                "priceSpecification": {"@type": "PriceSpecification", "minPrice": p, "priceCurrency": "USD"}}
               for n, p, label, d, s in WED_PKGS]}]

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
    ("The Gala", "$9,500+", 9500, "Guest Count 301+", "Includes an assistant or second artist"),
]
tiers_html = f"\n{DIVIDER}\n".join(
    f'<div class="tier"><h3 class="pkg-name small">{n}</h3><p class="price small">{p}</p><p>{c}{"<br>" + x if x else ""}</p></div>'
    for n, p, _, c, x in TIERS)
guest_body = f"""
<header class="page-title wrap"><h1 class="script title-lg">Guest Portraits</h1>
  <p class="page-sub">Live wedding and event guest portraits in Seattle and across Washington</p></header>
<section class="intro-split guest-split wrap">
  <div class="tilted">
    <img class="t1" src="assets/images/guest-portrait-sketch-from-phone.webp" width="656" height="840" fetchpriority="high"
         alt="Live guest portrait being sketched from a photo on a phone">
    <img class="t2" src="assets/images/guest-portrait-watercolor-couple.webp" width="946" height="1378"
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
  <h2 id="tiers-title" class="script title-sm">Guest Portrait Collections</h2>
{tiers_html}
</section>
<section class="ornaments wrap" id="ornaments" aria-labelledby="orn-title">
  <h2 id="orn-title" class="script title-sm">Live Ornament Portraits</h2>
  <p class="orn-lead">Guest portraits painted live and sealed in keepsake ornaments: the favor guests hang on their tree every year. Perfect for winter weddings and holiday parties.</p>
  <p class="orn-detail">Every ornament is packaged on-site by my assistant, ready for guests to take home.</p>
  <p class="orn-note">Ornament styles vary depending on availability. Please book at least 3 weeks before your event. Reach out for current options and pricing.</p>
  <p class="page-cta"><a class="btn" href="contact.html">Book a free consultation</a></p>
</section>
<section class="styles wrap" aria-labelledby="styles-title">
  <h2 id="styles-title" class="script title-sm">Portrait Styles</h2>
  <div class="style-grid">
    <img src="assets/images/guest-portrait-style-full-body-watercolor.webp" width="956" height="1400" loading="lazy"
         alt="Full-body watercolor fashion sketch guest portrait of a couple in formal wear">
    <img src="assets/images/guest-portrait-style-detailed.webp" width="1004" height="1400" loading="lazy"
         alt="Detailed zoomed-in guest portrait of a couple with pink hearts">
    <img src="assets/images/guest-portrait-style-faceless.webp" width="941" height="1400" loading="lazy"
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
    "areaServed": AREAS,
    "offers": [{"@type": "Offer", "name": n, "price": v, "priceCurrency": "USD",
                "description": c + (f". {x}" if x else "")} for n, _, v, c, x in TIERS]}]

# ---------------------------------------------------------------- CUSTOM ORDERS
custom_body = """
<div class="bg-white">
<header class="page-title wrap"><h1 class="script title-lg">Custom Orders</h1></header>
<section class="custom">
  <div class="custom-split">
    <img src="assets/images/custom-portrait-painting.webp" width="982" height="1342" fetchpriority="high"
         alt="Custom hand-painted canvas portrait of a couple on an easel">
    <ul class="custom-list">
      <li><h2>Custom Canvases &amp; Portraits:</h2><p>Transforming beloved pets, family photos, and special milestones into hand-painted canvas heirlooms.</p></li>
      <li><h2>Stationery &amp; Prints:</h2><p>Custom wedding invitations and fun, personalized stickers crafted from your favorite themes or photos.</p></li>
      <li><h2>Made for You, Wherever You Are:</h2><p>Every piece is painted by hand in my Seattle-area studio from your favorite photos, so you can commission one from anywhere.</p></li>
      <li><h2>Personalized Touches:</h2><p>Styled to match your aesthetic, complete with options for loose watercolor, fine detail, or hidden "Easter eggs."</p></li>
    </ul>
  </div>
</section>
<section class="custom-more wrap" aria-labelledby="ornament-title">
  <h2 id="ornament-title" class="script title-sm">Live Ornament Portraits</h2>
  <p>Hand-painted portraits of the people (and pets) you love, made to hang on the tree every year. Gift one painted from a favorite photo, or have guests painted live at your holiday party or winter wedding: the favor they actually keep.</p>
  <p class="orn-note">Ornament styles vary depending on availability. Please order at least 3 weeks ahead. Reach out for current options and pricing, or <a href="guest-portraits.html#ornaments">see live ornament portraits for events</a>.</p>
</section>
<section class="custom-more wrap" aria-labelledby="custom-how-title">
  <h2 id="custom-how-title" class="script title-sm">How a Custom Order Works</h2>
  <ol class="custom-steps">
    <li><h3>Share your idea</h3><p>Send me a few favorite photos and tell me who or what you’d like painted: a pet, your family, your wedding venue, or a milestone moment.</p></li>
    <li><h3>Choose your style</h3><p>Together we pick the size, medium and look, from loose watercolor to finely detailed portraiture, plus any hidden “Easter eggs” you’d like woven in.</p></li>
    <li><h3>I paint it by hand</h3><p>Every piece is painted by hand in my Seattle-area studio, with the same care I bring to live wedding paintings.</p></li>
    <li><h3>Ready to gift or hang</h3><p>Your finished piece is carefully packaged and ready to give, frame or hang at home.</p></li>
  </ol>
  <p class="custom-gifts">Popular as anniversary, wedding, holiday and memorial gifts, and as one-of-a-kind keepsakes of a beloved pet.</p>
  <p class="page-cta"><a class="btn" href="contact.html">Start a custom order</a></p>
</section>
</div>
"""
custom_schema = [breadcrumb("Custom Orders", "custom-orders.html"), {
    "@context": "https://schema.org", "@type": "Service", "serviceType": "Custom portrait painting",
    "name": "Custom Paintings, Portraits & Stationery", "provider": {"@id": f"{SITE}/#business"}}]

# ---------------------------------------------------------------- CONTACT
contact_body = f"""
<section class="contact contact-page" id="contact" aria-labelledby="contact-title">
  <h1 id="contact-title" class="script title-lg">Contact</h1>
  <p class="contact-intro">Tell me about your celebration and I’ll get back to you within a day to set up your free consultation.<br><span class="contact-base">Based in the Seattle area · Painting across Washington and beyond</span></p>
  <div class="contact-layout wrap">
    <form class="inquiry" id="inquiry" novalidate>
      <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
      <input type="hidden" name="from_name" value="Kala Fine Art website">
      <input type="checkbox" name="botcheck" class="visually-hidden" tabindex="-1" autocomplete="off">
      <div class="field-row">
        <label class="field"><span>Your name *</span><input id="f-name" name="name" required autocomplete="name"></label>
        <label class="field"><span>Email *</span><input id="f-email" name="email" type="email" required autocomplete="email"></label>
      </div>
      <div class="field-row">
        <label class="field"><span>Phone</span><input id="f-phone" name="phone" type="tel" autocomplete="tel"></label>
        <label class="field"><span>Event date</span><input id="f-date" name="event_date" type="date"></label>
      </div>
      <div class="field-row">
        <label class="field"><span>I’m interested in *</span>
          <select id="f-service" name="service" required>
            <option value="">Choose one</option>
            <option>Live Wedding Painting</option>
            <option>Guest Portraits</option>
            <option>Live Ornament Portraits</option>
            <option>Custom Painting or Portrait</option>
            <option>Something else</option>
          </select></label>
        <label class="field"><span>Venue or city</span><input id="f-venue" name="venue" autocomplete="address-level2"></label>
      </div>
      <label class="field"><span>Guest count</span><input id="f-guests" name="guest_count" inputmode="numeric" placeholder="If you know it"></label>
      <label class="field"><span>Tell me about your event *</span><textarea id="f-message" name="message" rows="5" required></textarea></label>
      <button class="btn" type="submit" id="f-submit">Request a free consultation</button>
      <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
    </form>
    <aside class="contact-side">
      <p class="contact-name">Wamika Bansal</p>
      <ul class="contact-list">
        <li>{ICONS['phone']}<a href="tel:+14258924523" style="text-decoration:none">{PHONE}</a></li>
        <li>{ICONS['instagram']}<a href="{IG}" target="_blank" rel="noopener">kalafineart</a></li>
        <li>{ICONS['tiktok']}<a href="{TT}" target="_blank" rel="noopener">kalafineart</a></li>
        <li>{ICONS['email']}<a href="mailto:{EMAIL}" style="text-decoration:none">{EMAIL}</a></li>
      </ul>
    </aside>
  </div>
</section>
"""
FORM_SCRIPT = """
<script>
(function () {
  var form = document.getElementById("inquiry");
  if (!form) return;
  var status = document.getElementById("form-status");
  var btn = document.getElementById("f-submit");
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var missing = [].filter.call(form.querySelectorAll("[required]"), function (el) { return !el.value.trim(); });
    var email = form.elements.email;
    if (missing.length || (email.value && !email.checkValidity())) {
      status.className = "form-status error";
      status.textContent = missing.length ? "Please fill in the fields marked with *." : "Please check your email address.";
      (missing[0] || email).focus();
      return;
    }
    var data = Object.fromEntries(new FormData(form));
    data.subject = "New inquiry: " + data.service + (data.event_date ? " on " + data.event_date : "") + " from " + data.name;
    data.replyto = data.email;
    btn.disabled = true; btn.textContent = "Sending…";
    status.className = "form-status"; status.textContent = "";
    fetch("https://api.web3forms.com/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify(data)
    }).then(function (r) { return r.json(); }).then(function (res) {
      if (!res.success) throw new Error(res.message);
      form.reset();
      status.className = "form-status ok";
      status.textContent = "Thank you! Your inquiry is on its way. I’ll be in touch within a day.";
    }).catch(function () {
      status.className = "form-status error";
      status.textContent = "Sorry, that didn’t send. Please email me at kala.fine.artist@gmail.com or text +1 425-892-4523.";
    }).finally(function () { btn.disabled = false; btn.textContent = "Request a free consultation"; });
  });
})();
</script>"""
contact_schema = [breadcrumb("Contact", "contact.html"), {
    "@context": "https://schema.org", "@type": "ContactPage", "name": "Contact Kala Fine Art",
    "url": f"{SITE}/contact.html", "about": {"@id": f"{SITE}/#business"}}]

PAGES = {
    "index.html": ("Live Wedding Painter in Seattle, WA | Kala Fine Art by Wamika Bansal",
                   "Live wedding painting and guest portraits by Wamika Bansal, a Seattle-area live wedding painter serving Seattle, Bellevue, the Puget Sound, Leavenworth and the San Juan Islands.",
                   home_body, [BUSINESS, faq_schema]),
    "live-wedding-painting.html": ("Live Wedding Painting in Seattle & Washington | Packages & Pricing",
                   "Bespoke live wedding paintings created on-site at your Seattle, Eastside or Washington destination wedding. Collections starting at $2,500, with free travel within 50 miles.",
                   wed_body, wed_schema),
    "guest-portraits.html": ("Live Guest Portraits for Seattle Weddings & Events | Kala Fine Art",
                   "Live guest portraits for Seattle-area weddings and events, on custom stationery — a one-of-a-kind favor every guest takes home. Watercolor, detailed and fashion-sketch styles. Packages from $2,000.",
                   guest_body, guest_schema),
    "custom-orders.html": ("Custom Pet, Family & Couple Portraits, Seattle | Kala Fine Art",
                   "Commission a custom hand-painted canvas of your pets, family or special milestone, plus custom wedding invitations and personalized stickers by Wamika Bansal.",
                   custom_body, custom_schema),
    "contact.html": ("Book Live Wedding Painting | Contact Kala Fine Art",
                   "Send an inquiry to Wamika Bansal of Kala Fine Art to book live wedding painting, live guest portraits or a custom painting.",
                   contact_body, contact_schema, FORM_SCRIPT),
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
