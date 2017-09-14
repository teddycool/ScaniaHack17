#!/usr/bin/python
#ACCELEROMETER
import smbus
import math
import time
import Queue
from collections import deque
from mpu6050 import mpu6050
# prereqs: https://github.com/Tijndagamer/mpu6050

class GY521(object):

# Device interface
    def __init__(self, bus=1, adr=0x68):
        self._mpu=mpu6050(adr)
        self._xlist = deque([0,0,0],3)
        self._ylist = deque([0, 0, 0], 3)

    def getAccelerometerdata(self):
        #Sensoraxis
        self._acel_data= self._mpu.get_accel_data()
        x= self._acel_data['x']
        self._xlist.append(x)
        xavg = reduce(lambda x, y: x + y, self._xlist) / len(self._xlist)

        return xavg




if __name__ == '__main__':
    gy=GY521()
    while 1:
        print "Accelerometer-data:"
        print gy.getAccelerometerdata()
        print "----------------------------------"
        time.sleep(0.1)