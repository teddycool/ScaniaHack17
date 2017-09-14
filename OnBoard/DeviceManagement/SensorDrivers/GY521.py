#!/usr/bin/python
#ACCELEROMETER
import smbus
import math
import time
import Queue
from mpu6050 import mpu6050
# prereqs: https://github.com/Tijndagamer/mpu6050

class GY521(object):

# Device interface
    def __init__(self, bus=1, adr=0x68):
        self._mpu=mpu6050(adr)
        self._accx


    def getAccelerometerdata(self):
        #Sensoraxis
        self._acel_data= self._mpu.get_accel_data()
        return self._acel_data

    #What is rotation in this scenario?
    def getRotation(self,  degrees=True):
        pass

    def getDown(self):
        x,y,z = self.getAccelerometerdata()
        absacc = (math.abs(1-x),math.abs(1-y),math.abs(1-z))
        #TODO...



    def _dist(self,a, b):
        return math.sqrt((a * a) + (b * b))


    def update(self):
        return self.getAccelerometerdata()


if __name__ == '__main__':
    gy=GY521()
    while 1:
        print "Accelerometer-data:"
        print gy.getAccelerometerdata()
        print "----------------------------------"
        time.sleep(1)