
from PIL import Image
from reportlab.pdfgen import canvas
import argparse
import math
import os


def scale_and_create_pdfs_single_v4(image_path, max_papers, pdf_path):
    # Load the image
    img = Image.open(image_path)
    img_width, img_height = img.size
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    paper_width, paper_height = 2550, 3300
    aspect_ratio = img_width / img_height
    num_segments_x = int(math.sqrt(max_papers * aspect_ratio))
    num_segments_y = int(math.sqrt(max_papers / aspect_ratio))
    while num_segments_x * num_segments_y > max_papers:
        if num_segments_x > num_segments_y:
            num_segments_x -= 1
        else:
            num_segments_y -= 1
    new_width = num_segments_x * paper_width
    new_height = num_segments_y * paper_height
    img_scaled = img.resize((new_width, new_height), Image.ANTIALIAS)
    c = canvas.Canvas(pdf_path, pagesize=(paper_width, paper_height))
    temp_files = []
    for i in range(num_segments_y):
        for j in range(num_segments_x):
            left = j * paper_width
            upper = i * paper_height
            right = (j + 1) * paper_width
            lower = (i + 1) * paper_height
            img_segment = img_scaled.crop((left, upper, right, lower))
            temp_img_path = f"/mnt/data/temp_img_segment_{i}_{j}.jpg"
            img_segment.save(temp_img_path)
            temp_files.append(temp_img_path)
            c.drawImage(temp_img_path, 0, 0, width=paper_width, height=paper_height)
            c.showPage()
    c.save()
    for temp_file in temp_files:
        os.remove(temp_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an image into multiple PDF segments.")
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument("max_papers", type=int, help="Maximum number of papers to use")
    parser.add_argument("pdf_path", help="Path to save the output PDF")
    
    args = parser.parse_args()
    scale_and_create_pdfs_single_v4(args.image_path, args.max_papers, args.pdf_path)
