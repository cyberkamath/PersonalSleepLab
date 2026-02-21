# Simple Audio Recorder, Needs to be modified later to handle Recording for Whole Sleep Session

import sounddevice as sd
import soundfile as sf
from datetime import datetime
from dataclasses import dataclass
from pathlib import Path


@dataclass
class RecorderConfig:
    sample_rate: int = 16000 # Standard rate for recording Human voice or Snoring
    duration: int = 10 # seconds
    channels: int = 1
    output_dir: Path = Path("recordings")
    assets_dir: Path = Path("assets")
    file_format: str = "wav"
    recording_started: str = "recording.mp3"
    recording_finished: str = "completed.mp3"

def generate_filename(config : RecorderConfig) -> Path :
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return config.output_dir / f"Sleep_sound_{timestamp}.{config.file_format}"

def play_audio(audio_path: Path):
    try:
        audio_data, fs = sf.read(audio_path)
        sd.play(audio_data,fs)
        sd.wait()
    except Exception as e:
        print(f"Could not play audio at {audio_path}: {e} ")


def record_audio(config: RecorderConfig):
    
    config.output_dir.mkdir(exist_ok=True)

    starting_time = datetime.now()
    print(f"Recording Started at {starting_time}")
    play_audio(config.assets_dir / config.recording_started)

    recorded_audio = sd.rec(
        int(config.duration * config.sample_rate),
        samplerate=config.sample_rate,
        channels=config.channels,
        dtype='float32'
    )
    sd.wait()

    output_file =  generate_filename(config)
    sf.write(output_file, recorded_audio, config.sample_rate)

    finish_time = datetime.now()
    print(f"Recording finished at {finish_time}")
    play_audio(config.assets_dir / config.recording_finished)

if __name__ == "__main__":
    config = RecorderConfig()
    record_audio(config)

