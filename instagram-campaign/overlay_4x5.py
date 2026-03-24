#!/usr/bin/env python3
"""Create 4:5 Instagram-ready image with text overlay."""
from PIL import Image, ImageDraw, ImageFont

# Load and crop source to 4:5
src = Image.open('/home/jonny/.openclaw/workspace/instagram-campaign/images/v2/02-story-stephan-cta.png')
W_src, H_src = src.size  # 3392 x 5056

# Target 4:5 at same width
W = W_src  # 3392
H = int(W * 5 / 4)  # 4240

# Crop source - keep upper portion (head area)
img = src.crop((0, 0, W, H))
draw = ImageDraw.Draw(img)

font_bold = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'

# --- Top right header ---
# "LEAVING CERT"
f_sm = ImageFont.truetype(font_bold, 140)
t1 = "LEAVING CERT"
bb1 = draw.textbbox((0, 0), t1, font=f_sm)
w1 = bb1[2] - bb1[0]
x1 = W - w1 - 180
y1 = 280
draw.text((x1, y1), t1, fill='#8BBEC2', font=f_sm)

# "MATHS"
f_big = ImageFont.truetype(font_bold, 250)
t2 = "MATHS"
bb2 = draw.textbbox((0, 0), t2, font=f_big)
w2 = bb2[2] - bb2[0]
x2 = W - w2 - 180
y2 = y1 + 160
draw.text((x2, y2), t2, fill='white', font=f_big)

# "REVISION"
t3 = "REVISION"
bb3 = draw.textbbox((0, 0), t3, font=f_big)
w3 = bb3[2] - bb3[0]
x3 = W - w3 - 180
y3 = y2 + 270
draw.text((x3, y3), t3, fill='white', font=f_big)

# "COURSE"
f_med = ImageFont.truetype(font_bold, 150)
t4 = "COURSE"
bb4 = draw.textbbox((0, 0), t4, font=f_med)
w4 = bb4[2] - bb4[0]
x4 = W - w4 - 180
y4 = y3 + 280
draw.text((x4, y4), t4, fill='white', font=f_med)

# Teal accent bar
bar_y = y4 + 170
draw.rectangle([x4, bar_y, x4 + w4, bar_y + 12], fill='#4A8C8C')

# --- Mid: value props ---
f_prop = ImageFont.truetype(font_bold, 95)
props = [
    ">  Higher Level",
    ">  In-Person, Limerick",
    ">  New Topic Every Sunday",
]
y_p = bar_y + 60
for p in props:
    bb = draw.textbbox((0, 0), p, font=f_prop)
    wp = bb[2] - bb[0]
    xp = W - wp - 180
    draw.text((xp, y_p), p, fill='#8BBEC2', font=f_prop)
    y_p += 125

# --- Bottom banner ---
banner_h = 600
banner_y = H - banner_h
img = img.convert('RGBA')
overlay = Image.new('RGBA', (W, banner_h), (15, 20, 30, 215))
img.paste(overlay, (0, banner_y), overlay)
draw = ImageDraw.Draw(img)

# "STARTS SUNDAY, MARCH 22"
f_cta = ImageFont.truetype(font_bold, 120)
cta = "STARTS SUNDAY, MARCH 22"
bb_cta = draw.textbbox((0, 0), cta, font=f_cta)
w_cta = bb_cta[2] - bb_cta[0]
draw.text(((W - w_cta) // 2, banner_y + 70), cta, fill='white', font=f_cta)

# "Book Now · 085 846 6670"
f_phone = ImageFont.truetype(font_bold, 110)
phone = "Book Now  ·  085 846 6670"
bb_ph = draw.textbbox((0, 0), phone, font=f_phone)
w_ph = bb_ph[2] - bb_ph[0]
draw.text(((W - w_ph) // 2, banner_y + 230), phone, fill='white', font=f_phone)

# "LEAMY MATHS · LIMERICK"
f_brand = ImageFont.truetype(font_bold, 90)
brand = "LEAMY MATHS  ·  LIMERICK"
bb_br = draw.textbbox((0, 0), brand, font=f_brand)
w_br = bb_br[2] - bb_br[0]
draw.text(((W - w_br) // 2, banner_y + 400), brand, fill='white', font=f_brand)

# Save
out = '/home/jonny/.openclaw/workspace/instagram-campaign/images/post1-parents-4x5.png'
img = img.convert('RGB')
img.save(out, quality=95)
print(f'Saved: {img.size}')
