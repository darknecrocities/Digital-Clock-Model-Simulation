
from datetime import datetime

# 7-segment bitmask
segments = {
    '0': [1,1,1,1,1,1,0],
    '1': [0,1,1,0,0,0,0],
    '2': [1,1,0,1,1,0,1],
    '3': [1,1,1,1,0,0,1],
    '4': [0,1,1,0,0,1,1],
    '5': [1,0,1,1,0,1,1],
    '6': [1,0,1,1,1,1,1],
    '7': [1,1,1,0,0,0,0],
    '8': [1,1,1,1,1,1,1],
    '9': [1,1,1,1,0,1,1]
}

# Segment coordinates
segment_coords = [
    [(10,10), (60,10), (50,20), (20,20)],        # top
    [(60,10), (70,20), (70,60), (60,50)],        # top right
    [(60,60), (70,70), (70,110), (60,100)],      # bottom right
    [(10,100), (60,100), (50,110), (20,110)],    # bottom
    [(10,60), (20,70), (20,110), (10,100)],      # bottom left
    [(10,10), (20,20), (20,60), (10,50)],        # top left
    [(10,55), (60,55), (50,65), (20,65)]         # middle
]

def setup():
    size(1300, 400)
    frameRate(1)
    textFont(createFont("Courier", 24))
    noStroke()

def draw():
    background(0)
    now = datetime.now()
    
    h = now.hour
    m = now.minute
    s = now.second

    hour_str = str(h).zfill(2)
    minute_str = str(m).zfill(2)
    second_str = str(s).zfill(2)

    base_x = 30
    base_y = 40
    scale = 2
    digit_width = 80 * scale  # approximate width of one digit after scaling
    digit_spacing = 15        # space between digits

    # Draw digits and colons with consistent spacing
    x = base_x
    draw_digit(hour_str[0], x, base_y, scale)
    x += digit_width + digit_spacing
    draw_digit(hour_str[1], x, base_y, scale)
    x += digit_width + digit_spacing

    draw_colon(x, base_y, scale)
    x += digit_spacing + 20  # colon width approx + spacing

    draw_digit(minute_str[0], x, base_y, scale)
    x += digit_width + digit_spacing
    draw_digit(minute_str[1], x, base_y, scale)
    x += digit_width + digit_spacing

    draw_colon(x, base_y, scale)
    x += digit_spacing + 20

    draw_digit(second_str[0], x, base_y, scale)
    x += digit_width + digit_spacing
    draw_digit(second_str[1], x, base_y, scale)

def draw_digit(n, x, y, s):
    if n not in segments:
        return
    fill(0, 255, 0)
    segs = segments[n]
    for i in range(7):
        if segs[i]:
            draw_segment(segment_coords[i], x, y, s)

def draw_segment(coords, x, y, s):
    beginShape()
    for px, py in coords:
        vertex(x + px * s, y + py * s)
    endShape(CLOSE)

def draw_colon(x, y, s):
    fill(0, 255, 0)
    ellipse(x, y + 30 * s, 15 * s, 15 * s)
    ellipse(x, y + 70 * s, 15 * s, 15 * s)
