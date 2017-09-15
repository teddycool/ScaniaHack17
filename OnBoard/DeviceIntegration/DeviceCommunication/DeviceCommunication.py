
from Publish import MqttPublish
from Subscribe import MqttSubscribe

class DeviceCommunication(object):

    def __init__(self, config):
        self._pub = MqttPublish()
        self._sub = {}
        for key in config["Actuators"]:
            self._sub[key] = MqttSubscribe(key)

    def send(self, key, value):
        self._pub.publish("sensors/" + key, value)

    def read(self, key):
       return self._sub[key].read()
