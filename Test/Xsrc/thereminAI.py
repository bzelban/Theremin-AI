
# Module NameSpaces
from modules.hand_detection import Hand_Detection_Module

from modules.estimation.depth_estimation import Hand_Depth_Estimation_Module
from modules.estimation.distance_estimation import Hand_Distance_Estimation_Module

from modules.oscillation.oscilator import Oscilator
from modules.oscillation.midi_sender import Midi_Bridge_Module

# Main Libraries
import threading
import queue as q


HAND_DETECTION_VISUAL_DEBUG = False


HDM = Hand_Detection_Module()

DEM = Hand_Distance_Estimation_Module()
DEP = Hand_Depth_Estimation_Module()

OSCM = Oscilator()

def check_diff(tempQ):
    hand_landmark = None

    while True:
        if hand_landmark != tempQ.get():
            current_parameters(tempQ.get())
            hand_landmark = tempQ.get()
            print(hand_landmark)
        #print(hand_landmark)
        # tempQ.task_done()


def current_parameters(chunk):
    if chunk != None:
        print(DEM.distance_estimation(chunk))
        print(DEP.depth_estimation(chunk))


def theremin():

    print('\t\t\tSTARTING THEREMIN.AI')

    # Q size ilerde sıkıntı yaşatır mı?
    main_q = q.Queue()

    detection_thread = threading.Thread(target=HDM.detection, args=(HAND_DETECTION_VISUAL_DEBUG, main_q))
    diff_thread = threading.Thread(target = check_diff, args = (main_q,))

    print('Threads Created - RUNNING')

    diff_thread.start()
    detection_thread.start()


if __name__ == "__main__":
    theremin()