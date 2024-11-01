import os
import speech_recognition as sr
import pyttsx3


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
            print("Sorry, I could not understand.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def open_file(file_path):
    try:
        os.startfile(file_path)  # For Windows
        # For Mac, use: os.system(f'open "{file_path}"')
        # For Linux, use: os.system(f'xdg-open "{file_path}"')
    except Exception as e:
        print(f"Failed to open {file_path}: {e}")


def main():
    while True:
        command = recognize_speech()
        if command:
            command = command.lower()
            if "hello" in command:
                speak("Hello! How can I assist you?")
            elif "open" in command:
                file_name = command.split("open")[-1].strip()
                # Here, you can map file_name to actual paths
                file_path = f"C:\\path\\to\\your\\{file_name}.txt"  # Adjust the path as needed
                open_file(file_path)
            elif "stop" in command:
                speak("Goodbye!")
                break


if __name__ == "__main__":
    main()
