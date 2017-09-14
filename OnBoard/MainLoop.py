__author__ = 'teddycool'
#State-switching and handling of general rendering

import time

#Global GPIO used by all...
import RPi.GPIO as GPIO

class MainLoop(object):
    def __init__(self):
        self._gpio= GPIO

    def initialize(self):
        print "Mainloop initialize"
        self._lastStateChange = time.time()

    def update(self):
        pass
        #self._currentState.update()
        #TODO: improve statemachine



    def __del__(self):
        self._gpio.cleanup()
        print "MainLoop cleaned up"


