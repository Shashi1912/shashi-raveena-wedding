import os
import subprocess
import shutil
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_file = os.path.abspath(r"D:\Shashi\Card\Shashi_Raveena_Wedding_Card\postcard.html")
target_folder = r"D:\Shashi\Card\Shashi_Raveena_Wedding_Card"
root_folder = r"D:\Shashi\Card"

print("1. Capturing 1x screenshot...")
cmd_1x = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1086,1800",
    f"--screenshot={os.path.join(root_folder, 'temp_preview_1x.png')}",
    html_file
]
subprocess.run(cmd_1x, check=True)

print("2. Capturing 2x (300 DPI) screenshot...")
cmd_2x = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--hide-scrollbars",
    "--force-device-scale-factor=2",
    "--window-size=1086,1800",
    f"--screenshot={os.path.join(root_folder, 'temp_preview_2x.png')}",
    html_file
]
subprocess.run(cmd_2x, check=True)

# Process 1x
im1 = Image.open(os.path.join(root_folder, 'temp_preview_1x.png'))
print(f"1x captured size: {im1.size}")
front_1x = im1.crop((63, 198, 1023, 838))
back_1x = im1.crop((63, 939, 1023, 1579))

# Process 2x
im2 = Image.open(os.path.join(root_folder, 'temp_preview_2x.png'))
print(f"2x captured size: {im2.size}")
front_2x = im2.crop((126, 396, 2046, 1676))
back_2x = im2.crop((126, 1878, 2046, 3158))

# Save to target folder
front_1x.save(os.path.join(target_folder, 'postcard_front.png'))
back_1x.save(os.path.join(target_folder, 'postcard_back.png'))
front_2x.save(os.path.join(target_folder, 'postcard_front_print_300dpi.png'), dpi=(300, 300))
back_2x.save(os.path.join(target_folder, 'postcard_back_print_300dpi.png'), dpi=(300, 300))

# Also copy to root folder
front_1x.save(os.path.join(root_folder, 'postcard_front.png'))
back_1x.save(os.path.join(root_folder, 'postcard_back.png'))
front_2x.save(os.path.join(root_folder, 'postcard_front_print_300dpi.png'), dpi=(300, 300))
back_2x.save(os.path.join(root_folder, 'postcard_back_print_300dpi.png'), dpi=(300, 300))

# Cleanup temp files
if os.path.exists(os.path.join(root_folder, 'temp_preview_1x.png')):
    os.remove(os.path.join(root_folder, 'temp_preview_1x.png'))
if os.path.exists(os.path.join(root_folder, 'temp_preview_2x.png')):
    os.remove(os.path.join(root_folder, 'temp_preview_2x.png'))

print("Front 1x size:", front_1x.size)
print("Back 1x size:", back_1x.size)
print("Front 2x size:", front_2x.size)
print("Back 2x size:", back_2x.size)
print("Done re-rendering all assets without AI symbols!")
