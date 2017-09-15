
import LedIndicator

class Comfort(object):

    def __init__(self, gpio, red, green):
        self._red = LedIndicator.LedIndicator(gpio,red)
        self._green = LedIndicator.LedIndicator(gpio, green)

    def actuate(self, value):
        print value
        self._red.ligth(False)
        self._green.ligth(False)
        if value > 3:
            self._red.ligth(True)
            self._green.ligth(False)
        elif value < 2:
            self._red.ligth(False)
            self._green.ligth(True)


