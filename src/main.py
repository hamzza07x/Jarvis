from jarvis import *
import wikipedia
import webbrowser
import os
import random
# you have to use your own paths to selective apps in the code below

def calculateMonth(tocalculate):
    months = {
        "01": "January", "02": "February", "03": "March", "04": "April",
        "05": "May", "06": "June", "07": "July", "08": "August",
        "09": "September", "10": "October", "11": "November", "12": "December"
    }
    return months.get(tocalculate, "Invalid month")

def run_jarvis():
    wishMe()
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue
        elif 'wikipedia' in query:
             speak('Searching Wikipedia...')
             query = query.replace("wikipedia", "")
             try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
             except wikipedia.exceptions.DisambiguationError as e:
                speak("I found multiple results. Here's the first one.")
                results = wikipedia.summary(e.options[0], sentences=2)
                speak(results)
             except wikipedia.exceptions.PageError:
                speak("No page found. Let me search that on Google instead.")
                webbrowser.open(f"https://www.google.com/search?q={query}")

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            speak("Opening Stack Overflow")
            webbrowser.open("stackoverflow.com")
        elif "open github" in query:
            speak("Opening GitHub")
            webbrowser.open("github.com")
        elif "open linkedin" in query:
            speak("Opening LinkedIn")
            webbrowser.open("linkedin.com")
        elif "open facebook" in query:
            speak("Opening Facebook")
            webbrowser.open("facebook.com")
        elif "open twitter" in query:
            speak("Opening Twitter")
            webbrowser.open("twitter.com")
        elif "open instagram" in query:
            speak("Opening Instagram")
            webbrowser.open("instagram.com")
        elif "open whatsapp" in query:
            speak("Opening WhatsApp")
            webbrowser.open("web.whatsapp.com")
        elif "open gmail" in query:
            speak("Opening Gmail")
            webbrowser.open("gmail.com")
        elif "open reddit" in query:
            speak("Opening Reddit")
            webbrowser.open("reddit.com")
        elif "open spotify" in query:
            speak("Opening Spotify")
            webbrowser.open("spotify.com")
        elif "open netflix" in query:
            speak("Opening Netflix")
            webbrowser.open("netflix.com")
        elif "open amazon" in query:
            speak("Opening Amazon")
            webbrowser.open("amazon.com")
        elif "play music " in query:
            speak("Playing music...")
            musicDir = r"C:\Users\Muhammad Hamza\Documents\Rockstar Games\GTA IV\User Music"
            songs = os.listdir(musicDir)
            print(songs)
            os.startfile(os.path.join(musicDir, random.choice(songs)))
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif "date" in query:
            strDate = datetime.datetime.now().strftime("%d/%m/%Y")
            speak(f"The date is {strDate}")
        elif "who are you" in query:
            speak("I am your virtual assistant, here to help you with any task or information you need")
        elif "what can you do" in query:
            speak("I can do a variety of tasks, including but not limited to:")
            speak("Playing music, opening websites, telling the time and date, and more!")
        elif "open notepad" in query:
            speak("Opening Notepad")
            notePadPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
            os.startfile(notePadPath)
        elif "open code" in query:
            speak("Opening Code")
            codePath = r"C:\Users\Muhammad Hamza\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
            os.startfile(codePath)
        elif "open visual studio" in query:
            speak("Opening Visual Studio")
            VSPath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
            os.startfile(VSPath)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "hamzza07x@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully")
            except Exception as e:
                speak("Sorry, I am not able to send this email")
        elif "shutdown" in query or "shut down" in query or "quit" in query or "exit" in query:
            speak("Are you sure you want to shut down?")
            confirmation = takeCommand().lower()
            if "yes" in confirmation or "sure" in confirmation:
                speak("Shutting down...")
                break
            else:
                speak("Shutdown cancelled.")
        elif "restart" in query:
            speak("Are you sure you want to restart?")
            confirmation = takeCommand().lower()
            if "yes" in confirmation or "sure" in confirmation:
                speak("Restarting...")
                os.system("shutdown /r /t 1")
        elif "sleep" in query:
            speak("Are you sure you want to sleep?")
            confirmation = takeCommand().lower()
            if "yes" in confirmation or "sure" in confirmation:
                speak("Sleeping...")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif "how are you" in query:
            speak("I am doing well, thank you for asking!")
        elif "joke" in query:
            speak("Here's one: Why couldn't the bicycle stand up by itself? Because it was two-tired! Ha ha ha!")
        elif "weather" in query:
            speak("Checking the weather...")
            webbrowser.open("https://www.weather.com/")
        elif "news" in query:
            speak("Checking the news...")
            webbrowser.open("https://www.bbc.com/news")
        elif "search" in query or "find" in query:
            speak("What do you want to search for?")
            search = takeCommand().lower()
            webbrowser.open("https://www.google.com/search?q=" + search)
            speak("Here are the results")
        elif "shutdown computer" in query or "turn off computer" in query:
            speak("Are you sure you want to shut down?")
            confirmation = takeCommand().lower()
            if "yes" in confirmation or "sure" in confirmation:
                speak("Shutting down...")
                os.system("shutdown /s /t 1")
            else:
                speak("Shutdown cancelled.")
        elif "when was i born" in query:
            myBirthDate = "20/06/2004"
            month = calculateMonth(myBirthDate.split("/")[1])
            speak(f"You were born on {myBirthDate.split('/')[0]} {month} {myBirthDate.split('/')[2]}.")
        elif "who is your creator" in query:
            speak("My creator is a brilliant individual who has given me life and purpose. I am grateful for their hard work and dedication in creating me.")
        elif "how old are you" in query:
            speak("I was created on May 29 , 2025")
            age = datetime.datetime.now().year - 2025
            speak("I am " + str(age) + " years old.")
        elif "how old am i" in query:
            myBirthDate = "20/06/2004"
            birthYear = int(myBirthDate.split("/")[2])
            currentYear = datetime.datetime.now().year
            age = currentYear - birthYear
            speak(f"you were born on {myBirthDate.split('/')[0]} {calculateMonth(myBirthDate.split('/')[1])} {birthYear}.")
            speak("so,You are " + str(age) + " years old.")
        else:
            print(query)
            print("I didn't understand that command.")
            speak("Sorry, I didn't understand that. Please try again!")

if __name__ == "__main__":
    run_jarvis()
