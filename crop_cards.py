from PIL import Image

# Crop the card from aosKebQY4uw.jpg
im = Image.open('thumbnails/aosKebQY4uw.jpg')
w, h = im.size
print("Size of aosKebQY4uw:", w, h)

# In aosKebQY4uw, the card is in the center-lower region (around x: 400-850, y: 450-800)
# Let's save a crop
crop1 = im.crop((int(w * 0.3), int(h * 0.4), int(w * 0.7), int(h * 0.8)))
crop1.save('thumbnails/crop_card_aos.jpg')

# In qPS0yLEwG3U, card on top right stack
im2 = Image.open('thumbnails/qPS0yLEwG3U.jpg')
w2, h2 = im2.size
crop2 = im2.crop((int(w2 * 0.55), int(h2 * 0.55), int(w2 * 0.95), int(h2 * 0.95)))
crop2.save('thumbnails/crop_card_qps.jpg')

print("Cropped successfully!")
