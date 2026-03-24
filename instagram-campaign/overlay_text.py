#!/usr/bin/env python3
"""Add text overlay to the headshot image for Instagram post."""
from PIL import Image, ImageDraw, ImageFont

# Load image
img = Image.open('/home/jonny/.openclaw/workspace/instagram-campaign/images/v2/02-story-stephan-cta.png')
draw = ImageDraw.Draw(img)
W, H = img.size  # 3392 x 5056

# Fonts
font_bold = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'

# --- Top text: "LEAVING CERT" + "MATHS REVISION" ---
top_font_size = 200
top_font = ImageFont.truetype(font_bold, top_font_size)

# Line 1
line1 = "LEAVING CERT"
bbox1 = draw.textbbox((0, 0), line1, font=top_font)
w1 = bbox1[2] - bbox1[0]
# Position top-right area
x1 = W - w1 - 200
y1 = 300
draw.text((x1, y1), line1, fill='white', font=top_font)

# Line 2 - bigger
big_font_size = 240
big_font = ImageFont.truetype(font_bold, big_font_size)
line2 = "MATHS"
bbox2 = draw.textbbox((0, 0), line2, font=big_font)
w2 = bbox2[2] - bbox2[0]
x2 = W - w2 - 200
y2 = y1 + 220
draw.text((x2, y2), line2, fill='#4A8C8C', font=big_font)

line3 = "REVISION"
bbox3 = draw.textbbox((0, 0), line3, font=big_font)
w3 = bbox3[2] - bbox3[0]
x3 = W - w3 - 200
y3 = y2 + 260
draw.text((x3, y3), line3, fill='#4A8C8C', font=big_font)

# --- Bottom banner ---
# Semi-transparent dark banner at bottom
banner_height = 900
banner_y = H - banner_height
overlay = Image.new('RGBA', (W, banner_height), (20, 25, 35, 200))
# Convert main image to RGBA for compositing
img = img.convert('RGBA')
img.paste(overlay, (0, banner_y), overlay)

draw = ImageDraw.Draw(img)

# CTA text
cta_font = ImageFont.truetype(font_bold, 160)
cta_text = "STARTS SUNDAY MARCH 22"
bbox_cta = draw.textbbox((0, 0), cta_text, font=cta_font)
w_cta = bbox_cta[2] - bbox_cta[0]
x_cta = (W - w_cta) // 2
y_cta = banner_y + 100
draw.text((x_cta, y_cta), cta_text, fill='white', font=cta_font)

# Sub-CTA
sub_font = ImageFont.truetype(font_bold, 120)
sub_text = "Book now · 085 846 6670"
bbox_sub = draw.textbbox((0, 0), sub_text, font=sub_font)
w_sub = bbox_sub[2] - bbox_sub[0]
x_sub = (W - w_sub) // 2
y_sub = y_cta + 220
draw.text((x_sub, y_sub), sub_text, fill='#8BBEC2', font=sub_font)

# Leamy Maths branding
brand_font = ImageFont.truetype(font_bold, 100)
brand_text = "LEAMY MATHS"
bbox_brand = draw.textbbox((0, 0), brand_text, font=brand_font)
w_brand = bbox_brand[2] - bbox_brand[0]
x_brand = (W - w_brand) // 2
y_brand = y_sub + 200
draw.text((x_brand, y_brand), brand_text, fill='#4A8C8C', font=brand_font)

# Save
output = '/home/jonny/.openclaw/workspace/instagram-campaign/images/post1-parents-overlay.png'
img = img.convert('RGB')
img.save(output, quality=95)
print(f'Saved to {output}')
print(f'Size: {img.size}')
