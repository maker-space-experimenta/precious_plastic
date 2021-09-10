
from PySide2.QtCore import QSize
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtQuick import QQuickImageProvider

import cv2

class CvImageProvider(QQuickImageProvider):

    def __init__(self):
        super().__init__(QQuickImageProvider.Pixmap)


    def requestPixmap(self, id, size, requestedSize):

        vid = cv2.VideoCapture(0)
        ret, cvImg = vid.read()

        height, width, channel = cvImg.shape
        bytesPerLine = 3 * width
        image = QImage(cvImg.data, width, height, bytesPerLine, QImage.Format_RGB888)
       
        return QPixmap.fromImage(image)