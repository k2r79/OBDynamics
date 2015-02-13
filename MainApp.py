#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide import QtCore

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QDeclarativeView, qmlRegisterType
from obdynamics.threads.SpeedThread import SpeedThread
from obdynamics.widget.OBDWidgets import CircularGauge

def setSpeedGaugeValue(value):
    speedGauge.setValue(value)

app = QApplication(sys.argv)

qmlRegisterType(CircularGauge, "ODBWidgets", 1, 0, "CircularGauge")

view = QDeclarativeView()

context = view.rootContext()

url = QUrl('view.qml')
view.setSource(url)
view.show()

speedGauge = view.rootObject().findChild(CircularGauge, "speedGauge")

speedThread = SpeedThread()
speedThread.newValueSignal.connect(setSpeedGaugeValue)
speedThread.start()

r = app.exec_()

speedThread.exit()
sys.exit(r)