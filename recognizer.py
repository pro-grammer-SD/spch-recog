import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

print("Say something...")

while True:
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic)
        audio = recognizer.listen(mic)
        print("Got audio, recognizing...")

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        engine.say(f"You said: {text}")
        engine.runAndWait()
    except Exception as e:
        print("Error:", e)
        