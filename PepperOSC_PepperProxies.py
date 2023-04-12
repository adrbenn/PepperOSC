import time
from naoqi import ALProxy

import PepperOSC_Config
import PepperOSC_OSC

# ALProxy init
posture_proxy = ALProxy("ALRobotPosture", PepperOSC_Config.pepperIP, PepperOSC_Config.pepperPort)
behavior_proxy = ALProxy("ALBehaviorManager", PepperOSC_Config.pepperIP, PepperOSC_Config.pepperPort)
tts_proxy = ALProxy("ALTextToSpeech", PepperOSC_Config.pepperIP, PepperOSC_Config.pepperPort)
awareness_proxy = ALProxy("ALBasicAwareness", PepperOSC_Config.pepperIP, PepperOSC_Config.pepperPort)
# autonomous_proxy = ALProxy("ALAutonomousLife", PepperOSC_Config.pepperIP, PepperOSC_Config.pepperPort)
memory_proxy = ALProxy("ALMemory", PepperOSC_Config.pepperIP, PepperOSC_Config.pepperPort)


# To be called during the program initiation
def pepper_pause_awareness():
    global awareness_proxy
    awareness_proxy.pauseAwareness()
    awareness_proxy.setEnabled(False)
    print("Pepper's passive awareness is OFF")


# To be called at the end of the program
def pepper_resume_awareness():
    global awareness_proxy
    awareness_proxy.setEnabled(True)
    awareness_proxy.resumeAwareness()
    print("Pepper's passive awareness is back ON")


# When Pepper needs to say something
def pepper_say(utterance):
    global tts_proxy
    tts_proxy.setParameter("speed", 80)
    tts_proxy.say(utterance)


# When Pepper needs to go to the standing posture
def pepper_stand():
    global posture_proxy
    posture_proxy.goToPosture("Stand", 0.5)
    time.sleep(0.2)


# Main function: running Pepper behavior
def pepper_run_behavior(behavior_index):
    # pepper_stand()
    behavior_name = PepperOSC_Config.animation_names[behavior_index]
    global behavior_proxy

    # check that the behavior exists
    if behavior_proxy.isBehaviorInstalled(behavior_name):
        # check that it is not already running
        if not behavior_proxy.isBehaviorRunning(behavior_name):
            print("Start running animation" + behavior_name)
            behavior_proxy.runBehavior(behavior_name)
            time.sleep(0.4)
        else:
            print("Animation is already running")
    else:
        print("Animation not found")


# Main function: streaming joint data
def pepper_data_stream(prev_time):
    global memory_proxy
    memory_proxy = ALProxy("ALMemory", PepperOSC_Config.pepperIP, PepperOSC_Config.pepperPort)
    for index_body in range(len(PepperOSC_Config.BodyPartList)):
        for index_data in range(len(PepperOSC_Config.DataTypeList)):
            key = "Device/SubDeviceList/" \
                  + PepperOSC_Config.BodyPartList[index_body] \
                  + PepperOSC_Config.DataTypeKeys[index_data]
            # print key
            # print memory_proxy.getData(key)
            PepperOSC_OSC.osc_send_pepper_data(["/" + PepperOSC_Config.BodyPartList[index_body],
                                                      "/" + PepperOSC_Config.DataTypeList[index_data],
                                                      memory_proxy.getData(key)])
    cur_time = time.time()
    latency = cur_time - prev_time
    PepperOSC_OSC.osc_send_pepper_data(["/latency", latency])


# Check if any behavior is running
def pepper_whats_running():
    global behavior_proxy
    # behavior_proxy = ALProxy("ALBehaviorManager", PolitePepper_config.pepperIP, PolitePepper_config.pepperPort)
    running_names = behavior_proxy.getRunningBehaviors()
    return running_names


# Debugging purpose
def pepper_available_behavior():
    global behavior_proxy
    # behavior_proxy = ALProxy("ALBehaviorManager", PolitePepper_config.pepperIP, PolitePepper_config.pepperPort)
    available_names = behavior_proxy.getInstalledBehaviors()
    for i in available_names:
        print i


# Debugging purpose
def pepper_test_behavior(behavior_name):
    global behavior_proxy
    # check that the behavior exists
    if behavior_proxy.isBehaviorInstalled(behavior_name):
        # check that it is not already running
        if not behavior_proxy.isBehaviorRunning(behavior_name):
            print("Start running behavior" + behavior_name)
            behavior_proxy.runBehavior(behavior_name)
            time.sleep(0.4)
        else:
            print("Behavior is already running")
    else:
        print("Behavior not found")


if __name__ == '__main__':
    print "Connecting..."
    start_time = time.time()
    pepper_pause_awareness()
    time.sleep(1)
    pepper_say("Hello! I am connected and ready.")
    time.sleep(1)
    pepper_say("But this is not the correct Python file to run. Please run Pepper O S C Main.")
    pepper_stand()
    pepper_resume_awareness()
    end_time = time.time()
    print("Runtime : " + str(end_time - start_time))