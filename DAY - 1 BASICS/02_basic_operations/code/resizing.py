# resizing
import os

import cv2


img = cv2.imread(os.path.join('..','..','data','bird.jpeg'))

resized_img = cv2.resize(img, (640, 640))

print(img.shape)
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)

output_dir = os.path.join('..', '..', 'output_data', 'basic_operations')
os.makedirs(output_dir, exist_ok=True)
cv2.imwrite(os.path.join(output_dir,'bird_resized.jpeg'), resized_img)