
#!/usr/bin/env python3
# mp4_to_text.py

"""
Author: Drew Mayberry
Date: June 28, 2024
Description: This script converts MP4 audio files to WAV format and transcribes the audio using the Google Cloud Speech-to-Text API. It splits the audio into 30-second chunks for transcription.
Version: 1.0
"""


import os
import io
from pydub import AudioSegment
from pydub.utils import make_chunks
from google.cloud import speech
from tqdm import tqdm

def convert_mp4_to_wav(mp4_path):
    """
    Convert MP4 file to WAV format.

    Args:
    mp4_path (str): The path to the MP4 file.

    Returns:
    str: The path to the converted WAV file.
    """
    print("Converting MP4 to WAV...")
    audio = AudioSegment.from_file(mp4_path, format="mp4")
    wav_filename = os.path.basename(mp4_path).replace('.mp4', '.wav')
    wav_path = os.path.join(os.getcwd(), wav_filename)
    audio.export(wav_path, format="wav")
    print(f"WAV file saved as {wav_path}")
    return wav_path

def get_sample_rate(wav_path):
    """
    Get the sample rate of a WAV file.

    Args:
    wav_path (str): The path to the WAV file.

    Returns:
    int: The sample rate of the WAV file.
    """
    audio = AudioSegment.from_wav(wav_path)
    return audio.frame_rate

def transcribe_audio_chunk(chunk, client, sample_rate):
    """
    Transcribe a chunk of audio using Google Cloud Speech-to-Text API.

    Args:
    chunk (AudioSegment): The audio chunk to transcribe.
    client (speech.SpeechClient): The Google Cloud Speech client.
    sample_rate (int): The sample rate of the audio chunk.

    Returns:
    speech.RecognizeResponse: The transcription response from the API.
    """
    with io.BytesIO() as audio_file:
        chunk.export(audio_file, format="wav")
        content = audio_file.getvalue()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    return response

def transcribe_audio(wav_path):
    """
    Split audio into chunks and transcribe each chunk.

    Args:
    wav_path (str): The path to the WAV file.

    Returns:
    None
    """
    client = speech.SpeechClient()

    print("Splitting audio into chunks...")
    audio = AudioSegment.from_wav(wav_path).set_channels(1)  # Convert to mono
    chunk_length_ms = 30000  # 30 seconds chunks
    chunks = make_chunks(audio, chunk_length_ms)

    transcript_path = wav_path.replace('.wav', '.txt')
    sample_rate = get_sample_rate(wav_path)

    with open(transcript_path, 'w') as transcript_file:
        print("Transcribing audio chunks...")
        for i, chunk in tqdm(enumerate(chunks), total=len(chunks), desc="Transcribing", ncols=100):
            try:
                response = transcribe_audio_chunk(chunk, client, sample_rate)
                for result in response.results:
                    transcript = result.alternatives[0].transcript
                    transcript_file.write(f"Chunk {i} Transcript: {transcript}\n")
                    print(f"Chunk {i} Transcript: {transcript}")
            except Exception as e:
                print(f"Error transcribing chunk {i}: {e}")

    print(f"Transcription saved to {transcript_path}")

def main():
    """
    Main function to execute the script.

    Args:
    None

    Returns:
    None
    """
    mp4_path = input("Enter the path to the MP4 file: ")

    if not os.path.exists(mp4_path):
        print(f"File {mp4_path} does not exist.")
        return

    try:
        wav_path = convert_mp4_to_wav(mp4_path)
        
        print("Processing audio transcription...")
        transcribe_audio(wav_path)

        print("Process completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
