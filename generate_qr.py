import qrcode
from PIL import Image

# Google Maps link
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=6,
    border=1,
)
qr.add_data('https://maps.google.com/?q=Wedding+Venue')
qr.make(fit=True)

# Generate image with vintage colors: dark brown on cream/kraft
img = qr.make_image(fill_color="#3e2714", back_color="#f2e6cf")
img.save("venue_qr.png")
print("Saved venue_qr.png, size:", img.size)
