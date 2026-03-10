import numpy as np
import librosa
import librosa.display
import json
import matplotlib.pyplot as plt

# 1️⃣ Loading audio
file_path = "sample.mp3"
y, sr = librosa.load(file_path, sr=None, mono=True)

num_peaks = 500  # number of waveform points, 2000 seems to do a good job at showing very similar waveform.
total_samples = len(y)
block_size = total_samples // num_peaks

# 3️⃣ Generating Peaks
peaks = []
for i in range(num_peaks):
    start = i * block_size
    end = start + block_size
    segment = y[start:end]
    if len(segment) == 0:
        continue
    peaks.append([float(segment.min()), float(segment.max())])


with open("waveform_peaks.json", "w") as f:
    json.dump(peaks, f)

# Comparing Original waveform with the Simplified Peaks waveform

mins = [p[0] for p in peaks]
maxs = [p[1] for p in peaks]
x_peaks = np.arange(len(peaks))

plt.figure(figsize=(15, 6))

# original waveform
plt.subplot(2, 1, 1)
librosa.display.waveshow(y=y, sr=sr, color="green")
plt.title("Original Audio Waveform")
plt.xlabel("Time")
plt.ylabel("Amplitude")

# peak-extracted waveform
plt.subplot(2, 1, 2)
plt.fill_between(x_peaks, mins, maxs, color="red")
plt.title("Peak-extracted Waveform")
plt.xlabel("Peaks")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()