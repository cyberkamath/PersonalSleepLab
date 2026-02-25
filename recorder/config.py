from dataclasses import dataclass
from pathlib import Path

@dataclass
class AudioRecorderConfig:
    sample_rate: int = 16000 # Standard Sample rate for recording Human voice or Snoring
    duration: int = 36 # seconds
    channels: int = 1 # Refers to Mono or Stereo
    output_dir: Path = Path("recordings")
    assets_dir: Path = Path("assets")
    file_format: str = "flac" # This is Compressed and Lossless format
    recording_started: str = "recording.mp3"
    recording_finished: str = "completed.mp3"
    chunk_duration: int = 3 #5 minutes chunk
    file_rotation_minutes: float = 0.15 # Creates new file every x minutes

## Upcoming Video Config, Network Config etc..