import cv2

image = cv2.imread('original_image.jpg')
blurred_image = cv2.blur(image, (5, 5))  # Ukuran kernel filter (5x5)

cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
