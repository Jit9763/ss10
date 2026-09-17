# -*- coding: utf-8 -*-
"""
Generator for Chapter 4: दो चरों वाले रैखिक समीकरण (Linear Equations in Two Variables)
Converts Chapter 4 to the EXACT Chapter 2 Master Standard:
- Sticky Black Action Bar with 9 Projector Buttons (W+, W-, A+, A-, B+, B-, Copy, Print, Home)
- Container #contentToCopy with 26pt 900-weight Noto Sans Devanagari typography
- Rich color-coded step boxes & yellow/green answer highlights
- High-contrast SVG coordinate plane graphs with DARK grid lines and BOLD NUMBERS on X & Y axes
- Simulator 5 Canvas with DARK grid lines, DARK axes, and BOLD NUMBERS on X & Y axes
- 100% verified NCERT Ex 4.1 and Ex 4.2 solutions
"""

def generate_svg_graph(line_name, points, equation_label, color="#2563eb", x_range=(-6, 6), y_range=(-4, 5)):
    """
    Generates a high-contrast SVG Cartesian graph:
    - ViewBox: 640 x 420
    - Origin at (320, 220), 1 unit = 36px
    - Dark grid lines (#94a3b8)
    - Solid black axes (#000000)
    - Black bold numbers on X and Y axes
    - Bold colored line with plotted points
    """
    w, h = 640, 420
    ox, oy = 320, 220
    scale = 36

    svg = []
    svg.append(f'<div style="margin:25px auto; max-width:650px; text-align:center;">')
    svg.append(f'<div style="font-size:20pt; font-weight:900; color:#1e3a8a; margin-bottom:10px;">📈 आलेखीय निरूपण: ${equation_label}$</div>')
    svg.append(f'<svg width="100%" height="420" viewBox="0 0 {w} {h}" style="background:#ffffff; border:4px solid #cbd5e1; border-radius:18px; box-shadow:0 8px 25px rgba(0,0,0,0.08); display:block; margin:0 auto;">')
    svg.append('  <defs>')
    svg.append('    <marker id="arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#000000"/></marker>')
    svg.append('  </defs>')

    # 1. Dark Grid Lines
    svg.append('  <!-- Grid Lines -->')
    svg.append('  <g stroke="#94a3b8" stroke-width="1.5" opacity="0.85">')
    # Verticals
    for x in range(x_range[0], x_range[1] + 1):
        px = ox + x * scale
        if 20 <= px <= w - 20:
            svg.append(f'    <line x1="{px}" y1="20" x2="{px}" y2="{h-20}"/>')
    # Horizontals
    for y in range(y_range[0], y_range[1] + 1):
        py = oy - y * scale
        if 20 <= py <= h - 20:
            svg.append(f'    <line x1="20" y1="{py}" x2="{w-20}" y2="{py}"/>')
    svg.append('  </g>')

    # 2. Solid Black Axes
    svg.append('  <!-- Axes -->')
    svg.append(f'  <line x1="20" y1="{oy}" x2="{w-20}" y2="{oy}" stroke="#000000" stroke-width="4.5" marker-end="url(#arr)" marker-start="url(#arr)"/>')
    svg.append(f'  <line x1="{ox}" y1="{h-20}" x2="{ox}" y2="20" stroke="#000000" stroke-width="4.5" marker-end="url(#arr)" marker-start="url(#arr)"/>')

    # Axis Labels X, Y
    svg.append(f'  <text x="{w-16}" y="{oy-8}" font-size="22" font-weight="900" fill="#000000">X</text>')
    svg.append(f'  <text x="10" y="{oy-8}" font-size="22" font-weight="900" fill="#000000">X\'</text>')
    svg.append(f'  <text x="{ox+8}" y="18" font-size="22" font-weight="900" fill="#000000">Y</text>')
    svg.append(f'  <text x="{ox+8}" y="{h-6}" font-size="22" font-weight="900" fill="#000000">Y\'</text>')
    svg.append(f'  <text x="{ox-14}" y="{oy+22}" font-size="18" font-weight="900" fill="#000000">O</text>')

    # 3. Numbers on X and Y Axes
    svg.append('  <!-- X Axis Numbers -->')
    svg.append('  <g font-size="18" font-weight="900" fill="#000000" text-anchor="middle">')
    for x in range(x_range[0], x_range[1] + 1):
        if x == 0: continue
        px = ox + x * scale
        if 30 <= px <= w - 30:
            svg.append(f'    <line x1="{px}" y1="{oy-5}" x2="{px}" y2="{oy+5}" stroke="#000000" stroke-width="2.5"/>')
            svg.append(f'    <text x="{px}" y="{oy+24}">{x}</text>')
    svg.append('  </g>')

    svg.append('  <!-- Y Axis Numbers -->')
    svg.append('  <g font-size="18" font-weight="900" fill="#000000" text-anchor="end">')
    for y in range(y_range[0], y_range[1] + 1):
        if y == 0: continue
        py = oy - y * scale
        if 30 <= py <= h - 30:
            svg.append(f'    <line x1="{ox-5}" y1="{py}" x2="{ox+5}" y2="{py}" stroke="#000000" stroke-width="2.5"/>')
            svg.append(f'    <text x="{ox-8}" y="{py+6}">{y}</text>')
    svg.append('  </g>')

    # 4. Straight Line
    # Calculate two extended endpoints
    p1, p2 = points[0], points[-1]
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if dx == 0:
        # Vertical line x = c
        lx1, ly1 = ox + p1[0]*scale, 25
        lx2, ly2 = ox + p1[0]*scale, h - 25
    else:
        m = dy / dx
        # line equation: y - y1 = m(x - x1) => y = m(x - x1) + y1
        x_min, x_max = x_range[0] - 1, x_range[1] + 1
        y_at_min = m * (x_min - p1[0]) + p1[1]
        y_at_max = m * (x_max - p1[0]) + p1[1]
        lx1, ly1 = ox + x_min * scale, oy - y_at_min * scale
        lx2, ly2 = ox + x_max * scale, oy - y_at_max * scale

    svg.append('  <!-- Plotted Line -->')
    svg.append(f'  <line x1="{lx1}" y1="{ly1}" x2="{lx2}" y2="{ly2}" stroke="{color}" stroke-width="4.5"/>')

    # 5. Plotted Points with Coordinates
    svg.append('  <!-- Points -->')
    for pt in points:
        px = ox + pt[0] * scale
        py = oy - pt[1] * scale
        svg.append(f'  <circle cx="{px}" cy="{py}" r="7" fill="#dc2626" stroke="#ffffff" stroke-width="2.5"/>')
        label = f'({pt[0]}, {pt[1]})'
        svg.append(f'  <text x="{px+10}" y="{py-10}" font-size="18" font-weight="900" fill="#b91c1c">{label}</text>')

    svg.append('</svg>')
    svg.append(f'<p style="font-size:16pt; font-weight:800; color:#334155; margin-top:8px;">चित्र: समीकरण ${equation_label}$ का आलेख (सरल रेखा)</p>')
    svg.append('</div>')

    return '\n'.join(svg)

print("SVG Graph Generator ready!")
