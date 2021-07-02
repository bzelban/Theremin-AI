
# Module NameSpaces
from modules.hand_detection import Hand_Detection_Module

from modules.estimation.depth_estimation import Hand_Depth_Estimation_Module
from modules.estimation.distance_estimation import Hand_Distance_Estimation_Module

from modules.oscillation.oscilator import Oscilator
from modules.oscillation.midi_sender import Midi_Bridge_Module

# Main Libraries
import threading
import queue as q


# Module Construction
HDM = Hand_Detection_Module() #

DEM = Hand_Distance_Estimation_Module()
DEP = Hand_Depth_Estimation_Module()

OSCM = Oscilator()
# MBM = Midi_Bridge_Module()


# MIDI Libraries
import rtmidi
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()


def current_parameters(dist_chunk, dept_chunk):

    while True:
        PITCHVALUE = DEM.distance_estimation(dist_chunk.get())
        AMPLITUDEVALUE = DEP.depth_estimation(dept_chunk.get())

        print(str(PITCHVALUE) + "   " + str(AMPLITUDEVALUE))

        if AMPLITUDEVALUE:
            # print("Printing PITCH VALUE: " + str(PITCHVALUE))
            # print("Printing AMPLITUDE VALUE: " + str(AMPLITUDEVALUE))

            if AMPLITUDEVALUE != 0:
                # MBM.send_midi(PITCHVALUE, AMPLITUDEVALUE)
                midiout.send_message([0x90, PITCHVALUE, AMPLITUDEVALUE])

            else:
                # MBM.send_silence()
                pass


# Here is where Theremin.AI born
def theremin():
    print('\t\t\tSTARTING THEREMIN.AI\n')

    if available_ports:
        midiout.open_port(1)
        print("\n\t\t\t\tNo Avail MIDI Port, NEW CREATED")
    else:
        midiout.open_virtual_port('\n\t\t\t\tVirtual MIDI on Defined Port')

    distance_q = q.Queue()
    depth_q = q.Queue()

    detection_thread = threading.Thread(target=HDM.detection, args=(distance_q, depth_q))
    parameter_thread = threading.Thread(target=current_parameters, args=(distance_q, depth_q))

    print('\t\t\t\tThreads Created - RUNNING')

    detection_thread.start()
    parameter_thread.start()

if __name__ == "__main__":
    theremin()
