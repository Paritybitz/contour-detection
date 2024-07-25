import cv2
import numpy as np

def detect_circle(image):
    # Step 1: Read the image
    # image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to open image.")
        return None

    # Step 2: Convert to grayscale
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 3: Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(image, (9, 9), 2)

    # Step 4: Edge detection using Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Step 5: Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100,
                               param1=5, param2=30, minRadius=1, maxRadius=0)

    if circles is not None:
        # Convert circles to (x, y, r) format and round the values
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            # Draw the circle in the output image (for visualization)
            cv2.circle(image, (x, y), r, (0, 255, 0), 4)
            # Draw the center of the circle
            cv2.circle(image, (x, y), 3, (0, 128, 255), -1)

        # Display the output image with the detected circle
        cv2.imshow("Detected Circle", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return circles
    else:
        print("No circles detected.")
        return None
    

def draw_circles(image, circles):
    # Step 1: Load the image
    # image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to open image.")
        return

    # Step 2: Draw circles on the image
    for (x, y, r) in circles:
        # Draw the circle perimeter
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)
        # Draw the circle center
        cv2.circle(image, (x, y), 2, (0, 0, 255), 3)

    # Step 3: Display the image with circles
    cv2.imshow("Image with Circles", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Optionally, save the image with circles
    # output_path = 'output_image_with_circles.jpg'
    # cv2.imwrite(output_path, image)
    # print(f"Output image saved to {output_path}")

def contours_of_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Display the edges
    # cv2.imshow('Edges', edges)
    cv2.waitKey(0)

    # Apply dilation to the edges
    kernel = np.ones((4, 4), np.uint8)
    edges_dilated = cv2.dilate(edges, kernel, iterations=1)

    # Display the dilated edges
    img1= cv2.resize(edges_dilated, (0, 0), fx = 3, fy = 3)

    cv2.imshow('Dilated Edges', edges_dilated)
    cv2.waitKey(0)

    print(type(edges_dilated))
    circles=detect_circle(edges_dilated)
    draw_circles(img,circles)


    # # Apply Hough Circle Transform on the dilated edges
    # circles = cv2.HoughCircles(
    #     edges_dilated,
    #     cv2.HOUGH_GRADIENT,
    #     dp=1,
    #     minDist=30,
    #     param1=25,
    #     param2=10,
    #     minRadius=5,
    #     maxRadius=100
    # )

    # # If circles are detected
    # if circles is not None:
    #     circles = np.uint16(np.around(circles))
    #     for i in circles[0, :]:
    #         # Draw the outer circle
    #         cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    #         # Draw the center of the circle
    #         cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

    # # Display the final image with detected circles
    # cv2.imshow('Detected Circles', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# Load an example image
img = cv2.imread('C:/Users/alimo/OneDrive/Documents/FRT/Contour Detection (Basketball)/contour-detection/Ballogy False Positive Images/ball_test35.png')

# Check if the image was loaded successfully
if img is not None:
    contours_of_image(img)
else:
    print("Error loading image.")
