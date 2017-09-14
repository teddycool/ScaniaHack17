
from Publish import MqttPublish
class DeviceCommunication(object):

    def __init__(self, config):
        self._pub = MqttPublish()

    def send(self, key, value):
        self._pub.publish("sensors/" + key, value)
