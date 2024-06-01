# 3D to 2D Floor Plan Converter

This Python program converts 3D images into 2D floor plans using image processing techniques. The tool leverages OpenCV for edge detection and contour finding to extract key features like walls and doors, generating a simplified floor plan.

## Features

- Convert 3D images to 2D floor plans
- Detect edges and contours to identify structural features
- Save the generated floor plan as an image

## Requirements

- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/3d-to-2d-floor-plan-converter.git
    cd 3d-to-2d-floor-plan-converter
    ```

2. Install the required packages:
    ```bash
    pip install opencv-python-headless numpy
    ```

## Usage

Run the script with the input 3D image path and the desired output path for the floor plan:

```bash
python convert_3d_to_2d.py path_to_your_3d_image.jpg path_to_save_floor_plan.jpg
