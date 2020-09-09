import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
engine =pyttsx3.init()

def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  
def wish():
    time=int(datetime.datetime.now().hour) 
    if time>0 and time<12:
        speak("good morning")
    elif time>12 and time<18:
        speak("good afternoon")
    else:
        speak("good evening")
    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as mic:
        print("listening.....")
        r.pause_threshold =1
        r.listen(mic)
    try:
        print("rercognising....")
        recog=r.recognize_google(audio_data=mic,language="english-india")
        print(f"user said {recog}")
    except Exception as e:
        print("please say that again")
    
if __name__ == "__main__":
    wish()
    search=takecommand().lower()
    if "open" in search:
        webbrowser.open("takecommand.recog")
    elif"thank you jarvis"in search:
        exit()
    
    
