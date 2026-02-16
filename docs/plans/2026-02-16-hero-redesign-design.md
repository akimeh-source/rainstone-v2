# Hero Section Redesign: Bold Split-Screen

**Date:** 2026-02-16
**Status:** Approved
**Scope:** Personal hero + Commercial hero sections

## Summary

Replace the current full-bleed overlay hero with a bold asymmetric split-screen layout. Left panel (dark green) holds all text content with staggered reveal animations. Right panel (45%) holds lifestyle photography (personal) or video (commercial) with a diagonal clip-path edge creating a sharp geometric cut between the two halves.

## Layout & Structure

- **Full viewport height** (`100vh`), content vertically centered
- **Left panel (55%):** `#1B3C2D` background with grain texture overlay. Text content vertically centered, left-padded ~8% from edge. Thin vertical gold accent line (2px, ~60px) above the heading
- **Right panel (45%):** Full-bleed image/video. Left edge uses a **diagonal clip-path** slanting ~8-10 degrees from top-left to bottom-right
- **Diagonal accent:** 1px gold line tracing the diagonal edge on the dark side
- **Personal hero:** Warm lifestyle photo (consultation/meeting scene) in right panel
- **Commercial hero:** Existing `commercial-hero.mp4` video in right panel, same split layout

## Typography & Text Treatment

### Section label
- "INDEPENDENT BROKERS" in small caps, gold, letter-spacing 4px
- Flanked by gold dashes: `-- INDEPENDENT BROKERS --`
- Fades in first (0ms delay)

### Heading
- Playfair Display, white, `clamp(2.8rem, 5.5vw, 4.2rem)`
- Text: "Independent Mortgage & / Commercial Finance / Brokers *in the UK*"
- "in the UK" rendered in gold italic Playfair Display
- Each line animates separately: slide-up 30px + fade, staggered 0ms / 150ms / 300ms

### Subtitle
- DM Sans, `rgba(255,255,255,.7)`, 1.05rem
- Pipe separators replaced with gold middle-dot characters
- "Providing expert financial solutions . Over 100 years combined experience . Nationwide coverage"
- Animates as single block at 450ms delay

### CTA Button
- "Free Consultation" with arrow icon
- Gold background (`#C9A84C`), dark green text (`#1B3C2D`) -- inverted from current for contrast against dark panel
- Scale-up animation (0.95 to 1.0) at 600ms delay

## Badge / Trust Strip

- **Position:** Full-width bar at bottom of hero, overlapping both panels
- **Background:** `#152E22`, 1px top border `rgba(201,168,76,.15)`
- **Content:** Real sourced award/accreditation logos:
  1. NACFB (member badge)
  2. FCA (authorized badge)
  3. Commercial Broker Awards -- "BTL Broker of the Year 2024"
  4. SME News Awards -- "Most Innovative 2023"
  5. The Signature Awards -- "Excellence in Financial Services 2023"
- **Logo treatment:** CSS filter to render as white or gold monochrome for visual consistency
- **Layout:** Centered, `gap: 48px`, each logo max-height 36px, opacity 0.7 default, 1.0 on hover
- **Animation:** Stagger in left-to-right, 100ms delays, starting at ~800ms after page load
- **Mobile:** Horizontally scrollable strip

## Animation Sequence (Timeline)

| Delay  | Element              | Animation                   |
|--------|----------------------|-----------------------------|
| 0ms    | Gold accent line     | Scale-Y from 0 to 1         |
| 100ms  | Section label        | Fade in                      |
| 200ms  | Heading line 1       | Slide up 30px + fade         |
| 350ms  | Heading line 2       | Slide up 30px + fade         |
| 500ms  | Heading line 3       | Slide up 30px + fade         |
| 650ms  | Subtitle             | Fade in                      |
| 800ms  | CTA button           | Scale 0.95 to 1.0 + fade     |
| 900ms+ | Badge logos (stagger) | Fade in, 100ms apart          |

## Technical Notes

- Diagonal clip-path uses `clip-path: polygon(...)` on the right panel
- Staggered animations via CSS `@keyframes` with `animation-delay`, no JS needed
- Award logos sourced as images, placed in `/images/logos/` directory
- Commercial hero reuses existing `videos/commercial-hero.mp4` inside the right panel
- Grain texture reuses existing SVG noise pattern from current CSS
- Both Personal and Commercial heroes share the same split layout component, differing only in right panel content (image vs video)
