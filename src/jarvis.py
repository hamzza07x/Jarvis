import pyttsx3
import datetime
import speech_recognition as sr
import smtplib

User = "PRO NOOB"
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

# engine.setProperty("voice",voices[0].id) #David's voice
engine.setProperty("voice",voices[1].id) # Zira's voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour < 24:
        speak("Good evening")
    else:
        speak("Good night")
    speak(f"Welcome {User}")
    speak("I am Jarvis, your personal assistant. How can i help you?")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  
        audio = r.listen(source, timeout=10, phrase_time_limit=8)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-en')
        print(f"User said: {query}\n")
    except sr.WaitTimeoutError:
        print("Timeout occurred. Try speaking louder or closer to mic.")
        return "None"
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return "None"
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return "None"

    return query

def sendEmail(to, content):

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("your-email@gmail.com", "your-password") 
    server.sendmail("your-email@gmail.com", to, content)
    server.close()