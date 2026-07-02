# 🎧 Audio Transcriber with OpenAI Whisper & Tkinter

A lightweight, user-friendly Python desktop script that transcribes audio files into text using OpenAI's powerful **Whisper** model. It features a native system file dialog interface, allowing you to manually select your input audio and choose exactly where to save the resulting `.txt` file.

---

## Features

*  **Manual File Selection:** Open a native OS window to pick your audio files easily.
*  **Custom Output Path:** Choose exactly where to save your transcription and customize the filename before processing.
*  **Multilingual Support:** Powered by OpenAI Whisper, capable of transcribing multiple languages with high accuracy.
*  **Fully Local:** Everything runs locally on your machine—no API keys required, ensuring complete privacy.

---

## Prerequisites

Before running the project, make sure you have the following installed:

1.  **Python 3.8+**
2.  **FFmpeg** (Required by Whisper to process audio)
    *   *Windows (via Winget):* `winget install Gyan.FFmpeg`
    *   *Mac (via Homebrew):* `brew install ffmpeg`
    *   *Linux (Ubuntu/Debian):* `sudo apt install ffmpeg`

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
   cd your-repository-name
