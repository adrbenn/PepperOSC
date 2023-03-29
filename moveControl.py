import pepperIP
import math
import time

from naoqi import ALProxy
def moveRC(robotIP, robotPort):
    motionProxy = ALProxy("ALMotion", robotIP, robotPort)
    postureProxy = ALProxy("ALRobotPosture", robotIP, robotPort)
    tts = ALProxy("ALTextToSpeech", robotIP, robotPort)

    keepMoving = True
    mvDistance = 1

    # wake up robot
    motionProxy.wakeUp()

    # robot do init pose
    postureProxy.goToPosture("Stand", 0.5)

    tts.say("I'm ready! Where do you want me to move?")

    while keepMoving:
        choices = promptRC()

        motionProxy.moveInit()
        motionProxy.setMotionConfig([["ENABLE_STIFFNESS_PROTECTION", False]])

        if choices == "w":
            motionProxy.post.moveTo(mvDistance, 0, 0, 2)
            tts.say("Moving forward")
            print("move forward")
        elif choices == "q":
            motionProxy.post.moveTo(0, 0, math.pi / 6, 2)
            tts.say("Turning left")
            print("turn left")
        elif choices == "e":
            motionProxy.post.moveTo(0, 0, -(math.pi / 6), 2)
            tts.say("Turning right")
            print("turn right")
        elif choices == "s":
            motionProxy.post.moveTo(-(mvDistance), 0, 0, 2)
            tts.say("Moving backward")
            print("move backward")
        elif choices == "a":
            motionProxy.post.moveTo(0, mvDistance/2, 0, 2)
            tts.say("Moving sideways to the left")
            print("move left")
        elif choices == "d":
            motionProxy.post.moveTo(0, -(mvDistance/2), 0, 2)
            tts.say("Moving sideways to the right")
            print("move right")
        elif choices == "o":
            tts.say("Ok, I'm going to sleep now. Bye!")
            motionProxy.rest()
            keepMoving = False
        else:
            print("Command unknown")

        time.sleep(0.5)
        motionProxy.setMotionConfig([["ENABLE_STIFFNESS_PROTECTION", True]])



def promptRC():
    moveInput = raw_input("Command : ")
    return moveInput

if __name__ == '__main__':
    moveRC(pepperIP.pepperIP, pepperIP.pepperPort)
