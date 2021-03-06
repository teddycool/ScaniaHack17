#!/usr/bin/python
import paho.mqtt.client as paho
import time


class MqttSubscribe(object):

    def __init__(self, topic):
        print "Init Subscribe..."
        self._client = paho.Client()
        self._client.on_subscribe = self.on_subscribe
        self._client.on_message = self.on_message
        self._client.connect("10.0.0.201", 1883)
        self._client.subscribe(topic , qos=1)
        self._client.loop_start()
        self._lastvalue = 0

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_message(self,client, userdata, msg):
        self._lastvalue = msg.payload
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    def read(self):
        return self._lastvalue


if __name__ == "__main__":
    pub=MqttSubscribe()
    temperature = 0

    while True:
        pub.publish("vehicle/front/temperature", str(temperature))
        time.sleep(2)
        temperature = temperature +1


