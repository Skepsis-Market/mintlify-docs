import os
import math
import random

OUTPUT_DIR = "images"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def write_svg(filename, content, width=800, height=400):
    with open(os.path.join(OUTPUT_DIR, filename), "w") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
        f.write('<defs>')
        # Glow Filter
        f.write('<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="blur" /><feComposite in="SourceGraphic" in2="blur" operator="over" /></filter>')
        f.write('</defs>')
        f.write('<style>text { font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }</style>')
        
        # Background
        f.write(f'<rect width="100%" height="100%" fill="#0F1115" />')
        
        f.write(content)
        f.write('</svg>')
    print(f"Generated {filename}")

def draw_target(x_center, y_center, color_primary):
    svg = ""
    # Outer rings
    for r, opacity in [(120, 0.1), (90, 0.2), (60, 0.3)]:
        svg += f'<circle cx="{x_center}" cy="{y_center}" r="{r}" fill="none" stroke="{color_primary}" stroke-width="2" stroke-opacity="{opacity}" />'
    
    # Bullseye
    svg += f'<circle cx="{x_center}" cy="{y_center}" r="30" fill="{color_primary}" fill-opacity="0.1" stroke="{color_primary}" stroke-width="2" />'
    
    # Crosshairs
    svg += f'<line x1="{x_center - 140}" y1="{y_center}" x2="{x_center + 140}" y2="{y_center}" stroke="{color_primary}" stroke-width="1" stroke-opacity="0.3" />'
    svg += f'<line x1="{x_center}" y1="{y_center - 140}" x2="{x_center}" y2="{y_center + 140}" stroke="{color_primary}" stroke-width="1" stroke-opacity="0.3" />'
    return svg

def gen_sniper_shotgun_svg():
    svg = ""
    
    # --- LEFT PANEL: SHOTGUN (Binary) ---
    svg += '<g id="shotgun-panel">'
    # Panel Background
    svg += '<rect x="20" y="20" width="370" height="360" rx="12" fill="#1A1D24" stroke="#333" stroke-width="1" />'
    # Title
    svg += '<text x="205" y="60" text-anchor="middle" fill="white" font-size="16" font-weight="bold">Binary Market (Shotgun)</text>'
    
    # Target
    svg += draw_target(205, 200, '#3B82F6') # Blue
    
    # Shotgun Impacts (Scattered dots)
    random.seed(42)
    for _ in range(15):
        angle = random.uniform(0, 2 * math.pi)
        dist = random.uniform(0, 100)
        dx = dist * math.cos(angle)
        dy = dist * math.sin(angle)
        svg += f'<circle cx="{205 + dx}" cy="{200 + dy}" r="3" fill="#60A5FA" opacity="0.8" />'
        
    # Label
    svg += '<text x="205" y="320" text-anchor="middle" fill="#94A3B8" font-size="14">Broad Coverage</text>'
    svg += '<rect x="155" y="335" width="100" height="30" rx="15" fill="#1E3A8A" stroke="#3B82F6" stroke-width="1" />'
    svg += '<text x="205" y="355" text-anchor="middle" fill="#60A5FA" font-size="14" font-weight="bold">2x Payout</text>'
    svg += '</g>'

    # --- RIGHT PANEL: SNIPER (Skepsis) ---
    svg += '<g id="sniper-panel">'
    # Panel Background
    svg += '<rect x="410" y="20" width="370" height="360" rx="12" fill="#1A1D24" stroke="#333" stroke-width="1" />'
    # Title
    svg += '<text x="595" y="60" text-anchor="middle" fill="white" font-size="16" font-weight="bold">Skepsis (Sniper)</text>'
    
    # Target
    svg += draw_target(595, 200, '#A3E635') # Lime Green
    
    # Sniper Impact (Single Bullseye Hit)
    svg += '<circle cx="595" cy="200" r="8" fill="#A3E635" filter="url(#glow)" />'
    svg += '<circle cx="595" cy="200" r="5" fill="#FFFFFF" />'
    
    # Label
    svg += '<text x="595" y="320" text-anchor="middle" fill="#94A3B8" font-size="14">Precision Strike</text>'
    
    # Glowing Badge
    svg += '<rect x="545" y="335" width="100" height="30" rx="15" fill="#365314" stroke="#A3E635" stroke-width="1" />'
    svg += '<text x="595" y="355" text-anchor="middle" fill="#A3E635" font-size="14" font-weight="bold" filter="url(#glow)">10x Payout</text>'
    svg += '</g>'

    write_svg("outcome-ui.svg", svg)

if __name__ == "__main__":
    gen_sniper_shotgun_svg()
