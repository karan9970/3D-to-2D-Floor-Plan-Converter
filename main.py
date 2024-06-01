import cv2
import numpy as np
def load_image(image_path):
    # Load the image from the specified path
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"No image found at {image_path}")
    return image

def convert_to_grayscale(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def detect_edges(image):
    # Use Canny edge detection to find edges in the image
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    return edges

def find_contours(edges):
    # Find contours in the edged image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_contours(image, contours):
    # Draw contours on the image
    floor_plan = np.zeros_like(image)
    cv2.drawContours(floor_plan, contours, -1, (255, 255, 255), 2)
    return floor_plan

def save_image(image, output_path):
    # Save the processed image to the specified path
    cv2.imwrite(output_path, image)

def main(input_image_path, output_image_path):
    # Load the 3D image
    image = load_image(input_image_path)
    
    # Convert to grayscale
    gray_image = convert_to_grayscale(image)
    
    # Detect edges
    edges = detect_edges(gray_image)
    
    # Find contours
    contours = find_contours(edges)
    
    # Draw contours to create a floor plan
    floor_plan = draw_contours(gray_image, contours)
    
    # Save the floor plan
    save_image(floor_plan, output_image_path)
    print(f"Floor plan saved to {output_image_path}")

if __name__ == "__main__":
    input_image_path = "D:\python\practise\pexels-mo-eid-1268975-9454915.jpg"
    output_image_path = "path_to_save_floor_plan.jpg"
    main(input_image_path, output_image_path)
