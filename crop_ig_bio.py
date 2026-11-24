from PIL import Image

im = Image.open('ig_screenshot.png')
# crop bio area: x: 350 to 900, y: 50 to 300
bio_crop = im.crop((350, 50, 900, 300))
bio_crop.save('ig_bio_crop.png')

# crop highlights area: x: 150 to 1100, y: 200 to 350
hl_crop = im.crop((150, 200, 1100, 350))
hl_crop.save('ig_highlights_crop.png')

print("Cropped bio and highlights!")
