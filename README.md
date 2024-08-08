# Contour Detection

<p align="center">
  <img src="https://github.com/user-attachments/assets/469738f0-b328-4885-8369-479499fa820f" alt="Image 1" width="26.5%" />
  <img src="https://github.com/user-attachments/assets/12376bc3-1b93-4122-ad3f-da1ac54dda95" alt="Image 2" width="30%" />
</p>

*The image on the left is input (the bounding box), the image on the right is the output (contour ball detection)*

<br>

This project involves detecting circles (using hough_circle), and contours, and calculating the percentage of white pixels in images using OpenCV. The main functionalities include detecting circles in an image, drawing contours, cropping detected circles, and processing images in a folder to calculate the percentage of white pixels. ***THE ISSUE:*** all these images were detected as false positives in the model my team and I were training.

## Features

- **Circle Detection:** Detect circles in an image using Hough Circle Transform.
- **Contour Detection:** Detect edges and contours in an image.
- **Crop Circles:** Crop the detected circles from the image.
- **Percentage of White Pixels:** Calculate the percentage of white pixels in an image.
- **Batch Processing:** Process all images in a specified folder and calculate the percentage of white pixels for each image.

## Prerequisites

- Python 3.11.4
- OpenCV (cv2)
- NumPy
- OS

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/contour-detection.git
   cd contour-detection
   ```
2. Install required packages:
   ```bash
   pip install opencv-python-headless numpy
   ```
