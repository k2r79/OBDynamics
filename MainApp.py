#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide import QtCore

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QDeclarativeView, qmlRegisterType
from obdynamics.threads.RPMThread import RPMThread
from obdynamics.widget.OBDWidgets import CircularGauge

def setRPMGaugeValue(value):
    rpmGauge.setValue(value)

app = QApplication(sys.argv)

qmlRegisterType(CircularGauge, "ODBWidgets", 1, 0, "CircularGauge")

view = QDeclarativeView()

context = view.rootContext()

url = QUrl('view.qml')
view.setSource(url)
view.show()

rpmGauge = view.rootObject().findChild(CircularGauge, "rpmGauge")
rpmThread = RPMThread()

rpmThread.newValueSignal.connect(setRPMGaugeValue)
rpmThread.start()

r = app.exec_()

rpmThread.exit()
sys.exit(r)