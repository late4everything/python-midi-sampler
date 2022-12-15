import pygame
from pygame import midi
import numpy as np
import midi_setup
import wave
import os
import pyaudio

class play_samples:

    def __init__(self):
        midi_setup.midi_setup()
        self.sample_dict = None

    def get_midi_device(self):
        midi_input = midi_setup.device()

        return midi_input

    def open_audio_stream(self, wave_object):
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
        
    def load_samples(self, filepath):
        samples_dict = {}
        sample_names = os.listdir(filepath)
        
        for name in sample_names:
            samples_dict[name] = wave.open(f'{filepath}{name}', 'r')

        self.sample_dict = samples_dict
        print(self.sample_dict)

    
    def open_wav(self, midi_note):
        if self.sample_dict.get(midi_note) == None:
            print("no note availale")
            return
        else:
            wave_note = self.sample_dict.get(midi_note)

        return wave_object

    def close_wav(self, wave_note):
        wave_note.close()
    def play_wav():
        pass
    def pitch_up(self):
        pass
    
    def midi_info(self, input_device):
        
        if midi_input == None:
            exit()
        if midi_input.poll():  
            note_on, note_val, vel = midi_setup.midi_loop(input_device)
        
        return note_on, note_val, vel
        
if __name__ == "__main__":

    play = play_samples()
    play.load_samples('samples/')
    # try: 
    #     while True:
            
    # except KeyboardInterrupt as err:
    #         print("Stopping...")