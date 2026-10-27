# Atelier Theme System

**Status:** Working design specification — 27 October 2026  
**Identity:** `placerte` / Technical Editorial Modernism  
**Purpose:** Consistent visual identity across website, presentations, documents, and terminal environments.
**Palette provenance:** Omoro’s **Hipster** palette is the source of the five original HEX colors. **Atelier** is the name of this derived design system; the source palette is credited, not renamed retroactively.

## 1. Design direction

The selected direction is **Technical Editorial Modernism**, combining four earlier visual approaches:

- **02 Editorial:** Strong typography, asymmetric compositions, editorial hierarchy.
- **03 Technical:** Schematics, annotations, grids, data visualization, engineering details.
- **04 Modern Geometric:** Geometric accents, section covers, bold but controlled shapes.
- **06 Hybrid:** A coherent combination of the above for websites and presentations.

**Geometric emphasis:** Balanced — recognizable, not overwhelming.  
**Typography:** **IBM Plex Sans** for headings and body text; **IBM Plex Mono** for labels, annotations, technical details, and code.

## 2. Theme architecture

Six named palettes, **including the master**:

| Name | Canvas | Color strategy | Intended use |
|---|---|---|---|
| **Atelier — Original** | Not applicable | Original five colors, unchanged | Master/reference palette |
| **Atelier — Brand Light** | Cream | Original colors as accents | Website, slides, documents on light canvas |
| **Atelier — Brand Dark** | Charcoal | Brighter, more legible derived accents | Website, slides, documents on dark canvas |
| **Atelier — Brand Darker** | Charcoal | Original colors as accents | Restrained, earthy dark website/slides |
| **Atelier — Terminal Dark** | Charcoal | ANSI-specific normal and bright colors | Dark terminal / code interfaces |
| **Atelier — Terminal Light** | Cream | ANSI colors adapted for light background | Light terminal / code interfaces |

**Key distinction:** Brand palettes prioritize visual identity; terminal palettes prioritize legibility and ANSI behavior. They share the master palette but do **not** need identical color assignments.

## 3. Original master palette — fixed source colors

**Source:** Omoro / Hipster (https://www.omoro.io/palettes/hipster). The Atelier master retains the five established HEX values unchanged.

These five colors are the **identity anchors** and should not be silently modified.

| Color name | HEX | Role |
|---|---|---|
| Flannel Red | `#A33B2C` | Rust/red accent |
| Mustard | `#C9962B` | Warm yellow accent |
| Forest Green | `#2F4A35` | Earthy green accent |
| Rinsed Denim | `#3B5068` | Muted blue accent |
| Faded Cream | `#EDE3CC` | Light neutral / canvas |

**Additional neutral (derived):** Charcoal `#191F22` — dark background, not one of the five original colors.

## 4. Terminal Dark — ANSI palette

The initial eight-color ANSI palette combines the original brand colors with derived black, magenta, and cyan. The brighter row is intended to improve contrast on charcoal.

| ANSI slot | Normal (0–7) | Bright (8–15), current Aether example | Optional brighter refinement* |
|---|---|---|---|
| Black | `#191F22` | `#81888C` | Keep `#81888C` |
| Red | `#A33B2C` | `#DE715F` | Keep `#DE715F` |
| Green | `#2F4A35` | `#729078` | `#8BA891` |
| Yellow | `#C9962B` | `#FFD470` | Keep `#FFD470` |
| Blue | `#3B5068` | `#7289A3` | `#91A9C4` |
| Magenta | `#87516D` | `#AD7491` | `#C18BA9` |
| Cyan | `#3F7777` | `#578F8F` | `#79B1AF` |
| White | `#EDE3CC` | `#FFFFF2` | Keep `#FFFFF2` |

**Suggested foreground:** `#EDE3CC`  
**Suggested background:** `#191F22`

\*The refinements are **proposals**, not confirmed Aether settings. The current Aether values above were read from the earlier discussion/screenshot and should be verified against the saved theme before implementation.

### Why normal and bright colors differ

- **Normal ANSI colors** preserve the muted personality of the master palette.
- **Bright ANSI colors** are easier to read on dark backgrounds.
- Some terminal programs use *normal* ANSI colors for foreground text. Very dark green `#2F4A35` and denim `#3B5068` on charcoal may therefore be difficult to read.
- If everyday readability suffers, move the **normal ANSI foreground colors** toward the brighter versions while keeping the original five colors as independent brand tokens.

## 5. Terminal Light — concept

**Background:** `#EDE3CC` (cream).  
**Foreground:** `#191F22` (charcoal).

Use darker colors derived from the original palette for readable text on cream. The complete 16-color ANSI mapping **has not yet been finalized or contrast-tested**. Do not assume that Terminal Dark's bright row can be reused unchanged on cream.

## 6. Brand Light — concept

- **Background:** `#EDE3CC`.
- **Primary text:** `#191F22`.
- **Accents:** Original Flannel Red, Mustard, Forest Green, and Rinsed Denim.
- **Mood:** Warm, editorial, technical, restrained.
- **Usage:** Default light website, presentations, reports, and documents.

Original colors can be used for headlines, large shapes, diagrams, and accent blocks, subject to contrast checks for small text.

## 7. Brand Dark — concept

- **Background:** `#191F22`.
- **Primary text:** `#EDE3CC`.
- **Accents:** Brighter derived variants from Terminal Dark, rather than the original dark hues.
- **Mood:** Energetic, readable, still earthy.
- **Suggested accent set (working):** Red `#DE715F`, Green `#8BA891`, Yellow `#FFD470`, Blue `#91A9C4`, Magenta `#C18BA9`, Cyan `#79B1AF`.

These brighter accents were discussed as a proposed refinement. They are **not** all confirmed as the current Aether bright ANSI values.

## 8. Brand Darker — concept

- **Background:** `#191F22`.
- **Primary text:** `#EDE3CC`.
- **Accents:** **Original master colors, unchanged**: `#A33B2C`, `#C9962B`, `#2F4A35`, `#3B5068`.
- **Mood:** Dark, understated, earthy, close to the original palette's character.
- **Usage:** Dark visual storytelling, large geometric forms, background blocks, editorial accents.

**Accessibility caution:** Forest Green and Rinsed Denim are too dark for many small-text applications on charcoal. Use cream for primary text; reserve those darker original hues for larger decorative areas, or explicitly check contrast.

## 9. Recommended token model

Keep the original palette immutable and derive application-specific roles from it:

```yaml
atelier:
  master:
    red: '#A33B2C'
    yellow: '#C9962B'
    green: '#2F4A35'
    blue: '#3B5068'
    cream: '#EDE3CC'
  neutral:
    charcoal: '#191F22'
  brand_light:
    background: '#EDE3CC'
    foreground: '#191F22'
    accent_source: master
  brand_dark:
    background: '#191F22'
    foreground: '#EDE3CC'
    accent_source: terminal_dark_bright_refined
  brand_darker:
    background: '#191F22'
    foreground: '#EDE3CC'
    accent_source: master
  terminal_dark:
    background: '#191F22'
    foreground: '#EDE3CC'
    ansi_normal: ['#191F22', '#A33B2C', '#2F4A35', '#C9962B', '#3B5068', '#87516D', '#3F7777', '#EDE3CC']
    ansi_bright_current: ['#81888C', '#DE715F', '#729078', '#FFD470', '#7289A3', '#AD7491', '#578F8F', '#FFFFF2']
  terminal_light:
    background: '#EDE3CC'
    foreground: '#191F22'
    ansi: TBD
```

This is a **conceptual source-of-truth schema**, not an Aether configuration file. No claim is made that Aether natively links these variants to a master or accepts this YAML directly.

### Machine-readable tokens and reference boards

`design-tokens.json` is the machine-readable implementation of the working palette. `tools/generate_boards.py` reads it and deterministically generates the SVG files under `assets/boards/`.

- The master colors remain fixed and unchanged.
- The Terminal Dark boards use the optional brighter refinement shown in the table above; those values still require comparison with the saved Aether theme.
- The Terminal Light boards introduce an explicit **draft candidate** so it can be reviewed visually and contrast-tested. Its mapping is not yet approved as final.
- Generated boards are color-authoritative for the token file that produced them, but they do not by themselves establish accessibility or approve a draft palette.

Regenerate the complete reference set with:

```bash
python tools/generate_boards.py
```

## 10. Aether workflow and open decisions

- Keep separately named Aether Blueprints or theme presets where supported.
- Confirm whether Aether offers automatic master-to-variant inheritance; **do not assume it does**.
- Verify saved **Terminal Dark** ANSI values against Aether before exporting.
- Finalize and contrast-test **Terminal Light**.
- Decide whether Terminal Dark normal colors should remain original or be brightened for routine text readability.
- Contrast-test colored text and interactive elements in Brand Light, Brand Dark, and Brand Darker.
- Apply **IBM Plex Sans / IBM Plex Mono** consistently to the website and slide templates.
- Review the generated Terminal Light candidate and either approve it or revise its values in `design-tokens.json`.

## 11. Naming convention

1. **Atelier — Original** (master)
2. **Atelier — Brand Light**
3. **Atelier — Brand Dark**
4. **Atelier — Brand Darker**
5. **Atelier — Terminal Dark**
6. **Atelier — Terminal Light**

**Guiding rule:** One visual identity, multiple purpose-built expressions. Do not conflate *original*, *bright*, and *dimmed* colors or equate a dark brand layout with a terminal ANSI palette.
