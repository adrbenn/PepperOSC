# Initiate Pepper's behavior and capturing the movement data through OSC

import threading
import time
import keyboard

import PepperOSC_Config
import PepperOSC_OSC
import PepperOSC_PepperProxies

stop_threads = False


# Thread 1
# Ask for behavior choice (and validate)
# Run the chosen behavior and flag the sound On
# When behavior stop, flag the sound off
# Repeat
def run_thread_pepper_control():
    print ("Thread 1 ON - Pepper behavior control")
    max_choice = int(len(PepperOSC_Config.animation_names) - 1)
    ask_choice = True
    while True:
        if ask_choice:
            behav_choice = raw_input("Choose a behavior index number between 0 and " + str(max_choice) + " : ")

            try:
                behav_choice = int(behav_choice)
                if behav_choice == 999:
                    print("Stop asking for choices, ESC to stop the Threads.")
                    ask_choice = False

                elif not 0 <= behav_choice <= max_choice:
                    print("Not in range")

                else:
                    print("You choose " + PepperOSC_Config.animation_names[behav_choice])
                    # sound start flag
                    PepperOSC_OSC.osc_send_sound_flag('/soundstart', 1)
                    # do the movement
                    PepperOSC_PepperProxies.pepper_run_behavior(behav_choice)
                    # sound stop flag
                    PepperOSC_OSC.osc_send_sound_flag('/soundstop', 1)
            except ValueError:
                print("Not a valid number")

        global stop_threads
        if stop_threads:
            print("Thread 1 OFF")
            break


# Thread 2
# Constantly streams OSC
def run_thread_send_osc():
    print ("Thread 2 ON - sending data to OSC")
    while True:
        prev_time = time.time()
        PepperOSC_PepperProxies.pepper_data_stream(prev_time)
        global stop_threads
        if stop_threads:
            print("Thread 2 OFF")
            break


if __name__ == "__main__":
    print("Initiating program ...")

    # global stuffs
    stop_threads = False

    # init Pepper's position
    PepperOSC_PepperProxies.pepper_pause_awareness()
    PepperOSC_PepperProxies.pepper_stand()
    print ("Please wait...")
    time.sleep(1)

    # init threads
    t2 = threading.Thread(target=run_thread_send_osc)
    t2.start()

    t1 = threading.Thread(target=run_thread_pepper_control)
    t1.start()

    time.sleep(1)

    while not (keyboard.is_pressed('ESCAPE')):
        # loop forever
        # until someone hit the ESC button
        stop_threads = False

    stop_threads = True
    print("Terminating program...")
    PepperOSC_PepperProxies.pepper_resume_awareness()
    time.sleep(2)
    print('ALL DONE !')
