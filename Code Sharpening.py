import cv2
import numpy as np
# Load an image
image = cv2.imread('original_image.jpg')

# Apply Sharpening
kernel = np.array([[-1,-1,-1],
                   [-1, 9,-1],
                   [-1,-1,-1]])
sharpened_image = cv2.filter2D(image, -1, kernel)

# Save the equalized image
output_path = 'sharpened_image.jpg'
cv2.imwrite(output_path, sharpened_image)

# Display the original and equalized images (optional)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
