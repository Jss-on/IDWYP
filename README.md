
# IDWYP-I Dont Want Your Paper

## Description
This Python script takes an image and splits it into segments, each fitting on a letter-size paper. The segments are then compiled into a single PDF file.

## Installation
1. Clone this repository.
2. Navigate to the project directory.
3. Install the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run the script using the following command:
```bash
python scale_my_image.py <image_path> <max_papers> <pdf_path>
```

- `image_path`: Path to the input image.
- `max_papers`: Maximum number of papers to use for the output.
- `pdf_path`: Path to save the output PDF.

## Example
```bash
python scale_my_image.py "./static/sample_image.png" 9 "output.pdf"
```
