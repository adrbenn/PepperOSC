# PepperOSC

Bridging Pepper robot to sound synthesizing software (Pd, MaxMSP, SC) through OSC

Requirements:

Python 2.7

Pepper (NAOqi) SDK 2.5.10 - Python 2.7 SDK
Available here (under the "Old: Pepper SDK" header): 
https://www.aldebaran.com/en/support/pepper-naoqi-2-9/downloads-softwares

Contents:

PepperOSC files:

- PepperOSC_Config.py : Config for ip addresses, ports, and choosing streamed data

PepperOSC_MAIN.py : The main file to run. In the current version it asks for number input, corresponds to the built in the available animation/behaviour inside a Pepper robot (See PepperOSC_Config.py for the list of available animation). The animation/behaviour will be activated, while at the same time the joint data is being constantly streamed out as OSC messages.  

PepperOSC_PepperProxies.py : Contains the required functions to communicate with Pepper.
PepperOSC_OSC.py : Contains the required functions to send OSC messages, based on pyOSC.
pyOSC_OSC.py : Cloned from pyOSC, included here to ensure the availability.

Sound Models:
- MaxMSP: Requires Sound Design Toolkit package (see https://cycling74.com/forums/announcing-a-new-package-sound-design-toolkit)
- Pure Data
- SuperCollider
