import time
class Red(object):

    def  __init__(self):
        self._lastChange = time.time()
        self._state = 1

    def update(self):
        if time.time() - self._lastChange > 2:
            if self._state == 1:
                self._state = 0
            else:
                self._state=1
        return self._state

class Green(object):

    def  __init__(self):
        self._lastChange = time.time()
        self._state = 1

    def update(self):
        if time.time() - self._lastChange > 2:
            if self._state == 1:
                self._state = 0
            else:
                self._state=1
        return not self._state
