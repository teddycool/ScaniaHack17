from DriverComponent.ActuatorDrivers import LedIndicator
from DriverComponent.SensorDrivers import Fake
from DriverComponent.SensorDrivers import GY273
from DriverComponent.SensorDrivers import BMP
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


config = { "cycletime": 1,
           "Actuators": {
               "red": LedIndicator.LedIndicator(GPIO,16),
                "yellow": LedIndicator.LedIndicator(GPIO,20),
                "green": LedIndicator.LedIndicator(GPIO,21),

},
          "Sensors":{
          #      "bearing": GY273.GY273(),
                "pressure": BMP.BMP(),
                "red": Fake.Red(),
                "yellow": Fake.Red(),
                "green": Fake.Green(),
                   },
                    }