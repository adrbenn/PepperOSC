# import time
import OSC
import PepperOSC_Config

osc_sound_client = OSC.OSCClient()
osc_sound_client.connect((PepperOSC_Config.soundIP, PepperOSC_Config.soundPort))


def osc_send_pepper_data(message):
    # TO THE SOUND SYNTH
    # print message
    global osc_sound_client
    pep_data = OSC.OSCMessage()
    pep_data.setAddress('/pepperdata')
    for i in message:
        msg = i
        pep_data.append(msg)
    # print pep_data
    osc_sound_client.send(pep_data)


def osc_send_sound_flag(osc_address, message):
    # SENDING FLAG TO sound
    global osc_sound_client
    flag_msg = OSC.OSCMessage()
    flag_msg.setAddress(osc_address)
    flag_msg.append(message)
    # print flag_msg
    osc_sound_client.send(flag_msg)