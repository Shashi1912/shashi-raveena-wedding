from PIL import Image

im = Image.open('CardRef/IMG-20261118-WA0001(1).jpg')
w, h = im.size
print("Original ref size:", w, h)

# Let's see the bounding box of the front card (top-left)
# The front card is in the top-left area.
# In a 1024x1024 or 1600x1600 image:
# Let's inspect coordinates
# Front card bounds are roughly x: 40..540, y: 110..490
# The feet illustration inside the front card is roughly x: 130..430, y: 145..355
crop_feet = im.crop((int(w * 0.13), int(h * 0.14), int(w * 0.44), int(h * 0.36)))
crop_feet.save('ref_feet_crop.png')

# Let's also crop the Ganesha icon from the back card:
# Back card is at bottom-left: x: 40..540, y: 530..900
crop_ganesha = im.crop((int(w * 0.25), int(h * 0.545), int(w * 0.33), int(h * 0.62)))
crop_ganesha.save('ref_ganesha_crop.png')

# Let's crop the envelope wax seal from the right side:
crop_seal = im.crop((int(w * 0.70), int(h * 0.45), int(w * 0.82), int(h * 0.58)))
crop_seal.save('ref_seal_crop.png')

print("Cropped reference assets!")
