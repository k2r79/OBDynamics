import json


class Configuration:

    def __init__(self):
        # Parse the configuration file
        self._data = json.load(open("settings.conf"))

    @property
    def host_mac(self):
        return self._data["host_mac"]

    @property
    def host_port(self):
        return self._data["host_port"]


