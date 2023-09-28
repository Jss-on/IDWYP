from PIL import Image
from reportlab.pdfgen import canvas
import argparse
import math
import os

paper_sizes = {"letter": (2550, 3300), "a4": (2480, 3508), "legal": (2550, 4200)}


def scale_and_create_pdfs_single_v6(
    image_path,
    max_papers=10,
    pdf_path="output.pdf",
    paper_size="letter",
    orientation="portrait",
):
    paper_width, paper_height = paper_sizes.get(paper_size, (2550, 3300))
    if orientation == "landscape":
        paper_width, paper_height = paper_height, paper_width
    img = Image.open(image_path)
    img_width, img_height = img.size
    if img.mode == "RGBA":
        img = img.convert("RGB")
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
    parser = argparse.ArgumentParser(
        description="Convert an image into multiple PDF segments."
    )
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument(
        "--max_papers",
        type=int,
        default=10,
        help="Maximum number of papers to use (default is 10)",
    )
    parser.add_argument(
        "--pdf_path",
        default="output.pdf",
        help="Path to save the output PDF (default is 'output.pdf')",
    )
    parser.add_argument(
        "--paper_size",
        choices=["letter", "a4", "legal"],
        default="letter",
        help="Paper size (default is 'letter')",
    )
    parser.add_argument(
        "--orientation",
        choices=["portrait", "landscape"],
        default="portrait",
        help="Paper orientation (default is 'portrait')",
    )

    args = parser.parse_args()
    scale_and_create_pdfs_single_v6(
        args.image_path,
        args.max_papers,
        args.pdf_path,
        args.paper_size,
        args.orientation,
    )
