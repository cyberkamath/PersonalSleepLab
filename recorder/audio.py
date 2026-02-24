# Simple Audio Recorder, Needs to be modified later to handle Recording for Whole Sleep Session

import sounddevice as sd
import soundfile as sf
from datetime import datetime
from dataclasses import dataclass
from pathlib import Path
from queue import Queue
from threading import Thread
import math


queue = Queue(maxsize=3)


@dataclass
class RecorderConfig:
    sample_rate: int = 16000 # Standard rate for recording Human voice or Snoring
    duration: int = 3600 # seconds
    channels: int = 1
    output_dir: Path = Path("recordings")
    assets_dir: Path = Path("assets")
    file_format: str = "flac"
    recording_started: str = "recording.mp3"
    recording_finished: str = "completed.mp3"
    chunk_duration: int = 300 #5 minutes chunk
    file_rotation_minutes: int = 15 


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


def writer_thread(config: RecorderConfig) :
    chunks_per_file = math.ceil(
        (config.file_rotation_minutes * 60) / config.chunk_duration
    )
    file_chunk_count = 0

    output_file =  generate_filename(config)
    f = sf.SoundFile(
        output_file,
        mode='w',
        samplerate=config.sample_rate,
        channels=config.channels,
        format=config.file_format
    )
        
    while True:
        chunk = queue.get()

        if chunk is None:
            queue.task_done()
            break

        f.write(chunk)
        file_chunk_count += 1
        queue.task_done()

        if file_chunk_count >= chunks_per_file:
            f.close()
            output_file = generate_filename(config)
            f = sf.SoundFile(
                output_file,
                mode='w',
                samplerate=config.sample_rate,
                channels=config.channels,
                format=config.file_format
                )
            file_chunk_count = 0
    f.close()
    finish_time = datetime.now()
    print(f"Recording finished at {finish_time}")
    play_audio(config.assets_dir / config.recording_finished)


def record_audio(config: RecorderConfig):
    
    config.output_dir.mkdir(exist_ok=True)

    starting_time = datetime.now()
    print(f"Recording Started at {starting_time}")
    play_audio(config.assets_dir / config.recording_started)
    total_chunks = int( config.duration / config.chunk_duration )

    writer = Thread(target=writer_thread, args=(config,))
    writer.start()

    for i in range(total_chunks):
        print(f"Recording Chunk number {i}")
        recorded_audio = sd.rec(
            int(config.chunk_duration * config.sample_rate),
            samplerate=config.sample_rate,
            channels=config.channels,
            dtype='float32'
        )
        sd.wait()
        queue.put(recorded_audio)

    queue.put(None)
    queue.join()
    writer.join()


if __name__ == "__main__":
    config = RecorderConfig()
    record_audio(config)

