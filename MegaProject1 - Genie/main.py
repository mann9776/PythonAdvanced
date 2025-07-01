import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recogniser = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
if __name__ == "__main__":
    #speak("Hello, I am Genie, your personal assistant. How can I help you today?")
    speak("Initializing Genie...")

    while True:
        #Listen for the wake word "Genie"
        with sr.Microphone() as source:
            print("Listening for the wake word 'Genie'...")
            audio = recogniser.listen(source)

        try:
            command = recogniser.recognize_google(audio).lower()
            print(f"Command received: {command}")

            if "genie" in command:
                speak("How can I assist you?")
                # Here you can add more functionality based on the command
                # For example, opening a website or performing a task
                # Example: webbrowser.open("https://www.example.com")
                with sr.Microphone() as source:
                    print("Genie Active, Listening for your command...")
                    audio = recogniser.listen(source)
                    command = recogniser.recognize_google(audio).lower()
                    processCommand(command)


        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    
