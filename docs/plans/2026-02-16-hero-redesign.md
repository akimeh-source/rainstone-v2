# Hero Split-Screen Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the full-bleed overlay hero with a bold asymmetric split-screen layout featuring a diagonal clip-path, staggered text animations, and real sourced award logos.

**Architecture:** Both the Personal and Commercial hero sections get rebuilt with the same split-screen structure: a 55% dark-green text panel on the left, a 45% image/video panel on the right separated by a diagonal clip-path. CSS keyframe animations handle the staggered reveal. Award logos are sourced as images and displayed with CSS filter for consistent gold/white treatment.

**Tech Stack:** HTML, CSS (keyframes, clip-path, custom properties), vanilla JS (existing parallax updated)

---

### Task 1: Source and save award logo images

**Files:**
- Create: `images/logos/nacfb.png`
- Create: `images/logos/fca.png`
- Create: `images/logos/commercial-broker-awards.png`
- Create: `images/logos/sme-news-awards.png`
- Create: `images/logos/signature-awards.png`

**Step 1: Create the logos directory**

```bash
mkdir -p images/logos
```

**Step 2: Source the logo images**

Download or source official logos for these 5 organizations. Place them in `images/logos/`. Acceptable formats: PNG or SVG. If official logos cannot be downloaded programmatically, create clean SVG text-based placeholder badges that look professional (org name in a styled badge shape) to be replaced with real logos later.

**Step 3: Commit**

```bash
git add images/logos/
git commit -m "feat: add award/accreditation logo images"
```

---

### Task 2: Rewrite Personal hero HTML to split-screen layout

**Files:**
- Modify: `index.html:120-157` (Personal hero section)

**Step 1: Replace the Personal hero section**

Replace everything from `<!-- PERSONAL HERO -->` comment through the closing `</section>` (lines 120-157) with:

```html
    <!-- ================================================================
         PERSONAL HERO — Split-Screen
         ================================================================ -->
    <section class="hero hero-split tab-personal" id="hero">
        <div class="hero-panel-left">
            <div class="hero-grain"></div>
            <div class="hero-diagonal-accent"></div>
            <div class="hero-text-wrap">
                <div class="hero-gold-line hero-anim" style="--delay:0ms"></div>
                <div class="hero-label hero-anim" style="--delay:100ms">Independent Brokers</div>
                <h1>
                    <span class="hero-line hero-anim" style="--delay:200ms">Independent Mortgage &amp;</span>
                    <span class="hero-line hero-anim" style="--delay:350ms">Commercial Finance</span>
                    <span class="hero-line hero-anim" style="--delay:500ms">Brokers <em class="text-gold-italic">in the UK</em></span>
                </h1>
                <p class="hero-subtitle hero-anim" style="--delay:650ms">Providing expert financial solutions <span class="gold-dot">&middot;</span> Over 100 years combined experience <span class="gold-dot">&middot;</span> Nationwide coverage</p>
                <div class="hero-btns hero-anim" style="--delay:800ms">
                    <a href="#contact" class="btn btn-secondary">Free Consultation <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
        </div>
        <div class="hero-panel-right">
            <div class="hero-panel-img hero-img-personal"></div>
        </div>
        <div class="hero-logos">
            <div class="container hero-logos-inner">
                <img class="hero-logo-img hero-anim" style="--delay:900ms" src="images/logos/nacfb.png" alt="NACFB Member" loading="eager">
                <img class="hero-logo-img hero-anim" style="--delay:1000ms" src="images/logos/fca.png" alt="FCA Authorised" loading="eager">
                <img class="hero-logo-img hero-anim" style="--delay:1100ms" src="images/logos/commercial-broker-awards.png" alt="BTL Broker of the Year 2024" loading="eager">
                <img class="hero-logo-img hero-anim" style="--delay:1200ms" src="images/logos/sme-news-awards.png" alt="Most Innovative 2023" loading="eager">
                <img class="hero-logo-img hero-anim" style="--delay:1300ms" src="images/logos/signature-awards.png" alt="Excellence in Financial Services 2023" loading="eager">
            </div>
        </div>
    </section>
```

**Step 2: Verify the HTML is valid**

Open `index.html` in the browser, confirm no broken tags. The section will be unstyled at this point -- that's expected.

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: rewrite personal hero HTML to split-screen layout"
```

---

### Task 3: Rewrite Commercial hero HTML to split-screen layout

**Files:**
- Modify: `index.html:159-197` (Commercial hero section, line numbers will have shifted from Task 2)

**Step 1: Replace the Commercial hero section**

Replace everything from `<!-- COMMERCIAL HERO -->` comment through its closing `</section>` with:

```html
    <!-- ================================================================
         COMMERCIAL HERO — Split-Screen with video
         ================================================================ -->
    <section class="hero hero-split tab-commercial" id="hero-commercial">
        <div class="hero-panel-left">
            <div class="hero-grain"></div>
            <div class="hero-diagonal-accent"></div>
            <div class="hero-text-wrap">
                <div class="hero-gold-line hero-anim" style="--delay:0ms"></div>
                <div class="hero-label hero-anim" style="--delay:100ms">Commercial Specialists</div>
                <h1>
                    <span class="hero-line hero-anim" style="--delay:200ms">Commercial Finance</span>
                    <span class="hero-line hero-anim" style="--delay:350ms"><em class="text-gold-italic">MADE EASY</em></span>
                </h1>
                <p class="hero-subtitle hero-anim" style="--delay:500ms">Built for Complexity, Powered by Expertise <span class="gold-dot">&middot;</span> Tailored funding for businesses, developers, and high-net-worth individuals</p>
                <div class="hero-btns hero-anim" style="--delay:650ms">
                    <a href="#contact" class="btn btn-secondary">Book A Consultation <i class="fas fa-arrow-right"></i></a>
                    <a href="#about" class="btn btn-outline-light">Speak to an Expert <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
        </div>
        <div class="hero-panel-right">
            <video class="hero-video" autoplay muted loop playsinline preload="auto">
                <source src="videos/commercial-hero.mp4" type="video/mp4">
            </video>
        </div>
        <div class="hero-logos">
            <div class="container hero-logos-inner">
                <img class="hero-logo-img hero-anim" style="--delay:750ms" src="images/logos/nacfb.png" alt="NACFB Member" loading="eager">
                <img class="hero-logo-img hero-anim" style="--delay:850ms" src="images/logos/fca.png" alt="FCA Authorised" loading="eager">
                <img class="hero-logo-img hero-anim" style="--delay:950ms" src="images/logos/commercial-broker-awards.png" alt="BTL Broker of the Year 2024" loading="eager">
                <img class="hero-logo-img hero-anim" style="--delay:1050ms" src="images/logos/sme-news-awards.png" alt="Most Innovative 2023" loading="eager">
                <img class="hero-logo-img hero-anim" style="--delay:1150ms" src="images/logos/signature-awards.png" alt="Excellence in Financial Services 2023" loading="eager">
            </div>
        </div>
    </section>
```

**Step 2: Commit**

```bash
git add index.html
git commit -m "feat: rewrite commercial hero HTML to split-screen layout"
```

---

### Task 4: Replace hero CSS with split-screen styles

**Files:**
- Modify: `css/style.css:382-506` (the entire `/* ---------- HERO ---------- */` block through `.badge-icon` closing brace)

**Step 1: Replace the hero CSS block**

Replace everything from `/* ---------- HERO ---------- */` (line 382) through the `.badge-icon` closing brace (line 506) with the new split-screen CSS:

```css
/* ---------- HERO (Split-Screen) ---------- */
.hero-split {
    position: relative;
    display: grid;
    grid-template-columns: 55% 45%;
    min-height: 100vh;
    overflow: hidden;
}

/* Left panel — dark green with text */
.hero-panel-left {
    position: relative;
    background: var(--green-dark);
    display: flex;
    align-items: center;
    padding: 120px 60px 100px 8%;
    z-index: 2;
}

/* Grain texture on left panel */
.hero-grain {
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
    opacity: .03;
    pointer-events: none;
    mix-blend-mode: overlay;
}

/* Gold diagonal accent line tracing the clip edge */
.hero-diagonal-accent {
    position: absolute;
    top: 0;
    right: -1px;
    width: 2px;
    height: 141%;
    background: var(--gold);
    opacity: .2;
    transform: rotate(8deg);
    transform-origin: top right;
    pointer-events: none;
    z-index: 3;
}

/* Text wrapper */
.hero-text-wrap {
    position: relative;
    z-index: 2;
    max-width: 620px;
}

/* Gold vertical accent line above heading */
.hero-gold-line {
    width: 2px;
    height: 60px;
    background: var(--gold);
    margin-bottom: 24px;
}

/* Section label */
.hero-label {
    font-size: .75rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--gold);
    font-weight: 600;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 14px;
}
.hero-label::before,
.hero-label::after {
    content: '';
    width: 24px;
    height: 1.5px;
    background: var(--gold);
    opacity: .5;
}

/* Heading */
.hero-split h1 {
    font-family: var(--font-display);
    font-weight: 700;
    font-size: clamp(2.8rem, 5.5vw, 4.2rem);
    line-height: 1.1;
    color: var(--white);
    margin-bottom: 24px;
    letter-spacing: -0.02em;
}
.hero-line {
    display: block;
}
.text-gold-italic {
    color: var(--gold);
    font-style: italic;
}

/* Subtitle */
.hero-split .hero-subtitle {
    color: rgba(255,255,255,.7);
    font-size: 1.05rem;
    margin-bottom: 40px;
    line-height: 1.8;
    letter-spacing: .01em;
}
.gold-dot {
    color: var(--gold);
    margin: 0 6px;
}

/* CTA buttons */
.hero-split .hero-btns {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}

/* Right panel — image or video */
.hero-panel-right {
    position: relative;
    overflow: hidden;
    clip-path: polygon(10% 0, 100% 0, 100% 100%, 0% 100%);
}
.hero-panel-img {
    position: absolute;
    inset: 0;
    background-size: cover;
    background-position: center;
}
.hero-img-personal {
    background-image: url('https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=1920&q=80');
}
.hero-panel-right .hero-video {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

@media (prefers-reduced-motion: reduce) {
    .hero-panel-right .hero-video { display: none }
}

/* ---------- HERO ANIMATIONS ---------- */
@keyframes heroFadeUp {
    from { opacity: 0; transform: translateY(30px) }
    to   { opacity: 1; transform: translateY(0) }
}
@keyframes heroScaleIn {
    from { opacity: 0; transform: scale(0.95) }
    to   { opacity: 1; transform: scale(1) }
}
@keyframes heroLineGrow {
    from { transform: scaleY(0) }
    to   { transform: scaleY(1) }
}

.hero-anim {
    opacity: 0;
    animation: heroFadeUp .7s var(--ease-out) forwards;
    animation-delay: var(--delay, 0ms);
}
.hero-gold-line {
    transform-origin: top;
    animation-name: heroLineGrow;
}
.hero-btns.hero-anim {
    animation-name: heroScaleIn;
}

/* ---------- HERO LOGO STRIP ---------- */
.hero-logos {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 10;
    background: var(--green-deep);
    border-top: 1px solid rgba(201,168,76,.12);
    padding: 18px 0;
}
.hero-logos-inner {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 48px;
    flex-wrap: wrap;
}
.hero-logo-img {
    max-height: 36px;
    width: auto;
    opacity: .65;
    filter: brightness(0) invert(1);
    transition: opacity .4s var(--ease-out), filter .4s;
}
.hero-logo-img:hover {
    opacity: 1;
    filter: brightness(0) invert(1) sepia(1) saturate(3) hue-rotate(10deg);
}
```

**Step 2: Verify in browser**

Open `index.html` in browser. Confirm:
- Split layout renders with dark green left, image right
- Diagonal clip-path creates the angled edge
- Text animates in staggered sequence
- Badge logos appear at the bottom
- Commercial tab shows video in the right panel

**Step 3: Commit**

```bash
git add css/style.css
git commit -m "feat: replace hero CSS with split-screen layout and animations"
```

---

### Task 5: Add responsive rules for split-screen hero

**Files:**
- Modify: `css/style.css` — inside the `@media (max-width: 768px)` block and `@media (max-width: 480px)` block

**Step 1: Add responsive hero overrides inside the 768px media query**

Find the existing hero responsive rules inside the `@media (max-width: 768px)` block (currently `.hero-text h1`, `.hero-content`, `.hero-logos-inner`, `.logo-badge`) and replace them with:

```css
    /* Split hero stacks on mobile */
    .hero-split {
        grid-template-columns: 1fr;
        min-height: auto;
    }
    .hero-panel-left {
        padding: 100px 24px 80px;
    }
    .hero-panel-right {
        clip-path: none;
        height: 40vh;
    }
    .hero-split h1 { font-size: clamp(1.8rem, 7vw, 2.8rem) }
    .hero-logos-inner {
        gap: 24px;
        justify-content: flex-start;
        overflow-x: auto;
        flex-wrap: nowrap;
        padding-bottom: 8px;
        -webkit-overflow-scrolling: touch;
    }
    .hero-logo-img { flex-shrink: 0 }
    .hero-logos { position: relative }
    .hero-diagonal-accent { display: none }
```

**Step 2: Add responsive hero overrides inside the 480px media query**

Find the existing `.hero-text h1` rule inside the `@media (max-width: 480px)` block and replace with:

```css
    .hero-split h1 { font-size: 1.8rem }
    .hero-panel-right { height: 30vh }
```

**Step 3: Verify on mobile viewport**

Open browser dev tools, toggle to mobile viewport (375px width). Confirm:
- Hero stacks vertically (text above, image below)
- No diagonal clip-path on mobile
- Logo strip scrolls horizontally
- Text is readable at mobile font sizes

**Step 4: Commit**

```bash
git add css/style.css
git commit -m "feat: add responsive rules for split-screen hero"
```

---

### Task 6: Update JS parallax to target new hero elements

**Files:**
- Modify: `js/main.js:258-276` (the `// ---- Subtle Hero Parallax ----` block)

**Step 1: Update the parallax selector**

The current parallax targets `.hero-image, .hero-video`. The new structure uses `.hero-panel-img, .hero-panel-right .hero-video`. Replace the parallax block:

```javascript
    // ---- Subtle Hero Parallax ----
    const heroVisuals = document.querySelectorAll('.hero-panel-img, .hero-panel-right .hero-video');
    if (heroVisuals.length && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        let ticking = false;
        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    const y = window.scrollY;
                    if (y < window.innerHeight) {
                        heroVisuals.forEach(el => {
                            el.style.transform = 'translateY(' + (y * 0.15) + 'px) scale(1.05)';
                        });
                    }
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });
    }
```

Note: parallax factor reduced from 0.25 to 0.15 since the image panel is narrower now.

**Step 2: Commit**

```bash
git add js/main.js
git commit -m "feat: update parallax to target new split-screen hero elements"
```

---

### Task 7: Clean up old hero CSS and unused classes

**Files:**
- Modify: `css/style.css` — remove orphaned rules
- Modify: `css/style.css` — remove old `.hero-image-personal`, `.hero-image-commercial`, `.hero-bg`, `.hero-overlay`, `.hero-overlay-commercial`, `.hero::after` rules if they still exist after Task 4

**Step 1: Search for and remove any remaining old hero class rules**

Search the CSS for these class names which are no longer referenced in the HTML:
- `.hero-bg`
- `.hero-overlay` (without `-commercial`)
- `.hero-overlay-commercial`
- `.hero-image`
- `.hero-image-personal`
- `.hero-image-commercial`
- `.hero-content`
- `.hero-text`
- `.hero::after`
- `.badge-icon`
- `.logo-badge`

Remove any rules for these classes that still exist. They were replaced by the new split-screen classes in Task 4.

**Step 2: Also remove the old `.btn-outline-light` if no longer used**

Check if `.btn-outline-light` is still referenced in the commercial hero HTML. If yes (it is -- the "Speak to an Expert" button uses it), keep it. If not, remove it.

**Step 3: Verify nothing is visually broken**

Open browser, test both Personal and Commercial tabs. Ensure no console errors about missing elements.

**Step 4: Commit**

```bash
git add css/style.css
git commit -m "chore: remove orphaned hero CSS classes from old layout"
```

---

### Task 8: Final visual QA and push

**Files:** None modified -- this is a review/push step

**Step 1: Full visual review**

Check in browser at these viewports:
- Desktop 1440px: Split layout, diagonal clip-path, animations, badge logos
- Tablet 768px: Stacked layout, no diagonal, all content visible
- Mobile 375px: Compact layout, scrollable logos
- Test both Personal and Commercial tabs
- Test the mode switcher -- video should play on commercial, pause on personal

**Step 2: Push all changes**

```bash
git push
```

**Step 3: Verify on Cloudflare Pages**

Visit https://rainstone.pages.dev/ and do a hard refresh (`Ctrl+Shift+R`). Confirm the new split-screen hero is live.
