from DriverComponent.ActuatorDrivers import LedIndicator
from DriverComponent.SensorDrivers import GY521
from DriverComponent.SensorDrivers import DHT
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


config = {#"Actuators": [("red", LedIndicator.LedIndicator(GPIO,16)),("yellow", LedIndicator.LedIndicator(GPIO,20))],
          "Sensors":{
                    "accx": GY521.accx(),
                    "accy": GY521.accy(),
                    "accz": GY521.accz()
                    },
                    }