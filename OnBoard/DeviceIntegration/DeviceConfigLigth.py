from DriverComponent.ActuatorDrivers import LedIndicator
from DriverComponent.SensorDrivers import Red
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


config = { "cycletime": 1,
           "Actuators": {
               "red": LedIndicator.LedIndicator(GPIO,16),
                "yellow": LedIndicator.LedIndicator(GPIO,20),
},
          "Sensors":{
                "red": Red.Red(),
                "yellow": Red.Red()
                   },
                    }