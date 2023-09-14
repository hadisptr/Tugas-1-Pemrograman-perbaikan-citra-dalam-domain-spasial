import cv2

# Load an image
image_path = 'original_image.jpg'  # Replace with the path to your image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equalized_image = cv2.equalizeHist(image)

# Save the equalized image
output_path = 'equalized_image.jpg'
cv2.imwrite(output_path, equalized_image)

# Display the original and equalized images (optional)
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
