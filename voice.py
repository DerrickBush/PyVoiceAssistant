import pyttsx3
import settings

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[int(settings.getVal('voice', 'TTS'))].id)
# engine.setProperty('volume', float(settings.getVal('volume', 'TTS')))

def speak(text):
    engine.setProperty('voice', voices[int(settings.getVal('voice', 'TTS'))].id)
    engine.setProperty('volume', float(settings.getVal('volume', 'TTS')))
    engine.say(text)
    engine.runAndWait()

def updateSettings(setting, newVal):
    pass