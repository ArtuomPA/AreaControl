#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tracking import Tracking
from transformation import Transformation
from compare import Compare
from db import DB
import sys
from rotate import Rotate
from trapezium import Trapezium
import argparse

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
from PyQt5.QtCore import QThread, pyqtSignal

from camid import CamId

from video_source import VideoSource

ap = argparse.ArgumentParser()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Calc = CalcThtead()

        # Connect the buttons.
        self.ui.pushButton_1.clicked.connect(self.Calc.start)
        self.ui.pushButton_2.clicked.connect(self.stopCalc)
        self.ui.pushButton_3.clicked.connect(self.stopProg)
        self.Calc.GetNewCoordinatesStr.connect(self.ui.textEdit.append)
        self.Calc.GetNewCoordinatesInt.connect(self.ui.widget.setCoordinates)

    def stopCalc(self):
        if self.Calc.runIndicator == 1:
            self.Calc.stopC = 1

    def stopProg(self):
        if self.Calc.runIndicator ==1:
            self.Calc.db.commit()
            self.Calc.db.disconnect()
            self.Calc.tracker1.stop()
            self.Calc.tracker2.stop()
        sys.exit()


class CalcThtead(QThread):
    GetNewCoordinatesInt = pyqtSignal(int, int)
    GetNewCoordinatesStr = pyqtSignal(str)
    def __init__(self, parent=None):
        super(CalcThtead, self).__init__()
        self.vidSource = VideoSource(ap)
        self.Video1 = self.vidSource.getVid1()
        self.Video2 = self.vidSource.getVid2()
        self.stopC = 0
        self.db = DB()
        self.tracker1 = Tracking()
        self.tracker2 = Tracking()
        self.center = None
        self.runIndicator = 0
        self.camInd = None
        self.trapezium = Trapezium()

    def run(self):
        self.tracker1.getVideo(self.Video1)
        self.tracker2.getVideo(self.Video2)
        self.db.connect()
        self._id = 0
        self.idChecker = CamId()

        while True:
            if self.stopC == 1:
                break

            center1 = self.tracker1.trackFrame()
            center2 = self.tracker2.trackFrame()

            if center1 == -1 or center2 == -1:
                break

            if center1==None:
                scaledCenter = Transformation(
                        center2,
                        self.trapezium.getTrapeziumBaseLarge(),
                        self.trapezium.getTrapeziumBaseSmall(),
                        self.trapezium.getTrapeziumHeight(),
                        self.trapezium.getZeroPointPosition())
                self.center = Rotate(scaledCenter)
                delta=None
                self.camInd = "Вторая"
            elif center2==None:
                scaledCenter = Transformation(
                        center1,
                        self.trapezium.getTrapeziumBaseLarge(),
                        self.trapezium.getTrapeziumBaseSmall(),
                        self.trapezium.getTrapeziumHeight(),
                        self.trapezium.getZeroPointPosition())
                self.center = scaledCenter
                delta=None
                self.camInd = "Первая"
            else:
                scaledCenter1 = Transformation(
                        center1,
                        self.trapezium.getTrapeziumBaseLarge(),
                        self.trapezium.getTrapeziumBaseSmall(),
                        self.trapezium.getTrapeziumHeight(),
                        self.trapezium.getZeroPointPosition())
                scaledCenter2 = Transformation(
                        center2,
                        self.trapezium.getTrapeziumBaseLarge(),
                        self.trapezium.getTrapeziumBaseSmall(),
                        self.trapezium.getTrapeziumHeight(),
                        self.trapezium.getZeroPointPosition())

                delta = Compare(scaledCenter1, scaledCenter2)
                self.center = (
                        [
                                int((scaledCenter1[0]+scaledCenter2[0])/2),
                                int((scaledCenter1[1]+scaledCenter2[1])/2)
                                ]
                        )
                delta = [int(delta[0]), int(delta[1])]
                self.camInd = "Обе"

            self.center=[int(self.center[0]), int(self.center[1])]

            if not self.idChecker.isCurrent(self.center):
                self._id = self._id + 1

            self.GetNewCoordinatesInt.emit(self.center[0],self.center[1])
            self.GetNewCoordinatesStr.emit("Позиция = "+str(self.center)+
                                           "  Камера: "+self.camInd+
                                           "  Объект: "+str(self._id))

            self.db.vrite(self.center, delta, self.camInd, self._id)
            if self.runIndicator !=1:
                self.runIndicator = 1

        self.db.commit()
        self.db.disconnect()
        self.tracker1.stop()
        self.tracker2.stop()
        if self.stopC != 0:
            self.stopC = 0
        if self.runIndicator != 0:
            self.runIndicator = 0


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
