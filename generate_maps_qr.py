import qrcode
import qrcode.image.svg

maps_url = 'https://maps.google.com/?q=Thanmaya+Farmstay+Resort,+Rajavaram,+Telangana+506144'
factory = qrcode.image.svg.SvgPathImage
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=2,
    image_factory=factory
)
qr.add_data(maps_url)
qr.make(fit=True)
svg_img = qr.make_image()

svg_str = svg_img.to_string().decode('utf-8')
svg_str = svg_str.replace('fill="#000000"', 'fill="#2b1104"')

paths = [
    r'D:\Shashi\Card\Unique_Wedding_Invitations\venue_qr.svg',
    r'D:\Shashi\Card\venue_qr.svg',
    r'D:\Shashi\Card\Shashi_Raveena_Wedding_Card\venue_qr.svg'
]

for p in paths:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(svg_str)

print('Generated clean Google Maps QR code SVG in all directories!')
print('Target URL:', maps_url)
