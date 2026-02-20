# Simple Audio Recorder, Needs to be modified later to handle Recording for Whole Sleep Session

import sounddevice as sd
import soundfile as sf

output_file =  "Sleep_sound.wav"
sample_rate = 44000 # Standard CD rate, may have to change to Human voice rate later if data is good enough
duration = 10 # seconds
channels = 1

#Initiate Recording
audio_data, fs = sf.read('assets/recording.mp3')
sd.play(audio_data,fs)
sd.wait()

#Record starts here
recorded_audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='float32')
sd.wait()

#Save the Recordings
sf.write(output_file, recorded_audio, sample_rate)

#Finish Recording
audio_data, fs = sf.read('assets/completed.mp3')
sd.play(audio_data,fs)
sd.wait()


