
# MP4 to Text Converter

This Python program converts an MP4 video file to WAV audio format and then transcribes the audio to a text file using Google Cloud's Speech-to-Text API.

## Table of Contents
- [Installation](#installation)
- [Google Cloud Setup](#google-cloud-setup)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Installation

### Step 1: Install Python and pip

Ensure you have Python 3.6+ installed on your system. You can download Python from [python.org](https://www.python.org/).

To check if Python is installed, run:
```sh
python3 --version
```

`pip` is the package installer for Python. It should come with Python, but you can install it manually if needed.

To install `pip`, run:
```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

### Step 2: Install Dependencies

Install the required Python packages using `pip`:

```sh
pip install pydub google-cloud-speech tqdm
```

### Step 3: Install FFmpeg

`pydub` requires FFmpeg for audio processing. Install it using the appropriate command for your operating system:

- **Ubuntu/Debian**:
  ```sh
  sudo apt-get install ffmpeg
  ```

- **macOS** (using Homebrew):
  ```sh
  brew install ffmpeg
  ```

- **Windows**:
  Download the FFmpeg executable from [ffmpeg.org](https://ffmpeg.org/download.html) and add it to your system PATH.

## Google Cloud Setup

### Step 1: Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.

### Step 2: Enable the Speech-to-Text API

1. In the Cloud Console, go to the [API & Services Dashboard](https://console.cloud.google.com/apis/dashboard).
2. Click "Enable APIs and Services".
3. Search for "Speech-to-Text API" and enable it.

### Step 3: Set Up Authentication

1. In the Cloud Console, go to the [Credentials page](https://console.cloud.google.com/apis/credentials).
2. Click "Create credentials" and select "Service account".
3. Follow the prompts to create a service account and download the JSON key file.

### Step 4: Set the `GOOGLE_APPLICATION_CREDENTIALS` Environment Variable

Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to your JSON key file. Replace `/path/to/your/service-account-file.json` with the actual path to your JSON key file.

- **Linux/macOS**:
  ```sh
  export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
  ```

- **Windows**:
  ```sh
  set GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\service-account-file.json"
  ```

## Usage

1. Clone this repository or save the script to a file named `mp4_to_text.py`.

2. Run the script:
   ```sh
   python3 mp4_to_text.py
   ```

3. Enter the path to your MP4 file when prompted:
   ```
   Enter the path to the MP4 file: /path/to/your/file.mp4
   ```

The script will convert the MP4 file to WAV format, split it into chunks, transcribe each chunk, and save the transcription to a text file in the same directory.

## Dependencies

- `pydub`: A high-level audio library.
- `google-cloud-speech`: Google Cloud client library for Speech-to-Text API.
- `tqdm`: A library for progress bars.
- `FFmpeg`: A multimedia framework for handling audio, video, and other multimedia files.

## Troubleshooting

### Common Issues

- **Payload Size Limit**: Ensure the audio chunks are under 10 MB.
- **Sample Rate Mismatch**: Ensure the sample rate in the `RecognitionConfig` matches the WAV file.
- **Stereo to Mono Conversion**: Ensure the audio is converted to mono before transcription.

### Debugging

Check the error messages printed by the script for guidance. Ensure that all dependencies are installed and correctly configured.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
