from DeviceCommunication import DeviceCommunication
import time
import argparse

class DeviceIntegration(object):

    def __init__(self, config):
        self._devcom= DeviceCommunication.DeviceCommunication(config)
        self._cycletime = config("cycletime")


    def update(self):
        for key in config["Sensors"]:
            self._devcom.send(key, config["Sensors"][key].update())


if __name__ == "__main__":
    config=None
    parser = argparse.ArgumentParser(description="configparser")
    parser.add_argument("config")
    args=parser.parse_args()

    exec("from " + args.config + " import config")

    devint = DeviceIntegration(config)
    while True:
       devint.update()
       time.sleep(config("cycletime"))

