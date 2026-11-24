from PIL import Image

im = Image.open('reel_frames/aosKebQY4uw_sec04.jpg')
w, h = im.size

# The back side of the postcard (where hands are resting):
# x: 100 to 800, y: 350 to 850
back_crop = im.crop((int(w * 0.1), int(h * 0.35), int(w * 0.8), int(h * 0.85)))
back_crop.save('reel_frames/real_back_crop.jpg')

# The front side of the postcard (top right cards):
# x: 550 to 1050, y: 220 to 600
front_crop = im.crop((int(w * 0.55), int(h * 0.22), int(w * 0.98), int(h * 0.6)))
front_crop.save('reel_frames/real_front_crop.jpg')

print("Cropped real postcard from reel!")
