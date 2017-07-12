from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transferchecker.functions.requestor import Requestor

@csrf_exempt
def index(request):
    requestor = Requestor()

    # passing data to front end
    if request.method == 'POST':

        # full player info to populate search autocomplete
        all_player_info = requestor.get_all_player_info()

        # all players currently taken
        user_list = []
        #user_list = requestor.get_group_ids('508077')
        taken_list = []
        for id in user_list:
            user_gameweek_roster = requestor.get_user_gameweek_roster(id, '38')
            for player_id in user_gameweek_roster:
                taken_list.append(player_id)

        data = {
            'all_player_info': all_player_info,
            'taken_list': taken_list
        }
        return JsonResponse(data)

    return render(request, 'transferchecker/index.html')