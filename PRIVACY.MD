# Privacy & Data Handling Guidelines

## Overview

Local Sleep Monitor is designed with privacy as a core principle.
All data is intended to be processed and stored **locally on the user’s device**.

The project does not collect, transmit, or share sleep data with external servers by default.

## Types of Data Collected

Depending on enabled features, the application may collect:
- Audio recordings (e.g., snoring, ambient noise)
- Video recordings during sleep sessions
- Derived data such as movement frequency, sleep position, and breathing patterns
- Metadata such as timestamps and session duration

## Local Storage

- All recordings and derived data are stored locally
- Users are responsible for securing their own devices
- No cloud uploads are performed unless explicitly added by the user

## User Consent

Users should be clearly informed when:
- Audio recording is active
- Video recording is active
- Computer vision analysis is enabled

Developers and contributors should ensure that recording features are **opt-in** and clearly documented.

## Data Retention

- Users should have the ability to delete recordings and analysis results
- Long-term storage policies should be configurable where possible

## Developer Responsibilities

Contributors are expected to:
- Avoid logging or exposing sensitive data unnecessarily
- Use secure file permissions when storing recordings
- Treat sleep, audio, and video data as highly sensitive information
- Follow the project’s Code of Conduct and Security Policy

## Disclaimer

This project is intended for educational and personal use.
It is **not a medical device** and does not provide medical diagnoses or treatment.
