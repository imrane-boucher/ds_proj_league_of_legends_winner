import requests
import pandas as pd



class RiotAPI(object):

    def __init__(self, api_key):
        self.api_key = api_key
    
    def _request(self, id_match):
        args = {'api_key': self.api_key}
        r = requests.get('https://euw1.api.riotgames.com/lol/match/v4/matches/{}'.format(id_match),
        params=args)
        return r.json()

    def get_game_duration(self, id_match):
        return self._request(id_match)




