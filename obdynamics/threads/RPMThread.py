import time
from PySide import QtCore
from PySide.QtCore import QThread
from obdlib.OBDUtils import OBDUtils


class RPMThread(QThread):
    newValueSignal = QtCore.Signal(int)

    def __init__(self, *args, **kwargs):
        super(RPMThread, self).__init__(*args, **kwargs)
        self._obdutils = OBDUtils("66:35:56:78:90:AB", 1, True)

    def run(self):
        self._obdutils.connect()
        self._obdutils.initialize()

        while True:
            try:
                engine_rpm = self._obdutils.engine_rpm()
                self.newValueSignal.emit(engine_rpm)
            except Exception:
                print("An error has occurred... retrying...")

            time.sleep(0.20)

    def exit(self, *args, **kwargs):
        self.obdutils.close()

        super(RPMThread, self).exit(*args, **kwargs)


    @property
    def obdutils(self):
        return self._obdutils

    @property
    def rpmGauge(self):
        return self._rpmGauge

    @rpmGauge.setter
    def rpmGauge(self, rpmGauge):
        self._rpmGauge = rpmGauge