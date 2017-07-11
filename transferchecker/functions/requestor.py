import requests

class Requestor(object):
    def __init__(self):
        self.base_url = 'https://fantasy.premierleague.com/drf/'

    def get_group_ids(self, league_id):
        league_url = 'leagues-classic-standings/' + league_id
        request_url = self.base_url + league_url

        league_info = requests.get(request_url).json()
        id_list = []
        for user in league_info['standings']['results']:
            id_list.append(str(user['entry']))
        
        return id_list

    def get_team_info(self):
        team_url = 'teams'
        request_url = self.base_url + team_url
        team_info = requests.get(request_url).json()
        return team_info

    def get_all_player_info(self):
        players_url = 'elements'
        request_url = self.base_url + players_url
        all_players = requests.get(request_url).json()
        team_info = self.get_team_info()

        player_info = []
        for i, player in enumerate(all_players):
            # getting player name
            player_name = player['first_name'] + ' ' + player['second_name']

            # getting team name
            team_code = player['team_code']
            team_name = ''
            for team in team_info:
                if team['code'] == team_code:
                    team_name = team['short_name']
                    break

            # putting it all together along with player ID
            player_info.append({
                'player_id': i + 1,
                'player_name': player_name,
                'team_name': team_name
            })
            
        return player_info

    def get_user_gameweek_roster(self, user_id, gameweek):
        user_roster_url = 'entry/' + user_id + '/event/' + gameweek + '/picks'
        request_url = self.base_url + user_roster_url

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