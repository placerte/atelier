# Atelier

Atelier is the theme and visual identity system for `placerte`. It combines editorial typography, technical diagrams and annotations, and restrained geometric forms under a direction called **Technical Editorial Modernism**.

The system is designed to remain recognizable across websites, presentations, documents, terminals, and code-oriented interfaces without forcing every medium to use colors in the same way.

![Atelier technical editorial brand moodboard](Technical_Editorial_Brand_Moodboard.png)

## Design language

- **Editorial:** strong hierarchy, asymmetric composition, and deliberate whitespace
- **Technical:** grids, schematics, labels, annotations, and data-focused layouts
- **Geometric:** balanced shapes used as structure and emphasis rather than decoration
- **Typography:** IBM Plex Sans for headings and body text; IBM Plex Mono for code and technical details

## Master palette

The five identity anchors come from Omoro's [Hipster palette](https://www.omoro.io/palettes/hipster) and remain unchanged in Atelier.

| Color | HEX | Role |
|---|---|---|
| Flannel Red | `#A33B2C` | Rust/red accent |
| Mustard | `#C9962B` | Warm yellow accent |
| Forest Green | `#2F4A35` | Earthy green accent |
| Rinsed Denim | `#3B5068` | Muted blue accent |
| Faded Cream | `#EDE3CC` | Light neutral and canvas |

Atelier also uses derived Charcoal (`#191F22`) as its primary dark background. It is a supporting neutral, not part of the original five-color palette.

## Theme families

Atelier separates brand presentation from terminal behavior:

| Theme | Purpose |
|---|---|
| **Original** | Immutable master/reference palette |
| **Brand Light** | Cream canvas with original colors as accents |
| **Brand Dark** | Charcoal canvas with brighter derived accents |
| **Brand Darker** | Charcoal canvas with restrained original accents |
| **Terminal Dark** | ANSI-aware dark terminal palette |
| **Terminal Light** | ANSI-aware light terminal palette; still in development |

This distinction is intentional: brand palettes prioritize identity and composition, while terminal palettes must also provide readable ANSI colors and predictable software behavior.

![Atelier Terminal Dark technical editorial board](Terminal_Dark_Technical_Editorial_Board.png)

## Project status

Atelier is currently a working design specification. The master palette and overall direction are established, while several implementation details still need validation:

- verify the saved Terminal Dark values against their source theme;
- finalize and contrast-test the Terminal Light ANSI palette;
- test colored text and interactive states across brand variants; and
- turn the conceptual tokens into platform-specific themes and templates.

See [atelier-theme-system.md](atelier-theme-system.md) for the complete specification, current token model, accessibility cautions, and open decisions.

## Repository contents

```text
.
├── atelier-theme-system.md
├── Technical_Editorial_Brand_Moodboard.png
├── Terminal_Dark_Technical_Editorial_Board.png
└── AGENTS.md
```

## Guiding rule

One visual identity, multiple purpose-built expressions. Do not conflate original, bright, and dimmed colors—or treat a dark brand layout as though it were an ANSI terminal palette.

## License

Released under the [MIT License](LICENSE).
