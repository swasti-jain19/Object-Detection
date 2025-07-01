import os
import cv2


# read image
image_path = os.path.join('..', '..','data', 'bird.jpeg')

img = cv2.imread(image_path)

# write image

cv2.imwrite(os.path.join('..', 'output_data', 'bird_out.jpeg'), img)

# visualize image

cv2.imshow('image', img)
cv2.waitKey(0)