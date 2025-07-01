import os
import cv2

# read video
video_path = os.path.join('..', '..', 'data', 'snow.mp4')

video = cv2.VideoCapture(video_path)

# visualize video

ret = True
while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('frame', frame)
        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()