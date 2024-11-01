import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I could not understand the you.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None


import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        command = recognize_speech()
        if command:
            command = command.lower()
            if "hello" in command:
                speak("Hello! How can I assist you?")
            elif "stop" in command:
                speak("Goodbye!")
                break
            # Add more commands as needed

if __name__ == "__main__":
    main()
