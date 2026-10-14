---
name: Kevin Pelozo
description: The CV as a node canvas. Every skill and job is a node, edges show what fed what, and the graph converges on the work he ships today.
colors:
  canvas-grey: "#f4f5f7"
  node-white: "#ffffff"
  graphite-ink: "#0e1116"
  slate-ink: "#474f5c"
  pewter-meta: "#626a77"
  hairline: "#dde1e7"
  grid-dot: "#cdd2d9"
  kind-base: "#0e1116"
  kind-build: "#2f6bff"
  kind-ops: "#0f8a5a"
  signal-orange: "#ff4f12"
  signal-orange-text: "#c63a06"
  signal-wash: "#fff1ea"
  on-signal: "#ffffff"
  night-canvas: "#0d0f13"
  night-node: "#151920"
  night-ink: "#eef0f3"
  night-ink-2: "#b4bac5"
  night-meta: "#8f97a4"
  night-hairline: "#262c36"
  night-dot: "#2b313b"
  night-kind-build: "#6b95ff"
  night-kind-ops: "#36c08a"
  night-signal-orange: "#ff6a33"
  night-signal-orange-text: "#ff8a5c"
  night-signal-wash: "#2a160d"
typography:
  display:
    fontFamily: "Geist, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(48px, 6vw, 84px)"
    fontWeight: 800
    lineHeight: 0.96
    letterSpacing: "-0.045em"
  closing:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(44px, 6.4vw, 88px)"
    fontWeight: 800
    lineHeight: 0.98
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(34px, 4.2vw, 52px)"
    fontWeight: 750
    lineHeight: 1.08
    letterSpacing: "-0.04em"
  title:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: "22px"
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.025em"
  lede:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: "18.5px"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.6
    fontFeature: "tnum"
  node-title:
    fontFamily: "Geist, ui-sans-serif, system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 650
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  label-mono:
    fontFamily: "Geist Mono, ui-monospace, SF Mono, Menlo, monospace"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0"
rounded:
  square: "2px"
  control: "8px"
  button: "10px"
  node: "12px"
  canvas: "18px"
spacing:
  unit: "8px"
  sm: "16px"
  md: "24px"
  lg: "48px"
  section: "96px"
  gutter: "clamp(16px, 4vw, 48px)"
  max: "1280px"
  measure: "64ch"
components:
  button-primary:
    backgroundColor: "{colors.graphite-ink}"
    textColor: "{colors.canvas-grey}"
    rounded: "{rounded.button}"
    padding: "0 22px"
    height: "48px"
  button-primary-hover:
    backgroundColor: "{colors.signal-orange}"
    textColor: "{colors.on-signal}"
  lang-switch:
    backgroundColor: "{colors.node-white}"
    textColor: "{colors.graphite-ink}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.control}"
    padding: "0 10px"
    height: "32px"
  node:
    backgroundColor: "{colors.node-white}"
    textColor: "{colors.graphite-ink}"
    typography: "{typography.node-title}"
    rounded: "{rounded.node}"
    padding: "10px 12px"
  node-ai:
    backgroundColor: "{colors.signal-wash}"
    textColor: "{colors.graphite-ink}"
    rounded: "{rounded.node}"
    padding: "10px 12px"
  node-next:
    backgroundColor: "transparent"
    textColor: "{colors.graphite-ink}"
    rounded: "{rounded.node}"
    padding: "10px 12px"
  canvas:
    backgroundColor: "{colors.node-white}"
    rounded: "{rounded.canvas}"
  cell:
    backgroundColor: "{colors.node-white}"
    textColor: "{colors.graphite-ink}"
    rounded: "{rounded.canvas}"
    padding: "24px"
  cell-ai:
    backgroundColor: "{colors.graphite-ink}"
    textColor: "{colors.canvas-grey}"
    rounded: "{rounded.canvas}"
    padding: "24px"
  cell-tint:
    backgroundColor: "{colors.signal-wash}"
    textColor: "{colors.graphite-ink}"
    rounded: "{rounded.canvas}"
    padding: "24px"
---

# Design System: Kevin Pelozo

## Overview

**Creative North Star: "The Career Graph"**

The page is a builder's node canvas. A cool grey workspace holds white nodes with a hairline rule and a soft tinted shadow; inside a canvas, a 22px dot grid sits underneath, and orthogonal edges run through the gutters between columns, entering and leaving each node at a small port. Every skill, job, project group and heading carries a kind: base (ink), build (blue), ops (green) or AI (signal orange). The kind square is the thread that continues from the graph into the bento, the Finwaise case, the project registry and the experience list, so the whole CV reads as one graph that ends at a dashed "next node": the reader's team.

The tone is a precise engineering tool, not a showcase. Geist carries display and body at heavy, tightly tracked weights; Geist Mono is reserved for metadata (kind labels, dates, stack lines, data-list terms). One accent, signal orange, marks AI and the output a flow converges on; everything else stays graphite on grey. Dark mode is the same canvas at night, not a different world.

Motion has a job: small tokens flow along edges toward the output, and focusing a node keeps its neighbourhood lit while the rest of the graph recedes. Reduced motion hides the tokens entirely and leaves the static graph intact. Rejected: the earlier transit-map/timeline world, the dark neon card grid, and any pitch of him as only a "workflows and agents" builder.

**Key Characteristics:**
- Node canvas: white nodes, 1px hairline, soft shadow, 12px corners, ports, orthogonal gutter edges over a 22px dot grid.
- Four node kinds coded by a 9-10px square; AI is the only circle.
- One accent (signal orange) for AI and convergence outputs.
- Geist for words, Geist Mono for metadata only.
- 8px unit; section rhythm of 96px; content capped at 1280px.
- Flow tokens and focus dimming as the only ambient motion.

## Colors

Cool, neutral graphite and grey carry the page; three kind colors code the graph, and one hot orange is spent only where AI or a convergence point appears.

### Primary
- **Signal Orange** (`signal-orange`): the AI kind. Fills the AI kind circle, the brand mark, AI edges (`.is-ai`, 85% opacity), the border of output nodes, the primary button hover, text selection and the flow token heading to the output. Never used for body text: below large sizes it fails contrast on white.
- **Signal Orange Text** (`signal-orange-text`): the text-safe orange for emphasised words in the hero role line and the contact headline, and for the contact email on hover.
- **Signal Wash** (`signal-wash`): the background of AI nodes and the one tinted bento cell; borders on wash surfaces mix 30-70% orange into the hairline.

### Secondary
- **Build Blue** (`kind-build`): the build kind (web, backend, frontend, integrations) and the default fallback for any kind square. Also the focus ring (2px outline, 3px offset).
- **Ops Green** (`kind-ops`): the ops kind (infrastructure, quality, verification).

### Neutral
- **Canvas Grey** (`canvas-grey`): page background and sticky header background.
- **Node White** (`node-white`): nodes, canvases, bento cells, the language switch.
- **Graphite Ink** (`graphite-ink`): headings, primary text, the base kind, the primary button, the inverted AI cell, the 1px rule under project group heads.
- **Slate Ink** (`slate-ink`): secondary prose (ledes, intros, descriptions, list items).
- **Pewter Meta** (`pewter-meta`): metadata, kind labels, dates, stack lines, edges (50% opacity), ports, the experience bullet outline.
- **Hairline** (`hairline`): every 1px border and section rule.
- **Grid Dot** (`grid-dot`): the dot grid inside canvases only.

Dark mode swaps every role through `prefers-color-scheme: dark` to the `night-*` values; the base kind becomes `night-ink`, and `on-signal` becomes `night-canvas` so text on orange stays dark.

### Named Rules
**The One Signal Rule.** Orange appears only on the AI kind, on output nodes where a flow converges, on the primary button's hover, and on two emphasised phrases. If a new element is orange and is neither AI nor an output, it is wrong.

**The Kind Square Rule.** Category is shown by a small square in the kind color (2px corners), never by a colored background block or a colored heading. The AI kind is the only circle.

## Typography

**Display Font:** Geist (with ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif), self-hosted variable woff2, weights 100-900, latin and latin-ext subsets, `font-display: swap`, the latin file preloaded.
**Body Font:** Geist (same stack).
**Label/Mono Font:** Geist Mono (with ui-monospace, SF Mono, Menlo, monospace), self-hosted.

**Character:** One grotesque used heavy and tight for statements, regular and open for reading, with a monospace companion that reads like node metadata in a builder tool. The user chose this pairing (prototype A, 2026-10-13); the detector's overused-font finding for Geist and Geist Mono is recorded as an approved ignore in `.impeccable/config.json`.

### Hierarchy
- **Display** (800, clamp(48px, 6vw, 84px), 0.96, -0.045em): the hero name. The Finwaise case title uses the same voice at clamp(48px, 6vw, 80px), line-height 1.
- **Closing** (800, clamp(44px, 6.4vw, 88px), 0.98, -0.04em): the contact headline ("next node") and the 404 headline, max 15ch.
- **Headline** (750, clamp(34px, 4.2vw, 52px), 1.08, -0.04em): section titles, max 20ch, balanced wrap.
- **Title** (700, 20-24px, -0.025em): bento cell heads (22px), project group heads (20px), experience role (24px). The inverted AI cell head scales to clamp(28px, 3vw, 38px).
- **Lead lines** (600-650, 21px, -0.015em): the hero role line and the case "what it is" line.
- **Lede** (400, 18-19px, 1.55): hero lede (40ch), section intros (64ch), contact lede (50ch).
- **Body** (400, 17px desktop / 16px phone, 1.6, tabular numerals): running text and lists, measure 64ch.
- **Node title** (650, 14px, -0.01em): the bold name inside a node; 17px on output nodes. Node subtext is 12px pewter.
- **Label mono** (400, 12-13px, no tracking, lowercase as written): kind labels, `.tools` and facts terms, dates, project stack lines, canvas captions.

### Named Rules
**The Metadata-Only Mono Rule.** Geist Mono labels data: a node's kind, a date, a stack line, a term in a definition list, a canvas caption. It never sits above a heading as an eyebrow or kicker. Headings carry only their kind square.

**The Heavy-Tight Rule.** Display and headline sizes run 750-800 with negative tracking (-0.04em or tighter); nothing above 30px is set at regular weight.

## Layout

An 8px unit (`--u`) drives spacing; observed steps are 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96 and 112px. Content sits in a centred wrap capped at 1280px with a fluid gutter of clamp(16px, 4vw, 48px). Sections are separated by a full-bleed 1px hairline and 96px of block padding (64px on phones); contact opens with 112px. The sticky header is 64px tall, and anchors scroll with 80px of padding.

- **Hero:** two columns at 4fr / 8fr, name and actions left, the career graph canvas right; one column below 1180px.
- **Career graph:** an SVG viewBox of 760 x 600 with 11 nodes in four columns (base, build, ops/integration, AI/output). Node geometry is generated into the stylesheet as percentage boxes; edges and ports are absolute SVG coordinates in the same space.
- **Skills bento:** a 12-column grid with 16px gaps. The AI cell spans 7 columns and 2 rows; other cells span 5, 4 or 6. At 1080px non-AI cells go to 6 and the AI cell to full width; at 720px everything stacks.
- **Finwaise case:** 5fr / 7fr, text left and a second canvas (760 x 500 flowchart) right; one column below 1080px.
- **Project registry:** two columns of groups with 48px x 40px gaps; one column on phones.
- **Experience:** 3fr date column / 9fr content; a four-column facts row below (two at 1080px, one at 720px).
- **Phones (720px and below):** canvases drop the SVG edges and become vertical node lists joined by a single 1.5px pewter connector on the left, each node marked by a 9px port circle (filled orange for AI); kind labels collapse to their square. The section nav hides and only the language switch remains.

## Elevation & Depth

The system is flat with one exception: nodes. Nodes lift off the canvas with a soft, ink-tinted two-layer shadow; every other surface (cells, canvases, header, buttons) is separated by tone and a 1px hairline only. Depth inside a canvas is otherwise conveyed by layering order: dot grid, then edges and ports, then nodes.

### Shadow Vocabulary
- **Node lift** (`box-shadow: 0 1px 2px rgb(14 17 22 / 0.07), 0 3px 8px -4px rgb(14 17 22 / 0.14)`; night: `0 1px 2px rgb(0 0 0 / 0.4), 0 3px 8px -4px rgb(0 0 0 / 0.5)`): nodes on a canvas. The "next" node drops it.

### Named Rules
**The Only-Nodes-Float Rule.** Shadows belong to nodes. Cells, canvases, buttons and the header stay flat; if something else needs separation, use the hairline.

## Shapes

Gently rounded rectangles at a small, stepped radius scale: 2px for kind squares and bullets, 8px for small controls (language switch, skip link), 10px for the button, 12px for nodes, 18px for the containers that hold them (canvases and bento cells). Containers are always rounder than what they contain. Every border is 1px hairline except output nodes (2px orange) and the "next" node (1px dashed pewter). Edges are 1.5px strokes routed orthogonally through the gutters with 8px rounded elbows; ports are 3.5px-radius circles in node white with a pewter stroke. The only circles in the system are ports, flow tokens and the AI kind marker.

## Components

### Buttons
Solid, compact, decisive; there is one.
- **Shape:** 10px corners, 48px tall, 22px inline padding, 600 weight at 16px, an inline 18px stroke icon.
- **Primary:** graphite ink on canvas grey text.
- **Hover / Active:** background turns signal orange with `on-signal` text (160ms); press scales to 0.97 with the ease-out curve.
- **Text link:** the secondary action is a 600-weight underlined link, not a ghost button. Underlines are 1.5px at 35% current color, offset 0.22em, going solid on hover.

### Language switch
A 32px mono chip ("EN"/"ES") in node white with a hairline border and 8px corners; hover darkens the border to pewter, press scales to 0.97.

### Navigation
Sticky 64px header on canvas grey: brand (a 12px orange square with 3px corners plus the name at 700) on the left, five 15px slate links with 24px gaps pushed right, then the language switch. Links go to graphite ink on hover. Below 720px the links hide.

### Node (signature)
The unit of the whole world.
- **Anatomy:** a mono kind label with its square, a 14px/650 name, a 12px pewter subtext; 10px x 12px padding, 4px internal gap, 12px corners, hairline border, node-lift shadow.
- **AI node:** signal-wash background, border mixing 70% orange into the hairline, circle kind marker.
- **Output node:** 2px signal-orange border, name at 17px. Used where a flow converges (Finwaise in the graph, the ERP modules and video in the flowchart).
- **Next node:** transparent, no shadow, 1px dashed pewter border, joined by a dashed edge (`4 5`). It points to contact and the 404 reuses it as "node not found".
- **States:** linked nodes darken their border to pewter on hover and scale to 0.98 on press.

### Canvas (signature)
A node-white container with an 18px radius, hairline border and a 22px dot grid (1.2px dots in grid-dot). It holds an SVG edge layer, ports, an optional flow-token group, absolutely positioned nodes, and a mono caption pinned bottom-left. Edges default to pewter at 50% opacity; AI edges are orange at 85%.
- **Focus dimming:** hovering or focusing any node lights it, its direct neighbours and the edges between them; unlit nodes fall to 30% opacity, unlit edges to 12%, lit edges go to full opacity at 2px, and flow tokens fade out (200ms).
- **Flow tokens:** 4.5px-radius circles in a kind color travel along composed edge paths with SVG `animateMotion` (3.6-6s loops, staggered starts), always toward an output. Under `prefers-reduced-motion: reduce` the token group is hidden, not paused.

### Bento cells
- **Corner Style:** 18px.
- **Background:** node white with a hairline border; the AI cell is inverted (graphite ink background and border, canvas-grey text, muted text by mixing 62-78% of the background color); one AI-related cell may take the signal wash with a 30% orange border.
- **Shadow Strategy:** none (see Elevation).
- **Internal Padding:** 24px, 12px gap between head, prose and capability list.
- **Head:** the cell's kind square (10px) before the title, through the `k-head` pattern used for every section-level heading that belongs to a kind.

### Capability list (category → capability rows)
A definition list pinned to the bottom of each cell, separated by a hairline: a mono 12px pewter term column (11ch, 13ch in the AI cell) and a 14.5px ink value column. Terms are categories of capability ("models", "agents", "cloud", "e2e"); values name the tools inside that category.

### Project registry
Groups headed by a kind-square title over a 1px graphite rule. Each project is a two-column row: name (18px/650, with an 11px external-link arrow that nudges 2px up-right on hover) and a mono date on the right; description in slate below (max 64ch); a mono 12.5px stack line joined by middle dots. Rows are separated by hairlines; compact rows drop the stack line.

### Experience and facts
A mono date column beside the role (24px/700), org line in slate, and points marked by an 8px outlined square (1.5px pewter stroke, 2px corners) with key facts in 650 ink. Below, a facts row of definition lists with mono terms over a hairline.

### Contact ("next node")
The closing headline completes the graph ("Next node: your team"), with the team phrase in signal-orange text. Then a lede, the email as a large 700-weight link (clamp(22px, 3.2vw, 36px)) that turns orange-text on hover, and a row of 600-weight links.

### Involvement list
In the Finwaise case, each contribution is marked by a 9px kind square in its own kind color, so the case reads as nodes of the same graph.

## Do's and Don'ts

### Do:
- **Do** give every skill, project group and graph node a kind (base, build, ops, ai) and show it with the 9-10px square; make the AI kind a circle.
- **Do** keep orange for AI, convergence outputs, the primary button hover and at most a phrase of emphasised text per view.
- **Do** route canvas edges orthogonally through the gutters with 8px rounded elbows and a port where they meet a node.
- **Do** keep the dot grid inside canvases; the page background stays plain canvas grey.
- **Do** present tools as category → capability rows in a definition list, never as a loose cloud of single tool names.
- **Do** hide flow tokens under reduced motion and keep the static graph complete without them.
- **Do** turn every canvas into a vertical node list with a left connector on phones.
- **Do** build spacing from the 8px unit and keep containers rounder than their contents (18 > 12 > 10 > 8 > 2).

### Don't:
- **Don't** put a mono eyebrow or kicker above any heading; a heading carries only its kind square.
- **Don't** add shadows to anything but nodes.
- **Don't** use orange on a non-AI element that is not a convergence output.
- **Don't** return to the transit-map/timeline world or a dark neon card grid; dark mode is the same canvas at night.
- **Don't** set Geist Mono on prose, headings or buttons.
- **Don't** headline a single tool (an automation product, a model vendor) as a skill; it belongs inside a capability category.
