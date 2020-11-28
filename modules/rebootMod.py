import os
import signal
import time
import settings
import voice

class Initial:
	def keyWord():
		return {"reboot system": "rebootMod"}

	def execute(response):
		voice.speak("Rebooting systems now")
		os.chdir('C:/Users/derri/Documents/Projects/voiceAI/pyAI/')
		os.system('start python main.py &')
		time.sleep(2)
		os.kill(int(settings.getVal('oldpid', 'DEFAULT')), signal.SIGTERM)

