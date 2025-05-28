import whisper
import pyttsx3

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]

def synthesize_audio(text, output_path="output.wav"):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()