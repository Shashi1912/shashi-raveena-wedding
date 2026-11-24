from PIL import Image

im = Image.open('thumbnails/aosKebQY4uw.jpg')
w, h = im.size

# Let's crop right around the card stack on the plate
# The plate is in the lower-right quadrant:
# x: 450 to 850, y: 350 to 700
crop_precise = im.crop((450, 350, 850, 700))
crop_precise.save('thumbnails/card_closeup.jpg')

# Let's also inspect qPS0yLEwG3U (the other video titled ~500 wedding cards)
im2 = Image.open('thumbnails/qPS0yLEwG3U.jpg')
w2, h2 = im2.size
# On the right side, there is a card lying flat on the bottom right and on top of the stack
crop2_stack = im2.crop((int(w2 * 0.55), int(h2 * 0.6), int(w2 * 0.9), int(h2 * 0.85)))
crop2_stack.save('thumbnails/card_qps_closeup.jpg')
crop2_flat = im2.crop((int(w2 * 0.7), int(h2 * 0.88), w2, h2))
crop2_flat.save('thumbnails/card_qps_bottom.jpg')

print("Saved closeups!")
