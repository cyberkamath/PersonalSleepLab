# Simple Audio Recorder, Needs to be modified later to handle Recording for Whole Sleep Session

from queue import Queue
from config import AudioRecorderConfig
from audio_recorder import record_audio

audio_queue = Queue(maxsize=3)

if __name__ == "__main__":
    audio_config = AudioRecorderConfig()
    record_audio(audio_config, audio_queue)

