def takeCommand1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query1 = r.recognize_google(audio, language='en-in')
        
    except Exception as e:
       
        return "None"
    return query1

    elif 'shutdown' in query1:
        speak('ok sir')
        break
    
    