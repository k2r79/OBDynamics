import time
from PySide import QtCore
from PySide.QtCore import QThread
from obdlib.OBDUtils import OBDUtils


class SpeedThread(QThread):
    newValueSignal = QtCore.Signal(int)
    zeroToThirtySignal = QtCore.Signal(int)
    zeroToSixtySignal = QtCore.Signal(int)
    zeroToEightySignal = QtCore.Signal(int)
    zeroToHundredSignal = QtCore.Signal(int)

    def __init__(self, *args, **kwargs):
        super(SpeedThread, self).__init__(*args, **kwargs)
        # OBD Connection
        self._obdutils = OBDUtils(MainApp.configuration.host_mac, MainApp.configuration.host_port, False)

        # Time at which the car starts moving
        self._timer = None

        # Previous frame's vehicule speed
        self._previous_vehicule_speed = 0

    def run(self):
        self._obdutils.connect()
        self._obdutils.initialize()

        while True:
            try:
                # Get current vehicule speed and update the GUI
                vehicule_speed = self._obdutils.vehicule_speed()
                self.newValueSignal.emit(vehicule_speed)

                # If the car starts moving
                if self._previous_vehicule_speed == 0 \
                        and vehicule_speed > 0:
                    # Then start the timer
                    self.start_timer()

                # When 30 km/h are passed
                if vehicule_speed >= 30:
                    self.zeroToThirtySignal.emit(self.current_millis() - self._timer)

                # When 60 km/h are passed
                if vehicule_speed >= 60:
                    self.zeroToSixtySignal.emit(self.current_millis() - self._timer)

                # When 80 km/h are passed
                if vehicule_speed >= 80:
                    self.zeroToEightySignal.emit(self.current_millis() - self._timer)

                # When 100 km/h are passed
                if vehicule_speed >= 100:
                    self.zeroToHundredSignal.emit(self.current_millis() - self._timer)

                # Set the previous vehicule speed to the current one
                self._previous_vehicule_speed = vehicule_speed

            except Exception:
                print("An error has occurred... retrying...")

            time.sleep(0.100)

    def current_millis(self):
        return int(round(time.time() * 1000))

    def start_timer(self):
        self._timer = self.current_millis()

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


from MainApp import MainApp