from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transferchecker.functions.requestor import Requestor

@csrf_exempt
def index(request):
    requestor = Requestor()

    all_player_info = requestor.get_all_player_info()

    if request.method == 'POST':
        data = {
            'names': requestor.get_all_player_names()
        }
        return JsonResponse(data)

    user_list = requestor.get_group_ids('508077')

    player_list = []
    for id in user_list:
        user_gameweek_roster = requestor.get_user_gameweek_roster(id, '38')

        for player_id in user_gameweek_roster:
            player_element = all_player_info[player_id]
            player_list.append(player_element['first_name'] + ' ' + player_element['second_name'])

    #return HttpResponse(', '.join(player_list))
    return render(request, 'transferchecker/index.html')