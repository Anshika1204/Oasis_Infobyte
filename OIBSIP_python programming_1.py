import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def get_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold =1
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        speak("What should I search for?")
        query = get_voice_command()
        if query:
            url = f"https://www.google.com/search?q={query}"
            speak(f"Searching Google for {query}")
            webbrowser.open(url)
    elif command:
        speak("I don't understand that command yet.")

def main():
    speak("Voice assistant activated. Say something.")
    while True:
        command = get_voice_command()
        if "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye!")
            break
        handle_command(command)

if __name__ == "__main__":
    main()
