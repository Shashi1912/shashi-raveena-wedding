from PIL import Image

im = Image.open('postcard_preview.png')
print('Preview image size:', im.size)

# Front card: x=63 to 1023, y=198 to 838 (960x640)
# Back card:  x=63 to 1023, y=939 to 1579 (960x640)
card_front = im.crop((63, 198, 1023, 838))
card_front.save('postcard_front.png')

card_back = im.crop((63, 939, 1023, 1579))
card_back.save('postcard_back.png')

print(f"Front saved: size={card_front.size}")
print(f"Back saved: size={card_back.size}")
