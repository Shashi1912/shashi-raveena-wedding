import urllib.request
import os
from PIL import Image, ImageDraw, ImageFont

fonts_to_test = {
    'Great Vibes': 'https://raw.githubusercontent.com/google/fonts/main/ofl/greatvibes/GreatVibes-Regular.ttf',
    'Alex Brush': 'https://raw.githubusercontent.com/google/fonts/main/ofl/alexbrush/AlexBrush-Regular.ttf',
    'Marck Script': 'https://raw.githubusercontent.com/google/fonts/main/ofl/marckscript/MarckScript-Regular.ttf',
    'Kaushan Script': 'https://raw.githubusercontent.com/google/fonts/main/ofl/kaushanscript/KaushanScript-Regular.ttf',
    'Parisienne': 'https://raw.githubusercontent.com/google/fonts/main/ofl/parisienne/Parisienne-Regular.ttf',
    'Allura': 'https://raw.githubusercontent.com/google/fonts/main/ofl/allura/Allura-Regular.ttf'
}

os.makedirs('fonts_test', exist_ok=True)
for name, url in fonts_to_test.items():
    clean_name = name.replace(' ', '_')
    fn = os.path.join('fonts_test', f'{clean_name}.ttf')
    if not os.path.exists(fn):
        try:
            urllib.request.urlretrieve(url, fn)
            print(f'Downloaded {name}')
        except Exception as e:
            print(f'Failed {name}: {e}')

img = Image.new('RGB', (900, 600), color=(240, 228, 205))
draw = ImageDraw.Draw(img)

y = 25
for name in fonts_to_test.keys():
    clean_name = name.replace(' ', '_')
    fn = os.path.join('fonts_test', f'{clean_name}.ttf')
    if os.path.exists(fn):
        try:
            font = ImageFont.truetype(fn, 44)
            draw.text((40, y), f'{name}:  Raveena & Shashi', font=font, fill=(56, 30, 14))
            y += 90
        except Exception as e:
            print(f'Error rendering {name}: {e}')

img.save('font_comparison.png')
print('font_comparison.png saved!')
