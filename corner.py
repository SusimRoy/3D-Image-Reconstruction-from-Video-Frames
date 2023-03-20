import cv2
import numpy as np

# Load the image
def corner(img):
    img = cv2.imread('image.jpg')

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Define the Harris Corner parameters
    block_size = 2
    aperture = 3
    k = 0.04
    threshold = 0.01

    # Apply Harris Corner detection
    dst = cv2.cornerHarris(gray, block_size, aperture, k)

    # Normalize the detected corner values to be in the range [0,1]
    dst_norm = cv2.normalize(dst, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    corners = np.argwhere(dst_norm > threshold)

    return corners[:7]
