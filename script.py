from pydub import AudioSegment

# Explicitly set ffmpeg and ffprobe paths
AudioSegment.converter = r"C:\ffmpeg\ffmpeg-2025-04-23-git-25b0a8e295-full_build\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\ffmpeg\ffmpeg-2025-04-23-git-25b0a8e295-full_build\bin\ffprobe.exe"

# Test audio conversion
try:
    audio = AudioSegment.from_file("test.mp3", format="mp3")
    audio.export("test.wav", format="wav")
    print("Audio conversion successful!")
except Exception as e:
    print(f"Error: {e}")