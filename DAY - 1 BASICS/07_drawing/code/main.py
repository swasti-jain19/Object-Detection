import os
import cv2


img = cv2.imread(os.path.join('..','..','data', 'whiteboard.png'))

print(img.shape)

# line
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

# rectangle
cv2.rectangle(img, (200, 350), (450, 600), (0, 0, 255), -1)

# circle
# format - (image, center, radius, color, thickness)
cv2.circle(img, (800, 200), 75, (255, 0, 0), 10)

# text
cv2.putText(img, 'Hey you!', (600, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 10)

cv2.imshow('img', img)
cv2.waitKey(0)

# Save the converted images
output_dir = os.path.join('..', '..', 'output_data', 'drawing')
os.makedirs(output_dir, exist_ok=True)
cv2.imwrite(os.path.join(output_dir, 'drawing.jpeg'), img)  
