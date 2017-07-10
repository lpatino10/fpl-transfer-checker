from django.shortcuts import render
from django.http import HttpResponse
from transferchecker.functions.requestor import Requestor

def index(request):
    requestor = Requestor()

    user_list = requestor.get_group_ids('508077')
    all_player_info = requestor.get_all_player_info()
    player_list = []
    for id in user_list:
        user_gameweek_roster = requestor.get_user_gameweek_roster(id, '38')

        for player_id in user_gameweek_roster:
            player_element = all_player_info[player_id]
            player_list.append(player_element['first_name'] + ' ' + player_element['second_name'])

    return HttpResponse(', '.join(player_list))