from PIL import Image
import numpy as np

im = Image.open('ref_ganesha_crop.png').convert('RGBA')
# crop just Ganesha, excluding text at bottom
w, h = im.size
ganesha_only = im.crop((10, 5, w - 10, int(h * 0.85)))
arr = np.array(ganesha_only)

# The background is kraft paper (r~185, g~155, b~120). The lines are darker (r<140).
# Let's extract the line art as dark brown with transparency:
r = arr[:, :, 0].astype(float)
g = arr[:, :, 1].astype(float)
b = arr[:, :, 2].astype(float)

# Background lightness
bg_val = 160.0
# Anything darker than bg_val has opacity
alpha = np.clip((bg_val - (r + g + b) / 3.0) * 4.0, 0, 255).astype(np.uint8)

# Set color to deep antique sepia #3d2314
out_arr = np.zeros_like(arr)
out_arr[:, :, 0] = 61
out_arr[:, :, 1] = 35
out_arr[:, :, 2] = 20
out_arr[:, :, 3] = alpha

ganesha_clean = Image.fromarray(out_arr)
ganesha_clean.save('ganesha_transparent.png')
print("Saved ganesha_transparent.png, size:", ganesha_clean.size)
