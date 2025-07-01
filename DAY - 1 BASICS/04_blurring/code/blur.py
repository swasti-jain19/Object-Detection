import os
import cv2


img = cv2.imread(os.path.join('..','..','data', 'cow-salt-peper.png'))

k_size = 7
img_blur = cv2.blur(img, (k_size, k_size))
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 5)
img_median_blur = cv2.medianBlur(img, k_size)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_median_blur', img_median_blur)
cv2.waitKey(0)

# Save the converted images
output_dir = os.path.join('..', '..', 'output_data', 'blurring')
os.makedirs(output_dir, exist_ok=True)
cv2.imwrite(os.path.join(output_dir, 'img_blur.jpeg'), img_blur)
cv2.imwrite(os.path.join(output_dir, 'img_gaussian_blur.jpeg'), img_gaussian_blur)
cv2.imwrite(os.path.join(output_dir, 'img_median_blur.jpeg'), img_median_blur)
