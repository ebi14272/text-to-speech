import pyttsx3

def speak(txt):
    engine = pyttsx3.init()
    engine.setProperty('rate' , 120)
    voices = engine.getProperty("voices")
    engine.say(txt)
    engine.runAndWait()
while True :
    text = input("wright youre sentences here >>> ")
    speak(text)
