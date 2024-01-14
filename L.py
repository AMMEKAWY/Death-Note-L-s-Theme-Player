import numpy as np
import sounddevice as sd
import time

# Music parameters
tempo = 135
timestamp = [4, 2, 1, 1/2, 1/4]  # seconds
timestamp = np.array(timestamp)
duration = timestamp * 60 / tempo

sample_rate = 44100
# Notes in one octave (C [0], C#/Db[1], D[2], D#/Eb[3], E[4], F[5], F#/Gb[6], G[7], G#/Ab[8], A[9], A#/Bb[10], B[11])
sheet = [7, 4, 9, 4, 6, 7, 4, 11, 9, 7, 6, 4, 2, 7, 4]
tim = [2] * np.size(sheet)
sheet = np.array(sheet)
tim = np.array(tim)

n = 4    # Octave number

def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t) * np.exp(-t)
    return sine_wave

# String parameters for C1
string_length = 1/2  # Length of the string in meters
tension = (32.7)**2  # Tension in Newtons
linear_density = 1  # Linear density in kg/m

# Calculate the resonance frequency using the string formula
resonance_frequency = (1 / (2 * string_length)) * np.sqrt(tension / linear_density)

cd=0
n2=3
note_frequencies = 2**(n2-1) * resonance_frequency * 2**(sheet/12)

# Generate and play the sine waves

def righthand():
    tau = 0
    while tau < np.size(tim):
        note_frequencies = 2**(n-1) * resonance_frequency * 2**(sheet/12)
        sine_wave = generate_sine_wave(note_frequencies[tau], duration[tim[tau]], sample_rate)
        sd.play(sine_wave, samplerate=sample_rate, blocking=False, blocksize=int(sample_rate/10))
        sd.wait()
        if (tau == np.size(tim)-1):
        
            time.sleep(0.5)
            tau=0
    
        else:
            tau += 1

righthand()

