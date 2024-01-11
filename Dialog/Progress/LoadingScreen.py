from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from Dialog.Progress.circle import CircleProgress  # Make sure this is the correct import for your CircleProgress class
import sys

class LoadingScreen(QMainWindow):
    def __init__(self):
        super(LoadingScreen, self).__init__()
        self.ui = CircleProgress()
        self.ui.setupUi(self)

        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(Qt.WA_TranslucentBackground)  # Set background to transparent

        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        # Initialize counters
        self.counter = 0

    ## DEF TO LOADING
    ########################################################################
    def progress(self, value):
        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(value))

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100:
            value = 100
        self.progressBarValue(value)
        self.ui.labelPercentage.setText(newHtml) 

        # CLOSE SPLASH SCREEN AND OPEN APP
        if value == 100:
            # SHOW MAIN WINDOW
            # CLOSE SPLASH SCREEN
            self.close()

    ## DEF PROGRESS BAR VALUE
    def progressBarValue(self, value):
        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works from 1.000 to 0.000
        progress = 1.0 - (value / 100.0)

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # Ensure that stop values are within the range 0 to 1
        stop_1 = max(0, min(1, float(stop_1)))
        stop_2 = max(0, min(1, float(stop_2)))

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", str(stop_1)).replace(
            "{STOP_2}", str(stop_2)
        )

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)