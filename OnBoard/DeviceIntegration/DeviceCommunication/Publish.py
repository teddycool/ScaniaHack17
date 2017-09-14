#!/usr/bin/python
import paho.mqtt.client as paho
import time


class MqttPublish(object):

    def __init__(self):
        print "Init Publish..."
        self._client = paho.Client()
        self._client.on_publish = self._on_publish
        self._client.connect("10.0.0.201", 1883)
        self._client.loop_start()


    def _on_publish(self, client, userdata, mid):
        print("mid: " + str(mid))

    def publish(self, topic, userdata):
        (rc, mid) = self._client.publish(topic, userdata, qos=1)



if __name__ == "__main__":
    pub=MqttPublish()
    temperature = 0

    while True:
        pub.publish("vehicle/front/temperature", str(temperature))
        time.sleep(2)
        temperature = temperature +1