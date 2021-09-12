
from PySide2.QtCore import QSize
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtQuick import QQuickImageProvider

from pyueye import ueye
from ids.camera import Camera

import cv2
import numpy


class CvImageProvider(QQuickImageProvider):



    def __init__(self):
        super().__init__(QQuickImageProvider.Pixmap)


    def requestPixmap(self, id, size, requestedSize):
        vid = cv2.VideoCapture(0)
        ret, frame = vid.read()
        
        imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # areas = []

        # for i in range(0, len(contours)):
        #     areas.append(cv2.contourArea(contours[i]))

        # mass_centres_x = []
        # mass_centres_y = []

        # for i in range(0, len(contours)):
        #     M = cv2.moments(contours[i], 0)
        #     mass_centres_x.append(int(M['m10']/M['m00']))
        #     mass_centres_y.append(int(M['m01']/M['m00']))

        print('Num particles: ', len(contours))

        # for i in range(0, len(contours)):
        #     print( 'Area', (i + 1), ':', areas[i])

        # for i in range(0, len(contours)):
        #     print( 'Centre',(i + 1),':', mass_centres_x[i], mass_centres_y[i])






        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
       
        return QPixmap.fromImage(image)