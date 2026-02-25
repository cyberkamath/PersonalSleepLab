import sounddevice as sd
import soundfile as sf
from pathlib import Path
from config import AudioRecorderConfig
from datetime import datetime


def generate_audio_filename(audio_config : AudioRecorderConfig) -> Path :
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return audio_config.output_dir / f"Sleep_sound_{timestamp}.{audio_config.file_format}"


def play_audio(audio_path: Path):
    try:
        audio_data, fs = sf.read(audio_path)
        sd.play(audio_data,fs)
        sd.wait()
    except Exception as e:
        print(f"Could not play audio at {audio_path}: {e} ")