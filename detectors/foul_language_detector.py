import whisper
from transformers import pipeline

def transcribe_audio(audio_file):
    model = whisper.load_model("large")
    result = model.transcribe(audio_file, language="en")
    return result["text"]

def detect_foul_language(text):
    print("🧠 Using BERT toxic classifier...")
    classifier = pipeline("text-classification", model="unitary/toxic-bert")
    results = classifier(text)
    foul_classes = ["toxic", "obscene", "insult", "threat"]
    for result in results:
        print(result)
        if result['label'].lower() in foul_classes and result['score'] > 0.1:
            return True
    return False
