#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QDeclarativeView, qmlRegisterType
from obdynamics.widget.OBDWidgets import CircularGauge

app = QApplication(sys.argv)

qmlRegisterType(CircularGauge, "ODBWidgets", 1, 0, "CircularGauge")

view = QDeclarativeView()

context = view.rootContext()

url = QUrl('view.qml')
view.setSource(url)
view.show()

sys.exit(app.exec_())