import os
import random

OUTPUT_DIR = "images"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def write_svg(filename, content, width=800, height=400):
    with open(os.path.join(OUTPUT_DIR, filename), "w") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
        f.write('<defs>')
        # Glow Filter
        f.write('<filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4" result="blur" /><feComposite in="SourceGraphic" in2="blur" operator="over" /></filter>')
        # Gradients
        f.write('<linearGradient id="binaryGrad" x1="0" x2="0" y1="0" y2="1"><stop offset="0%" stop-color="#3b82f6" stop-opacity="0.3"/><stop offset="100%" stop-color="#3b82f6" stop-opacity="0.05"/></linearGradient>')
        f.write('<linearGradient id="skepsisGrad" x1="0" x2="0" y1="0" y2="1"><stop offset="0%" stop-color="#bef264" stop-opacity="0.3"/><stop offset="100%" stop-color="#bef264" stop-opacity="0.05"/></linearGradient>')
        f.write('</defs>')
        f.write('<style>text { font-family: Inter, system-ui, sans-serif; }</style>')
        f.write(content)
        f.write('</svg>')
    print(f"Generated {filename}")

# Colors
COLOR_BG = "#09090b"
COLOR_PANEL = "#18181b"
COLOR_GRID = "#27272a"
COLOR_TEXT = "#a1a1aa"
COLOR_TEXT_BRIGHT = "#ffffff"
COLOR_BINARY = "#3b82f6"
COLOR_SKEPSIS = "#bef264"

def gen_side_by_side_chart():
    svg = f'<rect width="800" height="400" fill="{COLOR_BG}" />'
    
    # --- LEFT PANEL: BINARY ---
    svg += f'<g transform="translate(20, 20)">'
    # Panel Bg
    svg += f'<rect width="370" height="360" rx="12" fill="{COLOR_PANEL}" stroke="{COLOR_GRID}" />'
    svg += f'<text x="185" y="40" text-anchor="middle" fill="{COLOR_TEXT_BRIGHT}" font-size="18" font-weight="bold">Binary Market</text>'
    
    # Grid
    for i in range(1, 6):
        y = 80 + i * 40
        svg += f'<line x1="40" y1="{y}" x2="330" y2="{y}" stroke="{COLOR_GRID}" stroke-width="1" />'
    
    # Binary Zone (> $97k)
    # Let's say bottom is $95k (y=280), top is $100k (y=80). Scale: 40px per $1k.
    # $97k is at y=200. Zone is everything above y=200.
    svg += f'<rect x="40" y="80" width="290" height="120" fill="url(#binaryGrad)" />'
    svg += f'<line x1="40" y1="200" x2="330" y2="200" stroke="{COLOR_BINARY}" stroke-width="2" stroke-dasharray="4,4" />'
    svg += f'<text x="50" y="190" fill="{COLOR_BINARY}" font-size="12" font-weight="bold">THRESHOLD > $97k</text>'
    
    # Price Line (Start $95k -> End $98.5k)
    # Start: x=40, y=280 ($95k)
    # End: x=330, y=140 ($98.5k)
    points = "40,280 100,270 160,220 220,180 280,160 330,140"
    svg += f'<polyline points="{points}" fill="none" stroke="#ffffff" stroke-width="3" />'
    svg += f'<circle cx="330" cy="140" r="5" fill="{COLOR_TEXT_BRIGHT}" />'
    
    # Labels
    svg += f'<text x="30" y="285" text-anchor="end" fill="{COLOR_TEXT}" font-size="10">$95k</text>'
    svg += f'<text x="30" y="205" text-anchor="end" fill="{COLOR_TEXT}" font-size="10">$97k</text>'
    svg += f'<text x="30" y="145" text-anchor="end" fill="{COLOR_TEXT}" font-size="10">$98.5k</text>'

    # Badge
    svg += f'<rect x="135" y="300" width="100" height="36" rx="18" fill="{COLOR_BINARY}" fill-opacity="0.2" stroke="{COLOR_BINARY}" />'
    svg += f'<text x="185" y="324" text-anchor="middle" fill="{COLOR_BINARY}" font-size="16" font-weight="bold">2x Payout</text>'
    svg += f'</g>'


    # --- RIGHT PANEL: SKEPSIS ---
    svg += f'<g transform="translate(410, 20)">'
    # Panel Bg
    svg += f'<rect width="370" height="360" rx="12" fill="{COLOR_PANEL}" stroke="{COLOR_GRID}" />'
    svg += f'<text x="185" y="40" text-anchor="middle" fill="{COLOR_TEXT_BRIGHT}" font-size="18" font-weight="bold">Skepsis</text>'
    
    # Grid
    for i in range(1, 6):
        y = 80 + i * 40
        svg += f'<line x1="40" y1="{y}" x2="330" y2="{y}" stroke="{COLOR_GRID}" stroke-width="1" />'
        
    # Skepsis Zone ($98k - $99k)
    # $98k is y=160. $99k is y=120.
    svg += f'<rect x="40" y="120" width="290" height="40" fill="{COLOR_SKEPSIS}" fill-opacity="0.2" stroke="{COLOR_SKEPSIS}" stroke-width="2" />'
    svg += f'<text x="50" y="110" fill="{COLOR_SKEPSIS}" font-size="12" font-weight="bold">TARGET $98k - $99k</text>'
    
    # Price Line (Same as left)
    points = "40,280 100,270 160,220 220,180 280,160 330,140"
    svg += f'<polyline points="{points}" fill="none" stroke="#ffffff" stroke-width="3" />'
    svg += f'<circle cx="330" cy="140" r="5" fill="{COLOR_SKEPSIS}" stroke="#ffffff" stroke-width="2" />'
    
    # Labels
    svg += f'<text x="30" y="285" text-anchor="end" fill="{COLOR_TEXT}" font-size="10">$95k</text>'
    svg += f'<text x="30" y="165" text-anchor="end" fill="{COLOR_TEXT}" font-size="10">$98k</text>'
    svg += f'<text x="30" y="125" text-anchor="end" fill="{COLOR_TEXT}" font-size="10">$99k</text>'

    # Badge
    svg += f'<rect x="135" y="300" width="100" height="36" rx="18" fill="{COLOR_SKEPSIS}" filter="url(#glow)" />'
    svg += f'<rect x="135" y="300" width="100" height="36" rx="18" fill="{COLOR_SKEPSIS}" />'
    svg += f'<text x="185" y="324" text-anchor="middle" fill="#000000" font-size="16" font-weight="bold">10x Payout</text>'
    svg += f'</g>'

    write_svg("precision-chart-v2.svg", svg)

if __name__ == "__main__":
    gen_side_by_side_chart()
