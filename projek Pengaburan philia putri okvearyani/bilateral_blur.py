import cv2
import numpy as np

image = cv2.imread('pantai.jpeg')
cv2.imshow('Original Image', image)
cv2.waitKey(0)

#Bilateral Blur
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)

cv2.imwrite('pantai_Bilateral_Blur.jpeg', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()