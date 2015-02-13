import time
from PySide import QtCore
from PySide.QtCore import QThread
from obdlib.OBDUtils import OBDUtils


class SpeedThread(QThread):
    newValueSignal = QtCore.Signal(int)

    def __init__(self, *args, **kwargs):
        super(SpeedThread, self).__init__(*args, **kwargs)
        self._obdutils = OBDUtils("66:35:56:78:90:AB", 1, False)

    def run(self):
        self._obdutils.connect()
        self._obdutils.initialize()

        while True:
            try:
                vehicule_speed = self._obdutils.vehicule_speed()
                self.newValueSignal.emit(vehicule_speed)
            except Exception:
                print("An error has occurred... retrying...")

            time.sleep(0.100)

    def exit(self, *args, **kwargs):
        self.obdutils.close()
        super(SpeedThread, self).exit(*args, **kwargs)

    @property
    def obdutils(self):
        return self._obdutils

    @property
    def speedGauge(self):
        return self._speedGauge

    @speedGauge.setter
    def speedGauge(self, speedGauge):
        self._speedGauge = speedGauge