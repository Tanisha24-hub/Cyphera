from moviepy.editor import VideoFileClip
import os

def extract_audio(video_path, audio_output):
    os.makedirs(os.path.dirname(audio_output), exist_ok=True)
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_output, logger=None)
    return audio_output
