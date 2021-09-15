import urllib.request as urllib
import cv2
import numpy as np
from matplotlib import pyplot as plt



color_light = np.array([0, 0, 0])
color_dark = np.array([181, 148, 255])

crop_y=50
crop_x=60
crop_h=400
crop_w=580

name = "particle selection"

cv2.namedWindow(name, cv2.WINDOW_FREERATIO)
cv2.resizeWindow(name, 1980, 1024)
cv2.setWindowProperty(name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

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
    frame_croped = frame[crop_y:crop_y+crop_h, crop_x:crop_x+crop_w]

    frame_hsv = cv2.cvtColor(frame_croped, cv2.COLOR_BGR2HSV)
    frame_gray = cv2.cvtColor(frame_hsv, cv2.COLOR_BGR2GRAY)
    frame_gray_denoised = cv2.fastNlMeansDenoising(frame_gray, None, 10, 7, 21)

    frame_thresh = cv2.adaptiveThreshold(frame_gray_denoised, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
    contours, hierarchy = cv2.findContours(frame_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


    height, width, _ = frame_croped.shape
    min_x, min_y = width, height
    max_x = max_y = 0
    frame_features_rect = frame_croped.copy()
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        if w < 80 and h < 80:
            frame_features_rect = cv2.rectangle(frame_features_rect, (x,y), (x+w,y+h), (255, 0, 0), 1)


    # cv2.imshow(name, thresh)
    # cv2.imshow(name, frame)

    line1 = np.hstack((cv2.resize(frame, (frame_croped.shape[1], frame_croped.shape[0]), interpolation = cv2.INTER_AREA) , frame_croped))
    line2= np.hstack((frame_features_rect, cv2.cvtColor(frame_thresh, cv2.COLOR_GRAY2BGR)))
    cv2.imshow(name, np.vstack((line1, line2)) )

    # cv2.imshow(name, np.hstack((frame, thresh)) )

    # fig = plt.figure()
    # color = ('b','g','r')
    # for i,col in enumerate(color):
    #     histr = cv2.calcHist([frame],[i],None,[256],[0,256])
    #     plt.plot(histr,color = col)
    #     plt.xlim([0,256])
    # fig.canvas.draw()
    # img_plot = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    # img_plot  = cv2.resize(img_plot, (frame.shape[0], frame.shape[0]), interpolation = cv2.INTER_AREA) 
    
    # cv2.imshow(name, np.hstack((cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), img_plot) ))


    


    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()        
cv2.destroyAllWindows()