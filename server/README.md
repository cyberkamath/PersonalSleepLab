# SleepLab Server

## Overview

The SleepLab Server runs on your NAS (Raspberry Pi cluster).

It is responsible for:

- Receiving recordings from Recorder Pis
- Storing raw sleep data
- Processing audio and video
- Generating sleep metrics
- Exposing APIs for dashboards and future OpenHuman integration

Recorder devices only capture and upload data.
All heavy processing happens here.