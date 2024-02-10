import qrcode

# Data to be encoded
data = "https://www.elites.liupe.xyz"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an Image object from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save it somewhere, change the path as needed
img.save("qrcode_example.png")
