from DriverComponent.ActuatorDrivers import LedIndicator
from DriverComponent.SensorDrivers import GY521
from DriverComponent.SensorDrivers import DHT
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


config = { "cycletime": 1,
          "Actuators": {
                # "red", LedIndicator.LedIndicator(GPIO,16),
                # "yellow", LedIndicator.LedIndicator(GPIO,20)),
           },
          "Sensors":{
                    "cab/accx": GY521.accx(),
                    "cab/accy": GY521.accy(),
                    "cab/accz": GY521.accz()
                    },
                    }