import os
import cv2
import numpy as np


img = cv2.imread(os.path.join('..','..','data', 'basketball-player.jpg'))

img = cv2.resize(img, (640, 640))

# Edge detection
img_edge = cv2.Canny(img, 100, 200)

# Morphological operations
kernel = np.ones((3, 3), dtype=np.uint8)
img_edge_d = cv2.dilate(img_edge, kernel)
img_edge_e = cv2.erode(img_edge_d, kernel)

cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the converted images
output_dir = os.path.join('..', '..', 'output_data', 'edge_detection')
os.makedirs(output_dir, exist_ok=True)
cv2.imwrite(os.path.join(output_dir, 'img_edge.jpeg'), img_edge)
cv2.imwrite(os.path.join(output_dir, 'img_edge_d.jpeg'), img_edge_d)
cv2.imwrite(os.path.join(output_dir, 'img_edge_e.jpeg'), img_edge_e)    
