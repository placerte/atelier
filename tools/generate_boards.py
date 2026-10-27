#!/usr/bin/env python3
"""Generate deterministic Atelier SVG reference boards from shared tokens."""

from __future__ import annotations

import json
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "boards"
TOKENS = json.loads((ROOT / "design-tokens.json").read_text())
MASTER = TOKENS["master"]
NEUTRAL = TOKENS["neutral"]
DERIVED = TOKENS["derived"]
W, H = 1536, 1024


def text(x, y, value, size=24, fill="#191F22", weight=400, family="sans", anchor="start", opacity=1):
    font = "IBM Plex Mono, monospace" if family == "mono" else "IBM Plex Sans, sans-serif"
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" font-family="{font}" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" opacity="{opacity}" xml:space="preserve">'
        f'{escape(value)}</text>'
    )


def rect(x, y, w, h, fill, stroke="none", sw=0, rx=0, opacity=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>'


def line(x1, y1, x2, y2, stroke, sw=2, dash=""):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{extra}/>'


def circle(cx, cy, r, fill, stroke="none", sw=0):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def svg(title, description, body, background):
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title>',
        f'<desc id="desc">{escape(description)}</desc>',
        rect(0, 0, W, H, background),
        *body,
        "</svg>",
        "",
    ])


def header(name, subtitle, fg, rule):
    return [
        text(72, 78, "ATELIER / VISUAL SYSTEM", 18, rule, 600, "mono"),
        text(72, 153, name, 54, fg, 600),
        text(72, 196, subtitle, 21, fg, 400, opacity=0.72),
        line(72, 228, 1464, 228, rule, 2),
        text(1464, 78, "01—08 / 2026", 16, rule, 500, "mono", "end"),
    ]


def swatch_row(colors, labels, y, fg, border):
    parts = []
    sw = 244
    for index, (color, label) in enumerate(zip(colors, labels)):
        x = 72 + index * 278
        parts += [rect(x, y, sw, 112, color, border, 1), text(x, y + 142, label.upper(), 14, fg, 600, "mono"), text(x, y + 166, color, 16, fg, 400, "mono")]
    return parts


def master_board():
    bg, fg = NEUTRAL["paper"], NEUTRAL["charcoal"]
    colors = list(MASTER.values())
    labels = ["Flannel Red", "Mustard", "Forest Green", "Rinsed Denim", "Faded Cream"]
    body = header("Original / Master Palette", "Five immutable identity anchors from Omoro’s Hipster palette.", fg, MASTER["red"])
    body += swatch_row(colors, labels, 292, fg, "#B9AE99")
    body += [
        text(72, 554, "SYSTEM PRINCIPLE", 15, MASTER["red"], 600, "mono"),
        text(72, 612, "One identity.", 44, fg, 600),
        text(72, 660, "Purpose-built expressions.", 44, fg, 400),
        rect(878, 520, 586, 340, MASTER["cream"], fg, 2),
        line(928, 570, 1414, 570, MASTER["red"], 10),
        line(928, 614, 1320, 614, MASTER["yellow"], 10),
        line(928, 658, 1380, 658, MASTER["green"], 10),
        line(928, 702, 1260, 702, MASTER["blue"], 10),
        text(928, 790, "SOURCE COLORS DO NOT DRIFT", 17, fg, 600, "mono"),
        text(72, 952, "TECHNICAL EDITORIAL MODERNISM", 15, fg, 500, "mono"),
    ]
    return svg("Atelier Original master palette", "Exact source colors and core design principle.", body, bg)


def brand_board(name, background, foreground, accents, mode, number):
    rule = accents[0]
    body = header(name, "Editorial hierarchy / technical annotation / geometric restraint", foreground, rule)
    body[4] = text(1464, 78, f"{number:02d}—08 / 2026", 16, rule, 500, "mono", "end")
    body += [
        text(72, 292, "FIELD NOTE  /  027", 15, accents[1], 600, "mono"),
        text(72, 354, "Structure makes", 58, foreground, 600),
        text(72, 418, "the system visible.", 58, foreground, 400),
        text(76, 478, "A visual language for interfaces, documents, and ideas.", 20, foreground, 400, opacity=0.72),
        rect(72, 552, 620, 252, background, accents[2], 2),
        text(104, 600, "COMPOSITION / 01", 14, accents[2], 600, "mono"),
        line(104, 635, 650, 635, accents[2], 1, "6 7"),
        text(104, 690, "Clear hierarchy", 30, foreground, 600),
        text(104, 733, "Measured contrast", 30, foreground, 400),
        text(104, 776, "Repeatable geometry", 30, foreground, 400),
        rect(818, 286, 646, 518, accents[3]),
        rect(866, 334, 248, 194, accents[0]),
        circle(1288, 432, 112, accents[1]),
        rect(866, 578, 518, 34, accents[2]),
        rect(866, 646, 430, 18, foreground, opacity=0.78),
        rect(866, 686, 350, 18, foreground, opacity=0.48),
        text(1464, 874, mode.upper(), 16, foreground, 600, "mono", "end"),
        line(72, 918, 1464, 918, rule, 2),
        text(72, 958, "IBM PLEX SANS", 15, foreground, 500, "mono"),
        text(1464, 958, "IBM PLEX MONO / LABELS + DATA", 15, foreground, 500, "mono", "end"),
    ]
    return svg(f"Atelier {name}", f"Exact-color {name} reference board.", body, background)


def terminal_chrome(title, subtitle, palette, number):
    bg, fg = palette["background"], palette["foreground"]
    border = palette["bright"][0]
    body = header(title, subtitle, fg, palette["bright"][1])
    body[4] = text(1464, 78, f"{number:02d}—08 / {palette['status'].upper()}", 16, palette["bright"][1], 500, "mono", "end")
    body += [rect(72, 278, 1392, 628, bg, border, 2, 10), rect(72, 278, 1392, 52, border, opacity=0.18)]
    body += [circle(104, 304, 7, palette["normal"][1]), circle(130, 304, 7, palette["normal"][3]), circle(156, 304, 7, palette["normal"][2]), text(768, 310, "atelier — 120×34", 14, fg, 500, "mono", "middle", 0.7)]
    return body


def terminal_shell(title, palette, number):
    bg, fg = palette["background"], palette["foreground"]
    n, b = palette["normal"], palette["bright"]
    body = terminal_chrome(title, "ANSI palette / shell and diagnostic output", palette, number)
    rows = [
        ("$", "atelier inspect --theme current", b[2]),
        ("→", f"profile      {title.replace('Terminal / ', '')}", b[4]),
        ("→", f"status       {palette['status']}", b[3]),
        ("✓", "tokens       loaded from design-tokens.json", b[2]),
        ("✓", "foreground   readable on canvas", b[6]),
        ("!", "contrast     review semantic color pairs", b[1]),
    ]
    y = 384
    for prompt, value, color in rows:
        body += [text(112, y, prompt, 19, color, 600, "mono"), text(152, y, value, 19, fg, 400, "mono")]
        y += 48
    body += [text(112, 704, "NORMAL", 14, fg, 600, "mono", opacity=0.65), text(112, 820, "BRIGHT", 14, fg, 600, "mono", opacity=0.65)]
    for row, colors in enumerate((n, b)):
        for i, color in enumerate(colors):
            body += [rect(238 + i * 142, 672 + row * 116, 108, 66, color, fg, 1), text(292 + i * 142, 764 + row * 116, f"{i + row * 8:02d}", 13, fg, 500, "mono", "middle")]
    return svg(title, f"Exact-color shell example for {title}.", body, bg)


def terminal_code(title, palette, number):
    bg, fg = palette["background"], palette["foreground"]
    b = palette["bright"]
    body = terminal_chrome(title, "ANSI palette / code and system monitor", palette, number)
    body += [line(884, 330, 884, 906, b[0], 1), text(112, 374, "theme.py", 15, b[4], 600, "mono")]
    code = [
        [("def", b[5]), (" build_palette", b[4]), ("(tokens):", fg)],
        [("    background", fg), (" = ", b[0]), ('tokens["charcoal"]', b[3])],
        [("    accents", fg), (" = ", b[0]), ("select", b[6]), ("(tokens)", fg)],
        [("    return", b[5]), (" Palette", b[4]), ("(background, accents)", fg)],
    ]
    y = 430
    for line_no, spans in enumerate(code, 1):
        body.append(text(112, y, str(line_no), 17, b[0], 400, "mono", "end"))
        x = 140
        for value, color in spans:
            body.append(text(x, y, value, 18, color, 400, "mono"))
            x += len(value) * 10.8
        y += 48
    body += [text(934, 374, "SYSTEM / LIVE", 15, b[2], 600, "mono")]
    metrics = [("CPU", 0.42, b[2]), ("MEM", 0.67, b[4]), ("IO", 0.28, b[6]), ("NET", 0.54, b[3])]
    y = 442
    for label, value, color in metrics:
        body += [text(934, y, label, 16, fg, 600, "mono"), rect(1006, y - 18, 350, 14, b[0], opacity=0.25), rect(1006, y - 18, 350 * value, 14, color), text(1418, y, f"{int(value * 100):02d}%", 15, fg, 500, "mono", "end")]
        y += 70
    body += [line(112, 688, 824, 688, b[0], 1), text(112, 734, "$", 18, b[2], 600, "mono"), text(144, 734, "git status --short", 18, fg, 400, "mono"), text(112, 786, "M", 18, b[3], 600, "mono"), text(144, 786, "design-tokens.json", 18, fg, 400, "mono"), text(112, 838, "?", 18, b[1], 600, "mono"), text(144, 838, "assets/boards/", 18, fg, 400, "mono")]
    return svg(title, f"Exact-color code and monitor example for {title}.", body, bg)


def write(name, content):
    (OUT / name).write_text(content)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    write("atelier-original.svg", master_board())
    write("atelier-brand-light.svg", brand_board("Brand / Light", MASTER["cream"], NEUTRAL["charcoal"], [MASTER["red"], MASTER["yellow"], MASTER["green"], MASTER["blue"]], "cream canvas / original accents", 2))
    write("atelier-brand-dark.svg", brand_board("Brand / Dark", NEUTRAL["charcoal"], MASTER["cream"], [DERIVED["red_bright"], DERIVED["yellow_bright"], DERIVED["green_bright"], DERIVED["blue_bright"]], "charcoal canvas / bright accents", 3))
    write("atelier-brand-darker.svg", brand_board("Brand / Darker", NEUTRAL["charcoal"], MASTER["cream"], [MASTER["red"], MASTER["yellow"], MASTER["green"], MASTER["blue"]], "charcoal canvas / original accents", 4))
    write("atelier-terminal-dark-shell.svg", terminal_shell("Terminal / Dark", TOKENS["terminal_dark"], 5))
    write("atelier-terminal-dark-code.svg", terminal_code("Terminal / Dark", TOKENS["terminal_dark"], 6))
    write("atelier-terminal-light-shell.svg", terminal_shell("Terminal / Light", TOKENS["terminal_light"], 7))
    write("atelier-terminal-light-code.svg", terminal_code("Terminal / Light", TOKENS["terminal_light"], 8))


if __name__ == "__main__":
    main()
