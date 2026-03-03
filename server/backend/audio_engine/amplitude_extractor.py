# Testing Librosa to to Audio Analysis

import librosa
from matplotlib import pyplot as plt


# Load the Audio file
waveform, samplerate = librosa.load("sample.wav",sr=None , mono= True)

plt.figure(figsize=(10,4))

librosa.display.waveshow(y = waveform,sr=samplerate)

plt.title("Audio Waveform")
plt.xlabel("Amplitute")
plt.ylabel("Time")

plt.tight_layout

plt.show()

