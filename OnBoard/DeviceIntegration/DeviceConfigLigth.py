from DriverComponent.ActuatorDrivers import LedIndicator
from DriverComponent.SensorDrivers import Fake
from DriverComponent.SensorDrivers import GY273
from DriverComponent.SensorDrivers import BMP
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


config = { "cycletime": 1,
           "Actuators": {
               "vehicle/comfort/bad": LedIndicator.LedIndicator(GPIO,16),
                "vehicle/comfort/ok": LedIndicator.LedIndicator(GPIO,20),
                "vehicle/comfort/good": LedIndicator.LedIndicator(GPIO,21),

},
          "Sensors":{
               # "bearing": GY273.GY273(),
                "cab/pressure": BMP.BMP(),
                # "comfort/bad": Fake.Red(),
                # "comfort/ok": Fake.Red(),
                # "comfort/good": Fake.Green(),
                   },
                    }