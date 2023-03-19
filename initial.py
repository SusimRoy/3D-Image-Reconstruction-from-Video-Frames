import cv2

# Load the two stereo images
def points(img1,img2):
    # img1 = cv2.imread('left_image.png', cv2.IMREAD_GRAYSCALE)
    # img2 = cv2.imread('right_image.png', cv2.IMREAD_GRAYSCALE)

    # Create a SIFT detector and compute keypoints and descriptors for both images
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, desc1 = sift.detectAndCompute(img1, None)
    kp2, desc2 = sift.detectAndCompute(img2, None)

    # Create a Brute-Force Matcher object
    bf = cv2.BFMatcher()

    # Match the descriptors
    matches = bf.match(desc1, desc2)

    # Sort the matches by their distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Select the top N matches
    N = 50
    matches = matches[:N]

    # Extract the coordinates of the matched keypoints
    pts1 = []
    pts2 = []
    for match in matches:
        pts1.append(kp1[match.queryIdx].pt)
        pts2.append(kp2[match.trainIdx].pt)

    return pts1, pts2
