import cv2
import numpy as np

image = cv2.imread('pantai.jpeg')
cv2.imshow('Original Image', image)
cv2.waitKey(0)

#Median Blur
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(8)

cv2.imwrite('pantai_Median_Blur.jpeg', median)

cv2.waitKey(0)
cv2.destroyAllWindows()