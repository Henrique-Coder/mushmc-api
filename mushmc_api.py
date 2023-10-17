from pprint import pprint
from requests import get


base_api_url = 'http://mush.com.br/api/player'


class MushMC:
    @staticmethod
    def get_api_response(url: str):
        return get(url, allow_redirects=True).json()

    class Player:
        def __init__(self, nick_or_uuid: str):
            self.raw_response = self._get(nick_or_uuid)
            self.first_login = self.raw_response.get('first_login')
            self.last_login = self.raw_response.get('last_login')
            self.is_online = self.raw_response.get('connected')
            self.discord = self.raw_response.get('discord')
            self.account = self.raw_response.get('account')
            self.rank = self.raw_response.get('rank')
            self.clan = self.raw_response.get('clan')

        @staticmethod
        def _get(nick_or_uuid: str) -> dict:
            url = f'{base_api_url}/{nick_or_uuid}'
            data = MushMC.get_api_response(url)
            if not data['success'] or not data['response'].get('success', True):
                raise ValueError(f'"{nick_or_uuid}" has never been registered on MushMC.')
            return data['response']

        def stats(self, game: str) -> dict:
            return self.raw_response.get('stats', {}).get(game, None)


pprint(MushMC.Player('FHDP').account)
