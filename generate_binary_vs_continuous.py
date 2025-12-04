import svgwrite
from svgwrite import cm, mm
import math

def create_binary_vs_continuous_svg():
    # Canvas setup
    width = 800
    height = 400
    dwg = svgwrite.Drawing('images/binary-vs-continuous.svg', size=(width, height))
    
    # --- Definitions (Gradients & Filters) ---
    # Glow Filter
    # Using raw XML for filter to avoid svgwrite version issues or API guessing
    filter_glow = dwg.defs.add(dwg.filter(id="glow", x="-20%", y="-20%", width="140%", height="140%"))
    # svgwrite doesn't always expose filter primitives on the drawing object in all versions
    # We can use the generic 'element' method or just skip the filter if it's troublesome.
    # Let's try to construct it manually if needed, but for now let's skip the glow on the text/box to ensure it runs.
    # Or better, use a simple opacity trick.
    
    # Binary Gradient (Blue)
    grad_binary = dwg.defs.add(dwg.linearGradient(id="binaryGrad", x1="0", x2="0", y1="0", y2="1"))
    grad_binary.add_stop_color(offset="0%", color="#3b82f6", opacity=0.3)
    grad_binary.add_stop_color(offset="100%", color="#3b82f6", opacity=0.05)

    # Skepsis Gradient (Lime)
    grad_skepsis = dwg.defs.add(dwg.linearGradient(id="skepsisGrad", x1="0", x2="0", y1="0", y2="1"))
    grad_skepsis.add_stop_color(offset="0%", color="#bef264", opacity=0.3)
    grad_skepsis.add_stop_color(offset="100%", color="#bef264", opacity=0.05)
    
    # Red Gradient (Loss)
    grad_loss = dwg.defs.add(dwg.linearGradient(id="lossGrad", x1="0", x2="0", y1="0", y2="1"))
    grad_loss.add_stop_color(offset="0%", color="#ef4444", opacity=0.3)
    grad_loss.add_stop_color(offset="100%", color="#ef4444", opacity=0.05)

    # Styles
    dwg.defs.add(dwg.style("text { font-family: Inter, system-ui, sans-serif; }"))

    # --- Colors ---
    bg_color = "#09090b"
    card_bg = "#18181b"
    card_stroke = "#27272a"
    text_white = "#ffffff"
    text_muted = "#a1a1aa"
    
    col_binary = "#3b82f6" # Blue
    col_skepsis = "#bef264" # Lime
    col_loss = "#ef4444" # Red

    # Main Background
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill=bg_color))

    # --- Helper Functions ---
    def draw_card(x_offset, title, is_binary):
        # Card Container
        group = dwg.g(transform=f"translate({x_offset}, 20)")
        group.add(dwg.rect(insert=(0, 0), size=(370, 360), rx=12, fill=card_bg, stroke=card_stroke))
        
        # Title
        group.add(dwg.text(title, insert=(185, 40), text_anchor="middle", 
                           fill=text_white, font_size="18px", font_weight="bold"))

        # Graph Area
        graph_top = 100
        graph_bottom = 250
        graph_height = graph_bottom - graph_top
        graph_left = 40
        graph_right = 330
        graph_width = graph_right - graph_left
        
        # Grid Lines
        for i in range(5):
            y = graph_top + (i * (graph_height / 4))
            group.add(dwg.line(start=(graph_left, y), end=(graph_right, y), 
                               stroke=card_stroke, stroke_width=1))
            
        # Axis Labels (Price)
        # Range: $90k to $110k (Wider context)
        min_p = 90.0
        max_p = 110.0
        range_p = max_p - min_p
        
        def get_x(price):
            return graph_left + ((price - min_p) / range_p) * graph_width
            
        group.add(dwg.text("$90k", insert=(graph_left, graph_bottom + 20), fill=text_muted, font_size="10px", text_anchor="middle"))
        group.add(dwg.text("$100k", insert=(get_x(100), graph_bottom + 20), fill=text_muted, font_size="10px", text_anchor="middle"))
        group.add(dwg.text("$110k", insert=(graph_right, graph_bottom + 20), fill=text_muted, font_size="10px", text_anchor="middle"))

        # --- The Plot ---
        outcome_price = 99.8
        outcome_x = get_x(outcome_price)

        if is_binary:
            # Binary Logic: 0 below 100k, 1 above 100k
            threshold_x = get_x(100)
            
            # Path: Start low, go to threshold, go up, go right
            # "Loss" area fill
            
            # We only want to highlight the "Cliff" aspect. 
            # Let's draw the line
            line_path = f"M {graph_left},{graph_bottom} L {threshold_x},{graph_bottom} L {threshold_x},{graph_top} L {graph_right},{graph_top}"
            group.add(dwg.path(d=line_path, stroke=col_loss, stroke_width=3, fill="none"))
            
            # Fill the "Win" side blue
            win_area = f"M {threshold_x},{graph_bottom} L {threshold_x},{graph_top} L {graph_right},{graph_top} L {graph_right},{graph_bottom} Z"
            group.add(dwg.path(d=win_area, fill="url(#binaryGrad)"))

            # Threshold Line
            group.add(dwg.line(start=(threshold_x, graph_top), end=(threshold_x, graph_bottom + 10), 
                               stroke=text_muted, stroke_width=1, stroke_dasharray="4,4"))
            
            # Outcome Marker (Loss)
            group.add(dwg.circle(center=(outcome_x, graph_bottom), r=6, fill=col_loss, stroke=card_bg, stroke_width=2))
            
            # Annotation
            group.add(dwg.text("You are here ($99.8k)", insert=(outcome_x, graph_bottom - 15), 
                               fill=col_loss, font_size="12px", font_weight="bold", text_anchor="end"))
            
            # Result Box
            group.add(dwg.rect(insert=(135, 300), size=(100, 36), rx=18, fill=col_loss, fill_opacity="0.2", stroke=col_loss))
            group.add(dwg.text("LOSE", insert=(185, 324), text_anchor="middle", fill=col_loss, font_size="16px", font_weight="bold"))
            
            group.add(dwg.text("Missed by $200", insert=(185, 280), text_anchor="middle", fill=text_muted, font_size="12px"))

        else:
            # Skepsis Logic: Range $95k-$105k.
            range_start = 95
            range_end = 105
            range_start_x = get_x(range_start)
            range_end_x = get_x(range_end)
            
            # Draw "Bars" to represent the spectrum/continuous nature
            # We'll draw thin rectangles across the range
            num_bars = 20
            bar_width = (range_end_x - range_start_x) / num_bars
            
            for i in range(num_bars):
                bx = range_start_x + i * bar_width
                # Make them slightly separated
                bw = bar_width - 1
                if bw < 1: bw = 1
                
                # Height: Full height (Plateau)
                group.add(dwg.rect(insert=(bx, graph_top), size=(bw, graph_height), 
                                   fill=col_skepsis, opacity=0.3))
            
            # Outline the whole range
            # Path: Up at start, across, down at end
            line_path = f"M {graph_left},{graph_bottom} L {range_start_x},{graph_bottom} L {range_start_x},{graph_top} L {range_end_x},{graph_top} L {range_end_x},{graph_bottom} L {graph_right},{graph_bottom}"
            group.add(dwg.path(d=line_path, stroke=col_skepsis, stroke_width=2, fill="none"))
            
            # Range Labels
            group.add(dwg.text("$95k", insert=(range_start_x, graph_bottom + 15), fill=col_skepsis, font_size="10px", text_anchor="middle"))
            group.add(dwg.text("$105k", insert=(range_end_x, graph_bottom + 15), fill=col_skepsis, font_size="10px", text_anchor="middle"))

            # Outcome Marker (Win)
            group.add(dwg.circle(center=(outcome_x, graph_top), r=6, fill=col_skepsis, stroke=card_bg, stroke_width=2))
            
            # Annotation
            group.add(dwg.text("You are here ($99.8k)", insert=(outcome_x, graph_top - 15), 
                               fill=col_skepsis, font_size="12px", font_weight="bold", text_anchor="middle"))

            # Result Box
            # Removed filter="url(#glow)" to avoid error
            group.add(dwg.rect(insert=(135, 300), size=(100, 36), rx=18, fill=col_skepsis, fill_opacity="0.2", stroke=col_skepsis)) 
            group.add(dwg.text("WIN", insert=(185, 324), text_anchor="middle", fill="#000000", font_size="16px", font_weight="bold"))

            group.add(dwg.text("Inside Range ($95k-$105k)", insert=(185, 280), text_anchor="middle", fill=text_muted, font_size="12px"))

        dwg.add(group)

    # Draw Cards
    draw_card(20, "Binary Market", True)
    draw_card(410, "Skepsis Market", False)

    dwg.save()

if __name__ == '__main__':
    create_binary_vs_continuous_svg()