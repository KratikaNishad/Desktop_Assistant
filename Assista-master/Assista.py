# ASSISTA is the desktop assistant..

import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia
import datetime
import webbrowser
import time
import wolframalpha


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("please say that again")
            return "None"
        return statement
    
def wishMe():
    
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<15:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
    speak('SIR,ASSISTA! in your service..')
    

    
           
def date_meth():
    
    month_map = {1:"January",2:"February",3:"March", 4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    year = int(datetime.datetime.now().year)
    month =int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    print(date, month, year)
    speak("the currunt date is")
    speak(str(date))
    speak(month_map.get(month))
    speak(str(year))
    


        
    
if __name__=='__main__':
    
    wishMe()
    
    while True:
        speak("what can i do next for you sir.")
        statement = takeCommand().lower()
        if statement==0:
            continue
        
        elif 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'introduce yourself' in statement:
            speak('hello sir my name is Assista. i am a voice controlled device made by The Art of Coders')
            print('hello sir my name is Assista. i am a voice controlled device made by The Art of Coders')
            
        elif "ok bye assista" in statement or "ok bye" in statement or "stop" in statement or "thank you" in statement:
            speak('i am shutting down sir,bye bye')
            print('i am shutting down sir,bye bye')
            break
            
        elif 'youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            time.sleep(5)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
            
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by the art of coders")
            print("I was built by the art of coders")
            
        elif "team" in statement:
            speak("the name of the team who made me is the art of coders.")
            print("the name of the team who made me is the art of coders.")
        
        elif 'date' in statement:
            date_meth()
        
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id=" AGXEGQ-XRKJJ9QQ22 "
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            
                    

    
        
        


