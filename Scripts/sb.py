import cv2
import numpy as np

def percentage_of_white_pixels(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Check if image was successfully loaded
    if image is None:
        raise ValueError(f"Image at path '{image_path}' could not be loaded.")
    
    # Convert the image to grayscale (if it's not already)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Create a binary image where white pixels are separated from others
    _, binary_image = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)
    print(type(binary_image))
    # cv2.imshow(binary_image)
    # Count the number of white pixels
    white_pixels = np.sum(binary_image >200)
    
    # Count the total number of pixels
    total_pixels = binary_image.size
    
    # Calculate the percentage of white pixels
    white_percentage = (white_pixels / total_pixels) * 100
    
    return white_percentage

# Example usage:
image_path = 'C:/Users/alimo/Documents/FRT/Contour Detection (Basketball)/contour-detection/spiral_test.png'
percentage = percentage_of_white_pixels(image_path)
print(f"Percentage of white pixels in the image: {percentage:.2f}%")
