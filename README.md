# Gesture-Based Game Control

Control games with hand gestures using MediaPipe (hand tracking), OpenCV, and pyautogui.

# Project Structure

Image_Processing_Project
├── README.md
├── requirements.txt
├── logo.svg
└── src/
    ├── _init_.py
    ├── main.py
    └── detector.py

## Features
- Raise hand (open palm) → Jump (press Space)
- Closed fist → Duck (hold Down)
- Pointing (index finger extended, others folded) → Flap/Shoot (press Space)
- Debounce and cooldown logic to avoid accidental repeated presses

## Prerequisites
- Python 3.8+
- Webcam
- Install system deps if needed (e.g., v4l-utils on Linux)

## Install
1. Clone or copy this repo:
```bash
git clone <repo-url> gesture-based-game-control
cd gesture-based-game-control