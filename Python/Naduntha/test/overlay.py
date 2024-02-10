from PIL import Image
import os

def overlay_qr_codes(folder, output_folder, num_codes, background_image_path):
    for i in range(1, num_codes + 1):
        qr_code_path = os.path.join(folder, f'qr_code_{i}_1.jpg')  # Assuming only one image per QR code
        qr_code_image = Image.open(qr_code_path).convert("RGB")  # Convert to RGB mode
        qr_width, qr_height = qr_code_image.size

        # Open the background image for each iteration to avoid the transparency issue
        background_image = Image.open(background_image_path)
        bg_width, bg_height = background_image.size

        # Calculate the size of the centered box as a float value
        box_size = min(bg_width, bg_height) / 1.359

        # Resize the QR code image to fit within the box
        qr_code_image = qr_code_image.resize((int(box_size), int(box_size)))

        # Calculate the position to place the QR code in a centered box on the background image
        x = int((bg_width - box_size) / 2.05)
        y = int((bg_height - box_size) / 1.3)

        # Paste the QR code onto the background image at the calculated position
        background_image.paste(qr_code_image, (x, y))

        # Specify the output folder for saving the overlaid image
        output_path = os.path.join(output_folder, f'overlay_qr_code_{i}.jpg')
        
        # Save the overlaid image
        background_image.save(output_path)

folder = "/home/naduntha/Desktop/test/jpg"
output_folder = "/home/naduntha/Desktop/test/overlay"
background_image_path = "/home/naduntha/Desktop/test/card.png"
num_codes = 12

overlay_qr_codes(folder, output_folder, num_codes, background_image_path)
