import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import re
# import snowboydecoder
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("Vector welcome you back.")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source, timeout=3)
        r.adjust_for_ambient_noise(source, duration=1)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in').lower()
        print(f"You said: {query}\n")
        return query
    
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        return 'none'
    except IndexError:
        print("No Internet Connection")
        speak("No Internet connection")
        return 'none'
    except KeyError:                                    # the API key didn't work
        print("Invalid API key or quota maxed out")
        return 'none'
    except LookupError:                                 # speech is unintelligible
        print("Could not understand audio")
        speak("could not understand")
        return 'none'
    except:
        print("no audio received")
        speak("come near to me and speak clearly please")
        return 'none'
    
    # except Exception as e:
    #     # print(e)    To print the Error.
    #     print("Please say that again...")
    #     return "None"
    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_emailid', 'your_password')
    server.sendmail('vikash.up2109@gmail.com', to, content)
    server.close()

if __name__=="__main__":
    # chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    wishMe()
    while True:
        query = takeCommand()
        # logic for executing tasks based on query

        if 'hello' in query:
            speak('Hi Sir, How are you?')
        
        elif 'hay' in query:
            speak('Hi Sir, How are you?')

        elif 'good' in query:
            speak('I am also good')

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'search' in query:
            reg_ex = re.search('search (.*)', query)
            if reg_ex:
                search_txt = query.split('search',1)[1]
                print('Searching'+search_txt)
                driver = webdriver.Chrome(executable_path='C://chromedriver.exe')
                driver.get('https://www.google.co.in')
                search = driver.find_element_by_name('q')
                search.send_keys(str(search_txt))
                search.send_keys(Keys.RETURN)
            else:
                print('HAHA')
                


        elif 'open youtube' in query:
            driver = webdriver.Chrome(executable_path='C://chromedriver.exe')
            driver.get('https://www.youtube.com')

        elif 'open google' in query:
            driver = webdriver.Chrome(executable_path='C://chromedriver.exe')
            driver.get('https://www.google.co.in')
        
        elif 'open coursera' in query:
            driver = webdriver.Chrome(executable_path='C://chromedriver.exe')
            driver.get('https://www.coursera.org')
        
        # elif 'open zerodha' in query:
        #     driver = webdriver.Chrome(executable_path='C://chromedriver.exe')
        #     driver.get('https://www.kite.zerodha.com')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\vikas\\Downloads\\New folder\\New folder'
            songs = os.listdir(music_dir)
            index = random.randint(0,54)
            os.startfile(os.path.join(music_dir, songs[index]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, It's {strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Users\\vikas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to vikas' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "email to whom you want to send"
                sendEmail(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Sorry Sir, Email has not been sent. Please try again.")
        elif 'quit' in query:
            exit()
        elif 'stop' in query:
            exit()