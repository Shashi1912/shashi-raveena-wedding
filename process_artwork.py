from PIL import Image, ImageFilter
import numpy as np

im = Image.open('ref_feet_crop.png').convert('RGBA')
w, h = im.size

# Let's crop slightly tighter to remove any stray border bits on left/right
# Left has stray cage bit: crop x: 15..w-15
im_clean = im.crop((15, 0, w - 15, h))
cw, ch = im_clean.size

# Create gradient alpha mask for top and bottom so it feathers smoothly
mask = Image.new('L', (cw, ch), 255)
mask_arr = np.array(mask)

# Feather top 25 pixels
for y in range(25):
    alpha = int(255 * (y / 25.0))
    mask_arr[y, :] = np.minimum(mask_arr[y, :], alpha)

# Feather left 15 pixels
for x in range(15):
    alpha = int(255 * (x / 15.0))
    mask_arr[:, x] = np.minimum(mask_arr[:, x], alpha)

# Feather right 15 pixels
for x in range(15):
    alpha = int(255 * (x / 15.0))
    mask_arr[:, cw - 1 - x] = np.minimum(mask_arr[:, cw - 1 - x], alpha)

# Feather bottom 20 pixels
for y in range(20):
    alpha = int(255 * (y / 20.0))
    mask_arr[ch - 1 - y, :] = np.minimum(mask_arr[ch - 1 - y, :], alpha)

feathered_mask = Image.fromarray(mask_arr).filter(ImageFilter.GaussianBlur(3))
im_clean.putalpha(feathered_mask)
im_clean.save('feet_artwork_feathered.png')
print("Saved feet_artwork_feathered.png, size:", im_clean.size)
