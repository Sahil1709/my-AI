import pyttsx3
import speech_recognition as sr

def record(sec=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Start speaking")
        recorded_audio = recognizer.listen(source, timeout=sec)
        print("Done recording")
    try:
        text = recognizer.recognize_google(
            recorded_audio, 
            language="en-US"
        )
        print("Decoded Text : {}".format(text))
        text = text.lower()
        return text
    except Exception as e:
        print(e)

def speak(text="NA"):
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()

speak("Enter seconds for recording")

secs = int(input("Enter seconds for recording :"))
text = record(secs)

possibleValues = ["hi" in text ,
"hello" in text,
"what is up" in text,
"what's up" in text,
"sup" in text,
"hey there" in text
]
if any(possibleValues) :
    speak("Hello , may i know your name ?")
    ans = record(secs)
    if "yes" in ans:
        speak("Tell me ")
        name = record(secs)
        speak(f" hello {name} , nice to meet you")
    else:
        speak("sorry to hear that")
elif "capital" in text:
    speak("which state capital u wanna know ")
    country = record(secs)
    if "india" in country:
        speak("capital of India is Delhi .")
    elif "united states" or "us" or "united state" in country:
        speak("Capital of united states is Washington, D.C")
    else:
        speak("Cannot understand a word u say .")
else:
    speak("I didnt recognised what u say !")
