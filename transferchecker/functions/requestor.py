import requests

class Requestor(object):
    def __init__(self):
        self.base_url = 'https://fantasy.premierleague.com/drf/'
        self.all_players = None

    def get_group_ids(self, league_id):
        league_url = 'leagues-classic-standings/' + league_id
        request_url = self.base_url + league_url

        league_info = requests.get(request_url).json()
        id_list = []
        for user in league_info['standings']['results']:
            id_list.append(str(user['entry']))
        
        return id_list

    def get_all_player_info(self):

        # so we only have to pull all this once, and only when we need it
        if self.all_players:
            return self.all_players

        players_url = 'elements'
        request_url = self.base_url + players_url

        self.all_players = requests.get(request_url).json()
        return self.all_players

    def get_user_gameweek_roster(self, user_id, gameweek):
        user_roster_url = 'entry/' + user_id + '/event/' + gameweek + '/picks'
        request_url = self.base_url + user_roster_url
        # make request and do something with it

        picks_info = requests.get(request_url).json()
        player_list = []
        for player in picks_info['picks']:
            player_list.append(player['element'])
            
        return player_list 

    def get_user_transfer_history(self, user_id):
        transfer_url = 'entry/' + user_id + '/transfers'
        request_url = self.base_url + transfer_url
        # make request and do something with it
        return requests.get(request_url).json()