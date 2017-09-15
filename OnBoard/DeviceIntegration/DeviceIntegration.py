from DeviceCommunication import DeviceCommunication
import time
import argparse

class DeviceIntegration(object):

    def __init__(self, config):
        self._lastSend=time.time()
        self._devcom= DeviceCommunication.DeviceCommunication(config)
        self._values={}
        for key in config["Sensors"]:
            self._values[key]=[]


    def update(self):
        for key in config["Sensors"]:
            self._values[key].append(config["Sensors"][key].update())


        if time.time()-self._lastSend > config["cycletime"]:
            self._lastSend = time.time()
            for key in config["Sensors"]:
                avg = reduce(lambda x, y: x + y, self._values[key]) / len(self._values[key])
                self._devcom.send(key, avg)
                self._values[key] = []

        for key in config["Actuators"]:
            config["Actuators"][key].actuate(self._devcom.read(key))



if __name__ == "__main__":
    config=None
    parser = argparse.ArgumentParser(description="configparser")
    parser.add_argument("config")
    args=parser.parse_args()

    exec("from " + args.config + " import config")

    devint = DeviceIntegration(config)
    while True:
       devint.update()
       time.sleep(config["cycletime"])

