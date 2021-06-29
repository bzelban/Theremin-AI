import rtmidi


class Midi_Bridge_Module():

    def __init__(self):
        self.midiout = rtmidi.MidiOut()
        self.available_ports = self.midiout.get_ports()
        self.note_off = [0x80, 60, 0]

        if self.available_ports:
            self.midiout.open_port(1)
            print("No Avail MIDI Port, NEW CREATED")
        else:
            self.midiout.open_virtual_port('Virtual MIDI on Defined Port')


    def create_port(self):
        if self.available_ports:
            self.midiout.open_port(1)
            print("No Avail MIDI Port, NEW CREATED")
        else:
            self.midiout.open_virtual_port('Virtual MIDI on Defined Port')

    def send_midi(self, note, amplitude):

        self.midiout.send_message([0x80, note, amplitude])
        print('MIDI NOTE: ' + str(note) + 'MIDI VEL:' + str(amplitude))


    def send_silence(self, note, amplitude):
        self.midiout.send_message([0x90, note, amplitude])
        time.sleep(0.01)
        self.midiout.send_message([0x80, note, amplitude])

