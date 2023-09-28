
# IDWYP - I Dont Want Your Paper

## Description
This Python script takes an image and splits it into segments, each fitting on a specified paper size. The segments are then compiled into a single PDF file.

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
python main.py <image_path> [--max_papers <max_papers>] [--pdf_path <pdf_path>] [--paper_size <paper_size>]
```

- `image_path`: Path to the input image (required).
- `max_papers`: Maximum number of papers to use (optional, default is 10).
- `pdf_path`: Path to save the output PDF (optional, default is 'output.pdf').
- `paper_size`: Paper size to use ('letter', 'a4', or 'legal') (optional, default is 'letter').

## Example
```bash
python main.py "./static/sample_image.png" --max_papers 9 --pdf_path "output.pdf" --paper_size "a4"
```

### Available Paper Sizes
- 'letter': 8.5 x 11 inches
- 'a4': 210 x 297 mm
- 'legal': 8.5 x 14 inches
