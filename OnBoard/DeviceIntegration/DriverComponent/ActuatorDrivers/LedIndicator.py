__author__ = 'teddycool'
import time

class LedIndicator(object):
    def __init__(self, GPIO, controlpin):
        self._gpio = GPIO
        self._pin = controlpin
        self._gpio.setup(self._pin,self._gpio.OUT, initial=0)
        print "LedIndicator object created for IO: " + str(self._pin)

    def ligth(self, on= True):
        self._gpio.output(self._pin, on)



    def __del__(self):
        self.ligth(False)
        print "LedIndicator object deactivated and deleted for IO: " + str(self._pin)


if __name__ == '__main__':
    print "Testcode for LedIndicators"
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    led1 = LedIndicator(GPIO, 16)
    led2 = LedIndicator(GPIO, 20)
    led3 = LedIndicator(GPIO, 21)




    GPIO.cleanup()