
from DriverComponent.SensorDrivers import DHT
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


config = { "cycletime": 2,
           "Actuators": [
               #   "red", LedIndicator.LedIndicator(GPIO,16)),
               #   "yellow", LedIndicator.LedIndicator(GPIO,20),
           ],
          "Sensors":{
                      "cargo/temp": DHT.DHT("11",21),
                    }
            }