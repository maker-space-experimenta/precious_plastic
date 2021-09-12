import urllib.request as urllib
import cv2
import numpy as np
import time




color_light = np.array([0, 0, 0])
color_dark = np.array([181, 148, 255])

name = "test"

cv2.namedWindow(name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(name, 1980, 1024)

# device = cv2.CAP_OPENNI
# device = cv2.CAP_ANY
# device = cv2.CAP_FFMPEG 
device = cv2.CAP_GSTREAMER

cap = cv2.VideoCapture(device)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("native resolution", width, height)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640.0) # width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480.0) # height
# cap.set(cv2.CAP_PROP_EXPOSURE, 1)
# cap.set(cv2.CAP_PROP_WB_TEMPERATURE, 6000) 

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("configured resolution", width, height)


pBackSub = cv2.createBackgroundSubtractorMOG2()


while True:

    # Use urllib to get the image and convert into a cv2 usable format
    ret, frame = cap.read()
    # frame = cv2.resize(frame, (320, 240), interpolation = cv2.INTER_AREA)


    y=50
    x=60
    h=400
    w=580
    frame = frame[y:y+h, x:x+w]



    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # mask = cv2.inRange(hsv, color_light, color_dark)
    # masked = cv2.bitwise_and(frame,frame, mask= mask)

    imgray = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)
    imgray = cv2.fastNlMeansDenoising(imgray, None, 10, 7, 21)

    # ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    # thresh = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    thresh = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame, contours, -1, (0,255,0), 3)

    print(len(contours))
    print(len(hierarchy))


    height, width, _ = frame.shape
    min_x, min_y = width, height
    max_x = max_y = 0
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        # min_x, max_x = min(x, min_x), max(x+w, max_x)
        # min_y, max_y = min(y, min_y), max(y+h, max_y)
        if w < 80 and h < 80:
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 1)
        # if max_x - min_x > 0 and max_y - min_y > 0:
        #     frame = cv2.rectangle(frame, (min_x, min_y), (max_x, max_y), (255, 0, 0), 1)

    # cv2.imshow(name, thresh)
    cv2.imshow(name, frame)

    # line1 = np.hstack((frame, thresh))
    # line2= np.hstack((frame, masked))
    # cv2.imshow(name, np.vstack((line1, line2)) )

    # cv2.imshow(name, np.hstack((frame, thresh)) )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()        
cv2.destroyAllWindows()