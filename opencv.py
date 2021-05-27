import cv2

# Load image
img = cv2.imread('assets/portada sweater weather.jpg', 1)  # BGR is the standard load
"""
-1, cv2.IMREAD_COLOR: loads in color transparency dissapears (default)
0, cv2.IMREAD_GREYSCALE: Loads image in grayscale mode
1, cv2.IMREAD UNCHANGED: Loads as such including the alpha channel
"""

# Rotate and resize image
#  img = cv2.resize(img, (400,400))  # to shrink in pixel values
img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)  # to shrink in a scale
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

# Save image after manipulating it
cv2.imwrite("foto.jpg", img)

# Show the image and close
cv2.imshow("Image", img)
cv2.waitKey(0)  # 0 means wait infinitely, 5 means wait 5 sec in case no key is pressed
cv2.destroyAllWindows()  # close everything properly



