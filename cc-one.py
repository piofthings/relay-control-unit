#!/usr/bin/env python
from time import sleep
from uuid import getnode as get_mac
import paho.mqtt.client as mqtt
from gpiozero import DigitalOutputDevice
from common.payload import Payload;
from common.timeSync import TimeSync;
class RelayClient():
    relay1 = None
    relay2 = None
    client = None
    currentState = 'off'
    timeSync = TimeSync()


    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message


    def start(self):
        self.client.connect("localhost", 1883, 60)
        self.client.loop_forever()


    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        self.client.subscribe("/Relays")


    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        self.timeSync.sync()
        print(msg.topic+" "+str(msg.payload))
        payload = Payload(msg.payload)
        print("id:"+ str(payload.id))
        print("state:" + str(payload.state))
        if payload.state == 'on':
            print("turning on")
            if self.currentState == 'off':
                self.currentState = 'on'
                self.relay1 = DigitalOutputDevice(pin=17)
                self.relay1.on()
                self.relay2 = DigitalOutputDevice(pin=27)
                self.relay2.on()
        if payload.state == 'off':
            print("turning off")
            self.currentState = 'off'
            if self.relay1 is not None:
                self.relay1.close()
            else:
                print("self.relay1 is null")

            if self.relay2 is not None:
                self.relay2.close()
            else:
                print("self.relay2 is null")


def main():
    relayClient = RelayClient()
    relayClient.start()


if __name__ == '__main__':
    main()
