
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# # from pusher import Pusher
# from django.http import JsonResponse
# from decouple import config
# from django.contrib.auth.models import User
# from .models import *
# from rest_framework.decorators import api_view
# import json

# # instantiate pusher
# # pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

# @csrf_exempt
# @api_view(["GET"])
# def initialize(request):
#     user = request.user
#     player = user.player
#     player_id = player.id
#     uuid = player.uuid
#     room = player.room()
#     players = room.playerNames(player_id)
#     return JsonResponse({'uuid': uuid, 
#     'name': player.user.username, 
#     'title': room.title, 
#     'description': room.description, 
#     'can_make_money': room.can_make_money,
#     'cash': player.cash, 
#     'players': players}, safe=True)




# @csrf_exempt
# @api_view(["POST"])
# def say(request):
#     # IMPLEMENT
#     return JsonResponse({'error':"Not yet implemented"}, safe=True, status=500)