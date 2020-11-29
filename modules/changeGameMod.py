import re
import requests
import settings

class Initial:
	def keyWord():
		return {"change game": "changeGameMod"}

	def execute(response):
		game = response[re.search(r'\b(change game to)\b', response).end() + 1: len(response)]
		url = ('https://api.twitch.tv/v5/channels/%s' % settings.getVal('id', 'TWITCH'))
		payload = ('{"channel": {"game": "%s"}}' % game)
		headers = ({'Content-Type': 'application/json', 'Accept': 'application/vnd.twitchtv.v5+json',
					'Authorization': 'OAuth %s' % settings.getVal('oauth', 'TWITCH')})
		r = requests.put(url, data=payload, headers=headers)