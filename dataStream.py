# Stream of Pepper's sensor and actuator data
# To Pure Data with netsend
# To SuperCollider with OSC
# Python 2.7

from naoqi import ALProxy
import pepperIP
import time
import OSC
import os
# import serial
# import sys


# list of all possible data available here, add new entries in the list as needed
# http://doc.aldebaran.com/2-4/family/pepper_technical/pepper_dcm/actuator_sensor_names.html
ALMEMORY_KEY_NAMES = [
    "Device/SubDeviceList/LShoulderPitch/Position/Sensor/Value",
    "Device/SubDeviceList/RShoulderPitch/Position/Sensor/Value",
    "Device/SubDeviceList/HeadPitch/Position/Sensor/Value"
]

# to be accessed with ROUTE in Pd
def send2Pd(message):
    for i in message:
        msg = str(message.index(i)) + " " + str(i) + " "
        # print(msg)
        os.system("echo '" + msg + "' | pdsend 3000 localhost udp")


# sending an OSC stream
def send2SC(message):
    client = OSC.OSCClient()
    client.connect(('localhost', 3001))
    addr = '/pepper'
    pepper = OSC.OSCMessage()
    pepper.setAddress(addr)
    for i in message:
        msg = i
        pepper.append(float(msg))
    print(pepper)
    client.send(pepper)


def streamData(robot_ip, robot_port):
    print("Getting data ... ")
    memory = ALProxy("ALMemory", robot_ip, robot_port)
    # data = list()

    # stream continuously, have to be manually stopped
    while True:
        line = list()
        for key in ALMEMORY_KEY_NAMES:
            value = memory.getData(key)
            line.append(value)
        #print(line)           # to check what's in the list
        send2Pd(line)         # send list to Pure Data
        send2SC(line)           # send list to SuperCollider

        # data.append(line)     # use when a chunk of data within a time period is needed
        time.sleep(0.5)        # delay between reading, in second

if __name__ == '__main__':
    streamData(pepperIP.pepperIP, pepperIP.pepperPort)