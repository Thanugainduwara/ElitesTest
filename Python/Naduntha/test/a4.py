from PIL import Image, ImageDraw
import os

def overlay_qr_codes(folder, output_folder, num_codes):
    # Define A4 dimensions in pixels (assuming 300 dpi)
    a4_width = 3508.0  # pixels
    a4_height =  2480.0# pixels

    # Calculate the size of each image to fit 3x4 grid on A4 page
    image_width = a4_width / 3.0
    image_height = a4_height / 4.0 

    # Create a new image with A4 dimensions and white background
    a4_image = Image.new("RGB", (int(a4_width), int(a4_height)), "white")

    # Calculate the margin between images
    margin_x = (a4_width - 3.0 * image_width) / 4.0
    margin_y = (a4_height - 4.0 * image_height) / 5.0

    # Paste each QR code onto the A4 page
    for i in range(1, min(num_codes, 12) + 1):  # Display up to 12 images
        qr_code_path = os.path.join(folder, f'overlay_qr_code_{i}.jpg')  # Assuming file name format
        qr_code_image = Image.open(qr_code_path).convert("RGB")  # Convert to RGB mode
        
        # Make the image bigger
        qr_code_image = qr_code_image.resize((int(image_width * 0.9567), int(image_height * 0.8)))
        
        # Calculate the position to place the QR code
        col = (i - 1) % 3
        row = (i - 1) // 3
        x = col * (image_width + margin_x) + margin_x
        y = row * (image_height + margin_y) + margin_y

        # Paste the QR code onto the A4 page
        a4_image.paste(qr_code_image, (int(x), int(y)))

    # Save the final A4 image with overlaid QR codes
    output_file = os.path.join(output_folder, "a4_with_qr_codes.jpg")
    a4_image.save(output_file)

folder = "/home/naduntha/Desktop/test/overlay"  # Specify the directory containing QR code images
output_folder = "/home/naduntha/Desktop/test/a4"  # Specify the directory where you want to save the output image
num_codes = 12  # Set the number of QR codes you want to display

overlay_qr_codes(folder, output_folder, num_codes)
