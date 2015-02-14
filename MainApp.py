#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide import QtCore

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QDeclarativeView, qmlRegisterType
from obdynamics.threads.SpeedThread import SpeedThread
from obdynamics.utils.Configuration import Configuration
from obdynamics.widget.OBDWidgets import CircularGauge


class MainApp:
    # Static configuration class
    configuration = Configuration()

    def main(self):
        self._app = QApplication(sys.argv)

        qmlRegisterType(CircularGauge, "ODBWidgets", 1, 0, "CircularGauge")

        view = QDeclarativeView()

        context = view.rootContext()

        url = QUrl('view.qml')
        view.setSource(url)
        view.show()

        # Bind variables to the QML elements
        self._root_object = view.rootObject()
        self._speedGauge = self._root_object.findChild(CircularGauge, "speedGauge")

        # Initialize the speed thread
        self._speedThread = SpeedThread()

        # Connect the signals to their slots
        self._speedThread.newValueSignal.connect(self.setSpeedGaugeValue)
        self._speedThread.zeroToThirtySignal.connect(self.setZeroToThirtyTime)
        self._speedThread.zeroToSixtySignal.connect(self.setZeroToSixtyTime)
        self._speedThread.zeroToEightySignal.connect(self.setZeroToEightyTime)
        self._speedThread.zeroToHundredSignal.connect(self.setZeroToHundredTime)

        # Start the speed thread
        self._speedThread.start()

        r = self._app.exec_()

        self._speedThread.exit()
        sys.exit(r)

    def setSpeedGaugeValue(self, value):
        self._speedGauge.setValue(value)

    def setZeroToThirtyTime(self, time):
        self._root_object.setZeroToThirtyText(self.millis_to_seconds(time))

    def setZeroToSixtyTime(self, time):
        self._root_object.setZeroToSixtyText(self.millis_to_seconds(time))

    def setZeroToEightyTime(self, time):
        self._root_object.setZeroToEightyText(self.millis_to_seconds(time))

    def setZeroToHundredTime(self, time):
        self._root_object.setZeroToHundredText(self.millis_to_seconds(time))

    def millis_to_seconds(self, time):
        seconds = int(time / 1000)
        milliseconds = int(time - seconds * 1000)

        return str(seconds) + "." + str(milliseconds) + "s"

if __name__ == '__main__':
    mainApp = MainApp()
    mainApp.main()