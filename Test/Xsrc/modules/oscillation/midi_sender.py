import rtmidi


class Midi_Bridge_Module():

    def __init__(self):
        self.midiout = rtmidi.MidiOut()
        self.available_ports = self.midiout.get_ports()
        self.note_off = [0x80, 60, 0]

        if self.available_ports:
            self.midiout.open_port(1)
        else:
            self.midiout.open_virtual_port('Virtual Midi Port Created')

    def send_midi(self, note, amplitude):
        with self.midiout:
            midiout.send_message([0x90, note, amplitude])

    def send_silence(self):
        with self.midiout:
            self.midiout.send_message(note_off)

