import numpy as np
import cv2

# Load an image
image = cv2.imread('original_image.jpg', cv2.IMREAD_GRAYSCALE)

# Buat filter Gaussian
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]]) / 16

# Terapkan filter ke citra
filtered_image = cv2.filter2D(image, -1, kernel)

# Save the filtered_image
output_path = 'filtered_image.jpg'
cv2.imwrite(output_path, filtered_image)

# Display the original and filtered_image (optional)
cv2.imshow('Original Image', image)
cv2.imshow('filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
