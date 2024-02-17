
from pdf2image import convert_from_path
import os

def generate_qr_codes(folder, num_codes):
    for i in range(1, num_codes + 1):
        pdf_file = os.path.join(folder, f'qr_code_{i}.pdf')
        images = convert_from_path(pdf_file)
        for idx, image in enumerate(images):
            image.save(os.path.join(output_folder, f'qr_code_{i}_{idx + 1}.jpg'), 'JPEG')

folder = "/home/naduntha/Desktop/test/pdf"
output_folder = "/home/naduntha/Desktop/test/jpg"
num_codes = 12
generate_qr_codes(folder, num_codes)
