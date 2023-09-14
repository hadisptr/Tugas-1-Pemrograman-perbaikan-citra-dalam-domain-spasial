import cv2

# Load an image
image = cv2.imread('original_image.jpg')

# Apply Smoothing
blurred_image = cv2.blur(image, (5, 5))  # Ukuran kernel filter (5x5)

# Save the equalized image
output_path = 'blurred_image.jpg'
cv2.imwrite(output_path, blurred_image)

# Display the original and equalized images (optional)
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
