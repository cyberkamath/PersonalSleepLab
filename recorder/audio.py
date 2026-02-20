# Simple Audio Recorder, Needs to be modified later to handle Recording for Whole Sleep Session

import sounddevice as sd
import soundfile as sf
import datetime as dt

sample_rate = 16000 # Standard rate for recording Human voice or Snoring
duration = 10 # seconds
channels = 1

#Initiate Recording
audio_data, fs = sf.read('assets/recording.mp3')
sd.play(audio_data,fs)
sd.wait()

starting_time = str(dt.datetime.now())
print("Recording Started at ",starting_time)

# Unique name for Each days Recording
output_file =  "Sleep_sound_" + starting_time[0:10] + ".mp3"


#Record starts here
recorded_audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='float32')
sd.wait()

#Save the Recordings
sf.write(output_file, recorded_audio, sample_rate,bitrate_mode='CONSTANT',compression_level=0.99)

#Finish Recording
audio_data, fs = sf.read('assets/completed.mp3')
sd.play(audio_data,fs)
sd.wait()

finishing_time = str(dt.datetime.now())
print("Recording finished at ",finishing_time)

