from DriverComponent.ActuatorDrivers import Comfort
from DriverComponent.SensorDrivers import Fake
from DriverComponent.SensorDrivers import GY273
from DriverComponent.SensorDrivers import BMP
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


config = { "cycletime": 0,
           "Actuators": {
               "vehicle/comfort": Comfort.Comfort(GPIO,16, 21),

},
          "Sensors":{
               # "bearing": GY273.GY273(),
                #"cab/pressure": BMP.BMP(),
                #"comfort": Fake.Red(),
                # "comfort/ok": Fake.Red(),
                # "comfort/good": Fake.Green(),
                   },
                    }