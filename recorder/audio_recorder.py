import sounddevice as sd
from datetime import datetime
from queue import Queue
from threading import Thread
from config import AudioRecorderConfig
from utils import play_audio
from audio_writer import writer_thread


def _prepare_recording(audio_config : AudioRecorderConfig):
    
    audio_config.output_dir.mkdir(exist_ok=True)
    starting_time = datetime.now()
    print(f"Recording Started at {starting_time}")
    play_audio(audio_config.assets_dir / audio_config.recording_started)


def _start_writer_thread(audio_config: AudioRecorderConfig, audio_queue: Queue):
    writer = Thread(target=writer_thread, args=(audio_config, audio_queue))
    writer.start()
    return writer


def _record_chunks(audio_config: AudioRecorderConfig , audio_queue: Queue):

    total_chunks = int( audio_config.duration / audio_config.chunk_duration )

    for i in range(total_chunks):
        print(f"Recording Chunk number {i}")
        recorded_audio = sd.rec(
            int(audio_config.chunk_duration * audio_config.sample_rate),
            samplerate=audio_config.sample_rate,
            channels=audio_config.channels,
            dtype='float32'
        )
        sd.wait()
        audio_queue.put(recorded_audio)


def record_audio(audio_config: AudioRecorderConfig, audio_queue : Queue):
    
    _prepare_recording(audio_config)

    writer = _start_writer_thread(audio_config, audio_queue)

    _record_chunks(audio_config,audio_queue)

    audio_queue.put(None)
    audio_queue.join()
    writer.join()
