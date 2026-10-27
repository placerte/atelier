# AGENTS.md

## Project overview

Atelier is a design-system and branding repository for the `placerte` identity. Its direction is **Technical Editorial Modernism**, combining editorial typography, technical diagrams and annotations, and restrained geometric forms.

The repository is currently documentation- and asset-first. There is no application, package manifest, build system, or automated test suite yet.

## Source of truth

- `atelier-theme-system.md` is the current design specification.
- `README.md` is the public project introduction and should stay concise.
- `design-tokens.json` is the machine-readable palette used to generate exact-color reference boards.
- `assets/boards/` contains generated SVG reference boards; `tools/generate_boards.py` is their source generator.
- `references/concepts/` contains earlier GPT-generated directional images. They are historical concepts, not authoritative color references.
- `llm/` contains supporting workflow notes. It is intentionally ignored by Git; do not assume edits there will be committed.

When prose, examples, and visual assets disagree, report the conflict rather than silently choosing a new design rule.

## Design invariants

Preserve these five original Omoro Hipster source colors exactly unless the user explicitly changes the master palette:

| Token | HEX |
|---|---|
| Flannel Red | `#A33B2C` |
| Mustard | `#C9962B` |
| Forest Green | `#2F4A35` |
| Rinsed Denim | `#3B5068` |
| Faded Cream | `#EDE3CC` |

`#191F22` is the derived charcoal neutral; it is not one of the five source colors.

Keep the six named palettes distinct:

1. Atelier — Original
2. Atelier — Brand Light
3. Atelier — Brand Dark
4. Atelier — Brand Darker
5. Atelier — Terminal Dark
6. Atelier — Terminal Light

Do not conflate brand palettes with ANSI terminal palettes. Original, current bright, and proposed refined colors must be labeled accurately. In particular, the Terminal Light ANSI mapping and several brighter refinements are still proposals or TODOs, not finalized facts.

Use IBM Plex Sans for headings and body copy and IBM Plex Mono for code, labels, annotations, and technical details unless a deliverable has an explicit exception.

## Working practices

- Read `atelier-theme-system.md` before changing colors, names, typography, or palette roles.
- Make the smallest coherent change and preserve the distinction between confirmed values, proposals, and open decisions.
- Keep documentation plain Markdown with compact tables and fenced examples where they improve precision.
- Update related prose and token examples together so the specification does not contradict itself.
- After changing `design-tokens.json` or the board generator, run `python tools/generate_boards.py` and include the regenerated SVGs.
- Do not overwrite or rename source images without explicit approval. Check references first.
- When detailed image inspection is needed, follow `llm/image_ingestion_toolbox.md`: record provenance and observations in a sidecar Markdown file and distinguish observation from interpretation.
- Record important design decisions by appending to `llm/decision_log.md`; never rewrite earlier entries. Remember that `llm/` is Git-ignored, so also reflect durable public decisions in the tracked specification.
- If Typst sources are introduced, follow `llm/typst_toolbox.md`: default to US Letter, compile without warnings, and visually inspect affected PDF pages.

## Validation

There are currently no automated checks. For documentation changes:

1. Search for affected palette names, tokens, and HEX values across the repository.
2. Check Markdown structure, tables, links, and fenced examples.
3. Verify that statements about unfinished palettes remain qualified as proposals or TODOs.
4. Inspect relevant images when a change depends on exact layout, color, geometry, or typography.
5. Run `python tools/generate_boards.py`, then `git diff --exit-code -- assets/boards` to confirm generated boards are current.

If a build or test toolchain is added later, document the exact commands here and in the README.

## Git and hosted-forge safety

- Preserve unrelated work in the working tree.
- Do not commit, push, create or close issues, publish releases, or otherwise make outward-facing changes unless the user asks.
- Do not treat ignored `llm/` files as part of a commit without discussing whether they should remain ignored.
- Releases are explicit user-requested work, never an automatic follow-up to a documentation or asset change.
