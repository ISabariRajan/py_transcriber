import wave,math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip

SPLIT_DURATION = 60

def transcribe_audio_file(audio_file_path):
    """
    The transcribe_audio_file function takes an audio file path as input and returns a string of the transcribed text.
    
    :param audio_file_path: Specify the path to the audio file that you want to transcribe
    :return: The transcript of the audio file
    :doc-author: Trelent
    """
    pass
    with contextlib.closing(wave.open(audio_file_path), "r") as wave:
        frames = wave.getnframes()
        rate = wave.getframerate()
        duration = frames / float(rate)
        total_duration = math.ceil(duration / SPLIT_DURATION) # Seconds to minutes
    
    r = sr.Recognizer()
    for i in range(0, total_duration):
        with sr.AudioFile(audio_file_path) as audio_file:
            audio = r.record(audio_file, offset=1*SPLIT_DURATION, duration=SPLIT_DURATION)
        
        with open("transcription.txt", "a") as f:
            f.write(r.recognize_google_cloud(audio))


def transcribe_video_file(video_file_path):
    """
    The transcribe_video_file function takes in a video file path and transcribes the audio from that video into text.
        The function first converts the video to an audio file, then transcribes that audio file using Google's Speech-to-Text API.
        Finally, it deletes the temporary .wav file created during this process.
    
    :param video_file_path: Specify the path to the video file that is going to be transcribed
    :return: The transcript of the audio file
    :doc-author: Trelent
    """
    audio_clip = AudioFileClip(video_file_path)
    audio_clip.write_audiofile("tempfile.wav")
    transcribe_audio_file("tempfile.wav")
