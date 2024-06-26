
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
       
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

while True:
    query1 = takeCommand1().lower()
    if 'jarvis' in query1:
        speak("yes sir what can i do for you")
        while True:
            
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                break 

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                speak("ok sir!!! opening youtube")
                speak("any other work for me?")
                break 

            elif 'open google' in query:
                webbrowser.open("google.com")
                speak("ok sir!!! opening google.com")
                speak("any other work for me?")
                break 

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
                speak("any other work for me?")
                break 

            elif 'play music' in query:
                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
                speak("any other work for me?")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                speak("any other work for me?")

            elif 'open browser' in query:
                codepath="C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(codepath)
                speak("opening browser ")
                speak("any other work for me?")

            elif 'who are you' in query:
                speak('i am jarvis version 6.1.4 .  personal ai of rajiv ')
                speak('what can i do for you')

            elif 'read' in query:
                speak('sir paste here text')
                k=input(_)
                speak(k)
                break 

            elif 'open python' in query:
                codePath ='C:\\Users\\Rajiv\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.10\\IDLE (Python 3.10 32-bit).lnk'
                os.startfile(codePath)
                speak("ok sir!!! opening python")
                speak("any other work for me?")
                break 

            elif 'what happen jarvis' in query or 'jarvis what happen' in query:
                speak('i am searching the problem sir ,. something wrong happened , i will fix it .')
                break 

            elif 'about you' in query:
                speak('i am jarvis (just a really very intelligent system )')
                speak('created by rajiv ')
                speak('family : rajiv')
                speak('i was activate on 25 march 2023 at 1517 hours ')
                speak("i am running and taking care of all the internal system of rajiv's pc")

            elif 'what can you do' in query:
                speak("i can uses several artificial intelligence techniques ,including natural language processing ,speach recognition")
                speak("what can i do for you")

            elif ('you are dumb' in query) or ('you are bad' in query) or ('you are mad' in query):
                speak('sorry sir!! i will learn more')

            elif ('you are good' in query)or('you are cool' in query)or('you are best' in query):
                speak('thank you sir!! i will learn more')
                speak("any work for me?")

            elif 'no other work' in query:
                speak("ok sir you can ask me any time")
                break

            elif 'no work' in query:
                speak("ok sir you can ask me any time")
                break
 
            elif 'you can sleep ' in query:
                speak("ok sir you can ask me any time")
                break 

            elif 'sleep jarvis' in query:
                speak("ok sir you can ask me any time")
                break

            elif ('no' in query)or ('nothing' in query):
                speak("ok sir you can ask me any time")
                break

            elif 'shutdown' in query1:
                speak('ok sir')
                break
    

            else:
                speak("sorry sir i have not caught your words please say again ")
