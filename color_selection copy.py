import signal
import sys

import urllib.request as urllib
import cv2
import numpy as np
import time

# CONFIG SECTION

color_light = np.array([0, 0, 0])
color_dark = np.array([181, 148, 255])
name = "test"


def crop_image(img):
    y=50
    x=60
    h=400
    w=580
    return img[y:y+h, x:x+w]

def fix_colors(img):
    return img


def setup_cap():
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

    return cap


def create_mask(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, color_light, color_dark)
    masked = cv2.bitwise_and(frame,frame, mask= mask)

    return masked


# def get_contours(masked):

#     return contours


def start(cap):
    while True:
        ret, frame = cap.read()
        frame = crop_image(frame)
        frame = fix_colors(frame)

        masked = create_mask(frame)
        
        imgray = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
        # ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        # thresh = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        thresh = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # cv2.drawContours(frame, contours, -1, (0,255,0), 3)
# 
        cv2.imshow(name, thresh)
        # cv2.imshow(name, frame)
        # cv2.imshow(name, np.hstack((frame, masked)))

        if cv2.waitKey(1) & 0xFF == 27:
            break


def dispose():
    cap.release()        
    cv2.destroyAllWindows()

def sigint_handler(*args):
    """Handler for the SIGINT signal."""
    sys.stderr.write('\r')
    # QApplication.quit()
    # app.quit()
    dispose()


if __name__ == '__main__':
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 1980, 1024)

    cap = setup_cap()
    start(cap)


    signal.signal(signal.SIGINT, sigint_handler)