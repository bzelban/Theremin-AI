import numpy as np
import time
import pyaudio

class Oscilator():

    def __init__(self):
        self.STREAM_LOOP = True
        self.curr_pitch = 440
        self.curr_amp = 0.0

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=8000,
            output=True
        )

    def __str__(self):
        return 'Oscilator Module Testing Function'

    def set_current(self, amp, pitch):
        self.curr_pitch = pitch
        self.curr_amp = amp

    def controller_latch(self):
        if self.STREAM_LOOP == True: self.STREAM_LOOP = False;
        else: self.STREAM_LOOP = True

    def sound_stream(self):

        while self.STREAM_LOOP:
            sample = (np.sin(2*np.pi * np.arrange(8000)*self.curr_pitch/8000)).astype(np.float32)
            stream.write(self.curr_amp * self.curr_pitch)
