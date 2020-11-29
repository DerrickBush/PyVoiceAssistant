import speech_recognition as sr
import os
import settings
import voice

# Sets pid in storage to close out old instance
settings.setVal('oldpid', 'DEFAULT', settings.getVal('newpid', 'DEFAULT'))
settings.setVal('newpid', 'DEFAULT', str(os.getpid()))
# Creates moduleDictionary and ignoreList for importing modules and gets keywords
moduleDictionary = {}
ignoreList = {'__init__.py', '__pycache__', 'template.py', 'config.json'}
keywords = settings.getVal('keywords', 'DEFAULT')
voiceAssistant = sr.Recognizer()


class RunMod:
    def __init__(self, module_name, class_name, response):
        module = __import__('modules.' + module_name, fromlist=['*'])
        my_class = getattr(module, class_name)
        my_class.execute(response)


def loadModules():
    entries = os.listdir('modules/')
    for mods in entries:
        if mods not in ignoreList:
            module = __import__('modules.' + mods.split('.')[0], fromlist=['*'])
            mod_class = getattr(module, 'Initial')
            moduleDictionary.update(mod_class.keyWord())


def executeResponse(command):
    print(command)
    if command.split()[0] in keywords:
        for mod in moduleDictionary:
            if mod.lower() in command.lower():
                obj = RunMod(moduleDictionary.get(mod), "Initial", command)


loadModules()
voice.speak("All systems nominal")
while True:
    try:
        with sr.Microphone() as source:
            print("LIstening...")
            voiceAssistant.adjust_for_ambient_noise(source, duration=0.1)
            audio = voiceAssistant.listen(source)
            response = voiceAssistant.recognize_google(audio)
            response = response.lower()
            executeResponse(response)

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
