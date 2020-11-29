import os
import signal
import time, settings, voice

class Initial:
	def keyWord():
		return {"reboot system": "rebootMod"}

	def execute(response):
		voice.speak("Rebooting systems now")
		os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
		os.system('start python main.py &')
		time.sleep(2)
		os.kill(int(settings.getVal('oldpid', 'DEFAULT')), signal.SIGTERM)