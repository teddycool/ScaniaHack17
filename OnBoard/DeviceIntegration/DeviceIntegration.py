from DeviceCommunication import DeviceCommunication
import time
from DeviceConfig import config

class DeviceIntegration(object):

    def __init__(self, config):
        self._devcom= DeviceCommunication.DeviceCommunication(config)


    def update(self):
        for key in config["Sensors"]:
            self._devcom.send(key, config["Sensors"][key].update())


if __name__ == "__main__":

    devint = DeviceIntegration(config)

    while True:
       devint.update()
       time.sleep(0.1)

