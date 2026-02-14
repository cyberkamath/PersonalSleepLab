# SleepLab Recorder

## Overview

The SleepLab Recorder runs on a dedicated Raspberry Pi connected to a NOIR camera and optional microphone.

Its responsibility is to:

- Capture audio and video during sleep sessions
- Buffer recordings locally
- Upload recordings securely to the SleepLab Server (NAS cluster)
- Handle retries if the server is temporarily unavailable

⚠️ This component does NOT perform heavy processing.
All processing happens on the server.

---

## Hardware Requirements

- Raspberry Pi 4 (recommended) or Pi Zero 2W
- Raspberry Pi NOIR Camera
- Microphone (USB or I2S)
- Ethernet connection to local LAN

---

## Software Requirements

- Raspberry Pi OS (64-bit recommended)
- Python 3.10+
- FFmpeg
- Required Python dependencies (see requirements.txt)

---