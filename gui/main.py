import sys
from PySide2.QtCore import QTimer
from PySide2.QtGui import QImage

from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine

from cv_image_provider import CvImageProvider

sys.argv += ['--style', 'material']
app = QApplication(sys.argv)
engine = QQmlApplicationEngine()


imageProvider = CvImageProvider()
engine.addImageProvider("cvimage", imageProvider)
engine.load("view.qml")

def refresh_cv_image():
    # CvImageProvider.
    # engine.rootObjects
    # img = engine.elementById("cv_image")
    print( "test" )
    # print( img )

imagePeriod = 1000/25
imageTimer = QTimer()
imageTimer.setInterval(imagePeriod)
imageTimer.timeout.connect(refresh_cv_image)
imageTimer.start()


sys.exit( app.exec_() )
