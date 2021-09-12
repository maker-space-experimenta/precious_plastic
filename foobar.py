import urllib.request as urllib
import cv2
import numpy as np
import time




color_light = np.array([255,255,255])
color_dark = np.array([200, 200, 200])

# device = cv2.CAP_OPENNI
# device = cv2.CAP_ANY
# device = cv2.CAP_FFMPEG 
device = cv2.CAP_GSTREAMER

cap = cv2.VideoCapture(device)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("native resolution", width, height)

# cap.set(3, 640.0) # width
# cap.set(4, 480.0) # height

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("configured resolution", width, height)

while True:

    # Use urllib to get the image and convert into a cv2 usable format
    ret, frame = cap.read()

    img_height, img_width, channels = frame.shape
    print("img size", img_height, img_width)

    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    print('Num particles: ', len(contours))

    try: hierarchy = hierarchy[0]
    except: hierarchy = []

    height, width, _ = frame.shape
    min_x, min_y = width, height
    max_x = max_y = 0

    # computes the bounding box for the contour, and draws it on the frame,
    for contour, hier in zip(contours, hierarchy):
        (x,y,w,h) = cv2.boundingRect(contour)
        min_x, max_x = min(x, min_x), max(x+w, max_x)
        min_y, max_y = min(y, min_y), max(y+h, max_y)
        if w > 80 and h > 80:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)

    if max_x - min_x > 0 and max_y - min_y > 0:
        cv2.rectangle(frame, (min_x, min_y), (max_x, max_y), (255, 0, 0), 2)




    # put the image on screen
    cv2.imshow('Webcam', thresh)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()        
cv2.destroyAllWindows()