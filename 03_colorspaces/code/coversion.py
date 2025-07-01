import os
import cv2


img = cv2.imread(os.path.join('..', '..', 'output_data', 'basic_operations', 'bird_resized.jpeg'))

img = cv2.resize(img, (320, 320))

# Convert to other color spaces
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Display all at once
cv2.imshow('Original - BGR', img)
cv2.imshow('Grayscale', img_gray)
cv2.imshow('HSV', img_hsv)
cv2.imshow('RGB', img_rgb)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the converted images
output_dir = os.path.join('..', '..', 'output_data', 'colorspaces')
os.makedirs(output_dir, exist_ok=True)
cv2.imwrite(os.path.join(output_dir, 'img_gray.jpeg'), img_gray)
cv2.imwrite(os.path.join(output_dir, 'img_rgb.jpeg'), img_rgb)
cv2.imwrite(os.path.join(output_dir, 'img_hsv.jpeg'), img_hsv)


