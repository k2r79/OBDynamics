
class Configuration:

    def __init__(self):
        self._host_mac = None
        self._host_port = None

        # Parse the configuration file
        with open("settings.conf") as file:
            for line in file.readlines():
                splitted_line = line.split("=")
                if splitted_line[0] == "host_mac":
                    self._host_mac = splitted_line[1]
                elif splitted_line[0] == "host_port":
                    self._host_port = int(splitted_line[1])

    @property
    def host_mac(self):
        return self._host_mac

    @property
    def host_port(self):
        return self._host_port


