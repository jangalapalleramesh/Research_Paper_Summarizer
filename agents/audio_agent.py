from gtts import gTTS

def generate_audio(text, filename="summary.mp3"):
    tts = gTTS(text)
    path = f"outputs/audios/{filename}"
    tts.save(path)
    return path
