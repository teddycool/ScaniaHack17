import DriverComponent.SensorDrivers.GY521 as GY521
import DeviceCommunication.Publish as Publish
import time
class DeviceIntegration(object):

    def __init__(self):
        self._acc = GY521.GY521()
        self._pub = Publish.MqttPublish()


    def update(self):
        accel_data = self._acc.getAccelerometerdata()

        self._pub.publish("vehicle/front/temperature", str(accel_data))




if __name__ == "__main__":
    devint = DeviceIntegration()

    while True:
       devint.update()
       time.sleep(0.1)

