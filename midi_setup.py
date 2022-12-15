import pygame
from pygame import midi
import numpy as np


class midi_setup:

    def __init__(self):
        pygame.init()
        midi.init()
        # pass

    def device(self):
        if midi.get_count() > 0:
            for i in range(midi.get_count()):
                print(f'device id: {i}, info: {midi.get_device_info(i)} \n') 
            print(f'choose midi device: 1 - {midi.get_count()}\n')
            device_num = input()

            midi_input = midi.Input(device_id=int(device_num))
            return midi_input
        else:
            print("zero midi devices detected")
            return None

    def midi_loop(self, midi_input):
        
        note = np.array(midi_input.read(num_events=16), dtype=object)
        print(note)
        note = note.flatten()
        note_on = note[0][0]
        note_val = note[0][1]
        vel = note[0][2]

        return note_on, note_val, vel


if __name__ == "__main__":

    midi_setup = midi_setup()
    midi_input = midi_setup.device()

    if midi_input == None:
        exit()
    try: 
        while True:
            if midi_input.poll():  
                note_on, note_val, vel = midi_setup.midi_loop(midi_input)
                print(note_on, note_val, vel)
    except KeyboardInterrupt as err:
        print("Stopping...")