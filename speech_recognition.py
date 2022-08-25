from huggingsound import SpeechRecognitionModel

model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english")

def recognize(audio_paths):
    transcriptions = model.transcribe(audio_paths)
    
    return { 'transcript': transcriptions }