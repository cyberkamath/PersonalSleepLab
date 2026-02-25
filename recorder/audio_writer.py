import soundfile as sf
import math
from datetime import datetime
from queue import Queue
from config import AudioRecorderConfig
from utils import generate_audio_filename, play_audio

def _open_new_file(audio_config: AudioRecorderConfig):
    output_file = generate_audio_filename(audio_config)
    return sf.SoundFile(
        output_file,
        mode='w',
        samplerate=audio_config.sample_rate,
        channels=audio_config.channels,
        format=audio_config.file_format
        )

def _chunks_per_file(audio_config: AudioRecorderConfig):
    return math.ceil(
            (audio_config.file_rotation_minutes * 60) / audio_config.chunk_duration
        )

def _should_rotate(file_chunk_count: int ,chunks_per_file: int):
    return file_chunk_count >= chunks_per_file


def writer_thread(audio_config: AudioRecorderConfig, audio_queue: Queue) :
    
    chunks_per_file = _chunks_per_file(audio_config)
    file_chunk_count = 0
    f = None

    while True:
        chunk = audio_queue.get()

        if chunk is None:
            audio_queue.task_done()
            break
        
        if f is None:
            f = _open_new_file(audio_config)

        f.write(chunk)
        file_chunk_count += 1
        audio_queue.task_done()

        if _should_rotate(file_chunk_count , chunks_per_file):
            f.close()
            f = None
            file_chunk_count = 0

    if f is not None:
        f.close()
    finish_time = datetime.now()
    print(f"Recording finished at {finish_time}")
    play_audio(audio_config.assets_dir / audio_config.recording_finished)