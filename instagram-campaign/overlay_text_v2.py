#!/usr/bin/env python3
"""Add text overlay to the headshot image — V2 with fixed contrast."""
from PIL import Image, ImageDraw, ImageFont

img = Image.open('/home/jonny/.openclaw/workspace/instagram-campaign/images/v2/02-story-stephan-cta.png')
draw = ImageDraw.Draw(img)
W, H = img.size  # 3392 x 5056

font_bold = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'

# --- Top right: "LEAVING CERT" (white) + "MATHS" + "REVISION" (white, with teal accent line) ---
line1_font = ImageFont.truetype(font_bold, 160)
line1 = "LEAVING CERT"
bbox1 = draw.textbbox((0, 0), line1, font=line1_font)
w1 = bbox1[2] - bbox1[0]
x1 = W - w1 - 200
y1 = 350
draw.text((x1, y1), line1, fill='#8BBEC2', font=line1_font)  # light aqua

# "MATHS" - big and white
big_font = ImageFont.truetype(font_bold, 280)
line2 = "MATHS"
bbox2 = draw.textbbox((0, 0), line2, font=big_font)
w2 = bbox2[2] - bbox2[0]
x2 = W - w2 - 200
y2 = y1 + 190
draw.text((x2, y2), line2, fill='white', font=big_font)

# "REVISION" - big and white
line3 = "REVISION"
bbox3 = draw.textbbox((0, 0), line3, font=big_font)
w3 = bbox3[2] - bbox3[0]
x3 = W - w3 - 200
y3 = y2 + 300
draw.text((x3, y3), line3, fill='white', font=big_font)

# Accent bar under REVISION
bar_y = y3 + 310
draw.rectangle([x3, bar_y, x3 + w3, bar_y + 16], fill='#4A8C8C')

# "COURSE" smaller underneath
course_font = ImageFont.truetype(font_bold, 160)
line4 = "COURSE"
bbox4 = draw.textbbox((0, 0), line4, font=course_font)
w4 = bbox4[2] - bbox4[0]
x4 = W - w4 - 200
y4 = bar_y + 50
draw.text((x4, y4), line4, fill='#8BBEC2', font=course_font)

# --- Bottom banner ---
banner_height = 800
banner_y = H - banner_height
img = img.convert('RGBA')
overlay = Image.new('RGBA', (W, banner_height), (15, 20, 30, 210))
img.paste(overlay, (0, banner_y), overlay)
draw = ImageDraw.Draw(img)

# Date
cta_font = ImageFont.truetype(font_bold, 140)
cta_text = "STARTS SUNDAY, MARCH 22"
bbox_cta = draw.textbbox((0, 0), cta_text, font=cta_font)
w_cta = bbox_cta[2] - bbox_cta[0]
x_cta = (W - w_cta) // 2
y_cta = banner_y + 100
draw.text((x_cta, y_cta), cta_text, fill='white', font=cta_font)

# Phone number - white and bold
phone_font = ImageFont.truetype(font_bold, 130)
phone_text = "Book Now · 085 846 6670"
bbox_phone = draw.textbbox((0, 0), phone_text, font=phone_font)
w_phone = bbox_phone[2] - bbox_phone[0]
x_phone = (W - w_phone) // 2
y_phone = y_cta + 200
draw.text((x_phone, y_phone), phone_text, fill='white', font=phone_font)

# Brand - Leamy Maths
brand_font = ImageFont.truetype(font_bold, 90)
brand_text = "LEAMY MATHS · LIMERICK"
bbox_brand = draw.textbbox((0, 0), brand_text, font=brand_font)
w_brand = bbox_brand[2] - bbox_brand[0]
x_brand = (W - w_brand) // 2
y_brand = y_phone + 200
draw.text((x_brand, y_brand), brand_text, fill='#8BBEC2', font=brand_font)

# Save
output = '/home/jonny/.openclaw/workspace/instagram-campaign/images/post1-parents-v2.png'
img = img.convert('RGB')
img.save(output, quality=95)
print(f'Saved to {output}')
