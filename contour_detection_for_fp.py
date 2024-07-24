import cv2
import numpy as np


def contours_of_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Display the edges
    cv2.imshow('Edges', edges)
    cv2.waitKey(0)

    # Apply dilation to the edges
    kernel = np.ones((4, 4), np.uint8)
    edges_dilated = cv2.dilate(edges, kernel, iterations=1)

    # Display the dilated edges
    cv2.imshow('Dilated Edges', edges_dilated)
    cv2.waitKey(0)

    # Apply Hough Circle Transform on the dilated edges
    circles = cv2.HoughCircles(
        edges_dilated,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=30,
        param1=25,
        param2=10,
        minRadius=1,
        maxRadius=30
    )

    # If circles are detected
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw the outer circle
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

    # Display the final image with detected circles
    cv2.imshow('Detected Circles', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Load an example image
img = cv2.imread('C:/Users/alimo/OneDrive/Documents/FRT/Contour Detection (Basketball)/contour-detection/Ballogy False Positive Images/ball_test34.png')

# Check if the image was loaded successfully
if img is not None:
    contours_of_image(img)
else:
    print("Error loading image.")
