# CONFIG

# the robot
# pepperIP = "130.237.2.7"
pepperIP = "192.168.100.223"
pepperPort = 9559


# target machine where the sound synthesis software is
soundIP = "192.168.100.126"
soundPort = 3005

# Pepper's Data
# Details available here
# http://doc.aldebaran.com/2-5/family/pepper_technical/joints_pep.html
BodyPartList = [
    "HeadPitch",        # top-down
    "HeadYaw",          # left-right

    "RShoulderRoll",    # to the side
    "RShoulderPitch",   # hand forward
    "RElbowYaw",        # elbow rotation
    "RElbowRoll",       # elbow bent
    "RWristYaw",        # wrist rotation
    "RHand",            # hand open/close

    "LShoulderRoll",    # to the side
    "LShoulderPitch",   # hand forward
    "LElbowYaw",        # elbow rotation
    "LElbowRoll",       # elbow bent
    "LWristYaw",        # wrist rotation
    "LHand"             # hand open/close
]

DataTypeList = [
    "PositionSensor",       # in rad, except for LHand and RHand in %
    # "ElectricCurrent",      # in A
    # "TemperatureValue",     # in degree C
    # "Hardness"              # in %
]
DataTypeKeys = [
    "/Position/Sensor/Value",
    # "/ElectricCurrent/Sensor/Value",
    # "/Temperature/Sensor/Value",
    # "/Hardness/Actuator/Value"
]


# list of Pepper robot's built-in movements
animation_names = ["animations/Stand/BodyTalk/Listening/Listening_1",   # 0
                   "animations/Stand/BodyTalk/Listening/Listening_2",   # 1
                   "animations/Stand/BodyTalk/Listening/Listening_3",   # 2
                   "animations/Stand/BodyTalk/Listening/Listening_4",   # 3
                   "animations/Stand/BodyTalk/Listening/Listening_5",   # 4
                   "animations/Stand/BodyTalk/Listening/Listening_6",   # 5
                   "animations/Stand/BodyTalk/Listening/Listening_7",   # 6
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_1",     # 7
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_10",    # 8
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_11",    # 9
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_12",    # 10
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_13",    #
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_14",    #
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_15",    #
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_16",    #
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_2",     # 15
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_3",     #
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_4",     #
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_5",     #
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_6",     #
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_7",     # 20
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_8",     #
                   "animations/Stand/BodyTalk/Speaking/BodyTalk_9",     #
                   "animations/Stand/BodyTalk/Thinking/Remember_1",     #
                   "animations/Stand/BodyTalk/Thinking/Remember_2",     #
                   "animations/Stand/BodyTalk/Thinking/Remember_3",     # 25
                   "animations/Stand/BodyTalk/Thinking/ThinkingLoop_1",  #
                   "animations/Stand/BodyTalk/Thinking/ThinkingLoop_2",  #
                   "animations/Stand/Emotions/Negative/Angry_1",        #
                   "animations/Stand/Emotions/Negative/Angry_2",        #
                   "animations/Stand/Emotions/Negative/Angry_3",        # 30
                   "animations/Stand/Emotions/Negative/Angry_4",        #
                   "animations/Stand/Emotions/Negative/Anxious_1",      #
                   "animations/Stand/Emotions/Negative/Bored_1",        #
                   "animations/Stand/Emotions/Negative/Bored_2",        #
                   "animations/Stand/Emotions/Negative/Disappointed_1",  # 35
                   "animations/Stand/Emotions/Negative/Exhausted_1",    #
                   "animations/Stand/Emotions/Negative/Exhausted_2",    #
                   "animations/Stand/Emotions/Negative/Fear_1",         #
                   "animations/Stand/Emotions/Negative/Fear_2",         #
                   "animations/Stand/Emotions/Negative/Fearful_1",      # 40
                   "animations/Stand/Emotions/Negative/Frustrated_1",   #
                   "animations/Stand/Emotions/Negative/Humiliated_1",   #
                   "animations/Stand/Emotions/Negative/Hurt_1",         #
                   "animations/Stand/Emotions/Negative/Hurt_2",         #
                   "animations/Stand/Emotions/Negative/Late_1",         # 45
                   "animations/Stand/Emotions/Negative/Sad_1",          #
                   "animations/Stand/Emotions/Negative/Sad_2",          #
                   "animations/Stand/Emotions/Negative/Shocked_1",      #
                   "animations/Stand/Emotions/Negative/Sorry_1",        #
                   "animations/Stand/Emotions/Negative/Surprise_1",     # 50
                   "animations/Stand/Emotions/Negative/Surprise_2",     #
                   "animations/Stand/Emotions/Negative/Surprise_3",     #
                   "animations/Stand/Emotions/Neutral/Alienated_1",     #
                   "animations/Stand/Emotions/Neutral/AskForAttention_1",  #
                   "animations/Stand/Emotions/Neutral/AskForAttention_2",  # 55
                   "animations/Stand/Emotions/Neutral/AskForAttention_3",  #
                   "animations/Stand/Emotions/Neutral/Cautious_1",      #
                   "animations/Stand/Emotions/Neutral/Confused_1",      #
                   "animations/Stand/Emotions/Neutral/Determined_1",    #
                   "animations/Stand/Emotions/Neutral/Embarrassed_1",   # 60
                   "animations/Stand/Emotions/Neutral/Hesitation_1",    #
                   "animations/Stand/Emotions/Neutral/Innocent_1",      #
                   "animations/Stand/Emotions/Neutral/Lonely_1",        #
                   "animations/Stand/Emotions/Neutral/Mischievous_1",   #
                   "animations/Stand/Emotions/Neutral/Puzzled_1",       # 65
                   "animations/Stand/Emotions/Neutral/Sneeze",          #
                   "animations/Stand/Emotions/Neutral/Stubborn_1",      #
                   "animations/Stand/Emotions/Neutral/Suspicious_1",    #
                   "animations/Stand/Emotions/Positive/Amused_1",       #
                   "animations/Stand/Emotions/Positive/Confident_1",    # 70
                   "animations/Stand/Emotions/Positive/Ecstatic_1",     #
                   "animations/Stand/Emotions/Positive/Enthusiastic_1",  #
                   "animations/Stand/Emotions/Positive/Excited_1",      #
                   "animations/Stand/Emotions/Positive/Excited_2",      #
                   "animations/Stand/Emotions/Positive/Excited_3",      # 75
                   "animations/Stand/Emotions/Positive/Happy_1",        #
                   "animations/Stand/Emotions/Positive/Happy_2",        #
                   "animations/Stand/Emotions/Positive/Happy_3",        #
                   "animations/Stand/Emotions/Positive/Happy_4",        #
                   "animations/Stand/Emotions/Positive/Hungry_1",       # 80
                   "animations/Stand/Emotions/Positive/Hysterical_1",   #
                   "animations/Stand/Emotions/Positive/Interested_1",   #
                   "animations/Stand/Emotions/Positive/Interested_2",   #
                   "animations/Stand/Emotions/Positive/Laugh_1",        #
                   "animations/Stand/Emotions/Positive/Laugh_2",        # 85
                   "animations/Stand/Emotions/Positive/Laugh_3",        #
                   "animations/Stand/Emotions/Positive/Mocker_1",       #
                   "animations/Stand/Emotions/Positive/Optimistic_1",   #
                   "animations/Stand/Emotions/Positive/Peaceful_1",     #
                   "animations/Stand/Emotions/Positive/Proud_1",        # 90
                   "animations/Stand/Emotions/Positive/Proud_2",        #
                   "animations/Stand/Emotions/Positive/Proud_3",        #
                   "animations/Stand/Emotions/Positive/Relieved_1",     #
                   "animations/Stand/Emotions/Positive/Shy_1",          #
                   "animations/Stand/Emotions/Positive/Shy_2",          # 95
                   "animations/Stand/Emotions/Positive/Sure_1",         #
                   "animations/Stand/Emotions/Positive/Winner_1",       #
                   "animations/Stand/Emotions/Positive/Winner_2",       #
                   "animations/Stand/Gestures/Angry_1",                 #
                   "animations/Stand/Gestures/Angry_2",                 # 100
                   "animations/Stand/Gestures/Angry_3",                 #
                   "animations/Stand/Gestures/BowShort_1",              #
                   "animations/Stand/Gestures/BowShort_2",              #
                   "animations/Stand/Gestures/BowShort_3",              #
                   "animations/Stand/Gestures/But_1",                   # 105
                   "animations/Stand/Gestures/CalmDown_1",              #
                   "animations/Stand/Gestures/CalmDown_2",              #
                   "animations/Stand/Gestures/CalmDown_3",              #
                   "animations/Stand/Gestures/CalmDown_4",              #
                   "animations/Stand/Gestures/CalmDown_5",              # 110
                   "animations/Stand/Gestures/CalmDown_6",              #
                   "animations/Stand/Gestures/Choice_1",                #
                   "animations/Stand/Gestures/ComeOn_1",                #
                   "animations/Stand/Gestures/Confused_1",              #
                   "animations/Stand/Gestures/Confused_2",              # 115
                   "animations/Stand/Gestures/CountFive_1",             #
                   "animations/Stand/Gestures/CountFour_1",             #
                   "animations/Stand/Gestures/CountMore_1",             #
                   "animations/Stand/Gestures/CountOne_1",              #
                   "animations/Stand/Gestures/CountThree_1",            # 120
                   "animations/Stand/Gestures/CountTwo_1",              #
                   "animations/Stand/Gestures/Desperate_1",             #
                   "animations/Stand/Gestures/Desperate_2",             #
                   "animations/Stand/Gestures/Desperate_3",             #
                   "animations/Stand/Gestures/Desperate_4",             # 125
                   "animations/Stand/Gestures/Desperate_5",             #
                   "animations/Stand/Gestures/DontUnderstand_1",        #
                   "animations/Stand/Gestures/Enthusiastic_3",          #
                   "animations/Stand/Gestures/Enthusiastic_4",          #
                   "animations/Stand/Gestures/Enthusiastic_5",          # 130
                   "animations/Stand/Gestures/Everything_1",            #
                   "animations/Stand/Gestures/Everything_2",            #
                   "animations/Stand/Gestures/Everything_3",            #
                   "animations/Stand/Gestures/Everything_4",            #
                   "animations/Stand/Gestures/Everything_6",            # 135
                   "animations/Stand/Gestures/Excited_1",               #
                   "animations/Stand/Gestures/Explain_1",               #
                   "animations/Stand/Gestures/Explain_10",              #
                   "animations/Stand/Gestures/Explain_11",              #
                   "animations/Stand/Gestures/Explain_2",               # 140
                   "animations/Stand/Gestures/Explain_3",               #
                   "animations/Stand/Gestures/Explain_4",               #
                   "animations/Stand/Gestures/Explain_5",               #
                   "animations/Stand/Gestures/Explain_6",               #
                   "animations/Stand/Gestures/Explain_7",               # 145
                   "animations/Stand/Gestures/Explain_8",               #
                   "animations/Stand/Gestures/Far_1",                   #
                   "animations/Stand/Gestures/Far_2",                   #
                   "animations/Stand/Gestures/Far_3",  #
                   "animations/Stand/Gestures/Follow_1",  # 150
                   "animations/Stand/Gestures/Give_1",  #
                   "animations/Stand/Gestures/Give_2",  #
                   "animations/Stand/Gestures/Give_3",  #
                   "animations/Stand/Gestures/Give_4",  #
                   "animations/Stand/Gestures/Give_5",  # 155
                   "animations/Stand/Gestures/Give_6",  #
                   "animations/Stand/Gestures/Great_1",  #
                   "animations/Stand/Gestures/HeSays_1",  #
                   "animations/Stand/Gestures/HeSays_2",  #
                   "animations/Stand/Gestures/HeSays_3",  # 160
                   "animations/Stand/Gestures/Hey_1",  #
                   "animations/Stand/Gestures/Hey_10",  #
                   "animations/Stand/Gestures/Hey_2",  #
                   "animations/Stand/Gestures/Hey_3",  #
                   "animations/Stand/Gestures/Hey_4",  # 165
                   "animations/Stand/Gestures/Hey_6",  #
                   "animations/Stand/Gestures/Hey_7",  #
                   "animations/Stand/Gestures/Hey_8",  #
                   "animations/Stand/Gestures/Hey_9",  #
                   "animations/Stand/Gestures/Hide_1",  # 170
                   "animations/Stand/Gestures/Hot_1",  #
                   "animations/Stand/Gestures/Hot_2",  #
                   "animations/Stand/Gestures/IDontKnow_1",  #
                   "animations/Stand/Gestures/IDontKnow_2",  #
                   "animations/Stand/Gestures/IDontKnow_3",  # 175
                   "animations/Stand/Gestures/IDontKnow_4",  #
                   "animations/Stand/Gestures/IDontKnow_5",  #
                   "animations/Stand/Gestures/IDontKnow_6",  #
                   "animations/Stand/Gestures/Joy_1",  #
                   "animations/Stand/Gestures/Kisses_1",  # 180
                   "animations/Stand/Gestures/Look_1",  #
                   "animations/Stand/Gestures/Look_2",  #
                   "animations/Stand/Gestures/Maybe_1",  #
                   "animations/Stand/Gestures/Me_1",  #
                   "animations/Stand/Gestures/Me_2",  # 185
                   "animations/Stand/Gestures/Me_4",  #
                   "animations/Stand/Gestures/Me_7",  #
                   "animations/Stand/Gestures/Me_8",  #
                   "animations/Stand/Gestures/Mime_1",  #
                   "animations/Stand/Gestures/Mime_2",  # 190
                   "animations/Stand/Gestures/Next_1",  #
                   "animations/Stand/Gestures/No_1",  #
                   "animations/Stand/Gestures/No_2",  #
                   "animations/Stand/Gestures/No_3",  #
                   "animations/Stand/Gestures/No_4",  # 195
                   "animations/Stand/Gestures/No_5",  #
                   "animations/Stand/Gestures/No_6",  #
                   "animations/Stand/Gestures/No_7",  #
                   "animations/Stand/Gestures/No_8",  #
                   "animations/Stand/Gestures/No_9",  # 200
                   "animations/Stand/Gestures/Nothing_1",  #
                   "animations/Stand/Gestures/Nothing_2",  #
                   "animations/Stand/Gestures/OnTheEvening_1",  #
                   "animations/Stand/Gestures/OnTheEvening_2",  #
                   "animations/Stand/Gestures/OnTheEvening_3",  # 205
                   "animations/Stand/Gestures/OnTheEvening_4",  #
                   "animations/Stand/Gestures/OnTheEvening_5",  #
                   "animations/Stand/Gestures/Please_1",  #
                   "animations/Stand/Gestures/Please_2",  #
                   "animations/Stand/Gestures/Please_3",  # 210
                   "animations/Stand/Gestures/Reject_1",  #
                   "animations/Stand/Gestures/Reject_2",  #
                   "animations/Stand/Gestures/Reject_3",  #
                   "animations/Stand/Gestures/Reject_4",  #
                   "animations/Stand/Gestures/Reject_5",  # 215
                   "animations/Stand/Gestures/Reject_6",  #
                   "animations/Stand/Gestures/Salute_1",  #
                   "animations/Stand/Gestures/Salute_2",  #
                   "animations/Stand/Gestures/Salute_3",  #
                   "animations/Stand/Gestures/ShowFloor_1",  # 220
                   "animations/Stand/Gestures/ShowFloor_2",  #
                   "animations/Stand/Gestures/ShowFloor_3",  #
                   "animations/Stand/Gestures/ShowFloor_4",  #
                   "animations/Stand/Gestures/ShowFloor_5",  #
                   "animations/Stand/Gestures/ShowSky_1",  # 225
                   "animations/Stand/Gestures/ShowSky_10",  #
                   "animations/Stand/Gestures/ShowSky_11",  #
                   "animations/Stand/Gestures/ShowSky_12",  #
                   "animations/Stand/Gestures/ShowSky_2",  #
                   "animations/Stand/Gestures/ShowSky_3",  # 230
                   "animations/Stand/Gestures/ShowSky_4",  #
                   "animations/Stand/Gestures/ShowSky_5",  #
                   "animations/Stand/Gestures/ShowSky_6",  #
                   "animations/Stand/Gestures/ShowSky_7",  #
                   "animations/Stand/Gestures/ShowSky_8",  # 235
                   "animations/Stand/Gestures/ShowSky_9",  #
                   "animations/Stand/Gestures/ShowTablet_1",  #
                   "animations/Stand/Gestures/ShowTablet_2",  #
                   "animations/Stand/Gestures/ShowTablet_3",  #
                   "animations/Stand/Gestures/Shy_1",  # 240
                   "animations/Stand/Gestures/Stretch_1",  #
                   "animations/Stand/Gestures/Stretch_2",  #
                   "animations/Stand/Gestures/Surprised_1",  #
                   "animations/Stand/Gestures/Take_1",  #
                   "animations/Stand/Gestures/TakePlace_1",  # 245
                   "animations/Stand/Gestures/TakePlace_2",  #
                   "animations/Stand/Gestures/Thinking_1",  #
                   "animations/Stand/Gestures/Thinking_2",  #
                   "animations/Stand/Gestures/Thinking_3",  #
                   "animations/Stand/Gestures/Thinking_4",  # 250
                   "animations/Stand/Gestures/Thinking_5",  #
                   "animations/Stand/Gestures/Thinking_6",  #
                   "animations/Stand/Gestures/Thinking_7",  #
                   "animations/Stand/Gestures/Thinking_8",  #
                   "animations/Stand/Gestures/This_1",  # 255
                   "animations/Stand/Gestures/This_10",  #
                   "animations/Stand/Gestures/This_11",  #
                   "animations/Stand/Gestures/This_12",  #
                   "animations/Stand/Gestures/This_13",  #
                   "animations/Stand/Gestures/This_14",  # 260
                   "animations/Stand/Gestures/This_15",  #
                   "animations/Stand/Gestures/This_2",  #
                   "animations/Stand/Gestures/This_3",  #
                   "animations/Stand/Gestures/This_4",  #
                   "animations/Stand/Gestures/This_5",  # 265
                   "animations/Stand/Gestures/This_6",  #
                   "animations/Stand/Gestures/This_7",  #
                   "animations/Stand/Gestures/This_8",  #
                   "animations/Stand/Gestures/This_9",  #
                   "animations/Stand/Gestures/WhatSThis_1",  # 270
                   "animations/Stand/Gestures/WhatSThis_10",  #
                   "animations/Stand/Gestures/WhatSThis_11",  #
                   "animations/Stand/Gestures/WhatSThis_12",  #
                   "animations/Stand/Gestures/WhatSThis_13",  #
                   "animations/Stand/Gestures/WhatSThis_14",  # 275
                   "animations/Stand/Gestures/WhatSThis_15",  #
                   "animations/Stand/Gestures/WhatSThis_16",  #
                   "animations/Stand/Gestures/WhatSThis_2",  #
                   "animations/Stand/Gestures/WhatSThis_3",  #
                   "animations/Stand/Gestures/WhatSThis_4",  # 280
                   "animations/Stand/Gestures/WhatSThis_5",  #
                   "animations/Stand/Gestures/WhatSThis_6",  #
                   "animations/Stand/Gestures/WhatSThis_7",  #
                   "animations/Stand/Gestures/WhatSThis_8",  #
                   "animations/Stand/Gestures/WhatSThis_9",  # 285
                   "animations/Stand/Gestures/Whisper_1",  #
                   "animations/Stand/Gestures/Wings_1",  #
                   "animations/Stand/Gestures/Wings_2",  #
                   "animations/Stand/Gestures/Wings_3",  #
                   "animations/Stand/Gestures/Wings_4",  # 290
                   "animations/Stand/Gestures/Wings_5",  #
                   "animations/Stand/Gestures/Yes_1",  #
                   "animations/Stand/Gestures/Yes_2",  #
                   "animations/Stand/Gestures/Yes_3",  #
                   "animations/Stand/Gestures/You_1",  # 295
                   "animations/Stand/Gestures/You_2",  #
                   "animations/Stand/Gestures/You_3",  #
                   "animations/Stand/Gestures/You_4",  #
                   "animations/Stand/Gestures/You_5",  #
                   "animations/Stand/Gestures/YouKnowWhat_1",  # 300
                   "animations/Stand/Gestures/YouKnowWhat_2",  #
                   "animations/Stand/Gestures/YouKnowWhat_3",  #
                   "animations/Stand/Gestures/YouKnowWhat_4",  #
                   "animations/Stand/Gestures/YouKnowWhat_5",  #
                   "animations/Stand/Gestures/YouKnowWhat_6",  # 305
                   "animations/Stand/Gestures/Yum_1",  #
                   "animations/Stand/Waiting/AirGuitar_1",  #
                   "animations/Stand/Waiting/BackRubs_1",  #
                   "animations/Stand/Waiting/Bandmaster_1",  #
                   "animations/Stand/Waiting/Binoculars_1",  # 310
                   "animations/Stand/Waiting/BreathLoop_1",  #
                   "animations/Stand/Waiting/BreathLoop_2",  #
                   "animations/Stand/Waiting/BreathLoop_3",  #
                   "animations/Stand/Waiting/CallSomeone_1",  #
                   "animations/Stand/Waiting/Drink_1",  # 315
                   "animations/Stand/Waiting/DriveCar_1",  #
                   "animations/Stand/Waiting/Fitness_1",  #
                   "animations/Stand/Waiting/Fitness_2",  #
                   "animations/Stand/Waiting/Fitness_3",  #
                   "animations/Stand/Waiting/FunnyDancer_1",  # 320
                   "animations/Stand/Waiting/HappyBirthday_1",  #
                   "animations/Stand/Waiting/Helicopter_1",  #
                   "animations/Stand/Waiting/HideEyes_1",  #
                   "animations/Stand/Waiting/HideHands_1",  #
                   "animations/Stand/Waiting/Innocent_1",  # 325
                   "animations/Stand/Waiting/Knight_1",  #
                   "animations/Stand/Waiting/KnockEye_1",  #
                   "animations/Stand/Waiting/KungFu_1",  #
                   "animations/Stand/Waiting/LookHand_1",  #
                   "animations/Stand/Waiting/LookHand_2",  # 330
                   "animations/Stand/Waiting/LoveYou_1",  #
                   "animations/Stand/Waiting/Monster_1",  #
                   "animations/Stand/Waiting/MysticalPower_1",  #
                   "animations/Stand/Waiting/PlayHands_1",  #
                   "animations/Stand/Waiting/PlayHands_2",  # 335
                   "animations/Stand/Waiting/PlayHands_3",  #
                   "animations/Stand/Waiting/Relaxation_1",  #
                   "animations/Stand/Waiting/Relaxation_2",  #
                   "animations/Stand/Waiting/Relaxation_3",  #
                   "animations/Stand/Waiting/Relaxation_4",  # 340
                   "animations/Stand/Waiting/Rest_1",  #
                   "animations/Stand/Waiting/Robot_1",  #
                   "animations/Stand/Waiting/ScratchBack_1",  #
                   "animations/Stand/Waiting/ScratchBottom_1",  #
                   "animations/Stand/Waiting/ScratchEye_1",  # 345
                   "animations/Stand/Waiting/ScratchHand_1",  #
                   "animations/Stand/Waiting/ScratchHead_1",  #
                   "animations/Stand/Waiting/ScratchLeg_1",  #
                   "animations/Stand/Waiting/ScratchTorso_1",  #
                   "animations/Stand/Waiting/ShowMuscles_1",  # 350
                   "animations/Stand/Waiting/ShowMuscles_2",  #
                   "animations/Stand/Waiting/ShowMuscles_3",  #
                   "animations/Stand/Waiting/ShowMuscles_4",  #
                   "animations/Stand/Waiting/ShowMuscles_5",  #
                   "animations/Stand/Waiting/ShowSky_1",  # 355
                   "animations/Stand/Waiting/ShowSky_2",  #
                   "animations/Stand/Waiting/SpaceShuttle_1",  #
                   "animations/Stand/Waiting/Stretch_1",  #
                   "animations/Stand/Waiting/Stretch_2",  #
                   "animations/Stand/Waiting/TakePicture_1",  # 360
                   "animations/Stand/Waiting/Taxi_1",  #
                   "animations/Stand/Waiting/Think_1",  #
                   "animations/Stand/Waiting/Think_2",  #
                   "animations/Stand/Waiting/Think_3",  #
                   "animations/Stand/Waiting/Think_4",  # 365
                   "animations/Stand/Waiting/Waddle_1",  #
                   "animations/Stand/Waiting/Waddle_2",  #
                   "animations/Stand/Waiting/WakeUp_1",  #
                   "animations/Stand/Waiting/Zombie_1"]                # 369
