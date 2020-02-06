# copied from example project

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User 
from rest_framework.decorators import api_view
import json
from .models import Room, room_dict, Player

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

@csrf_exempt
@api_view(["GET"])
def initialize(request):

    user = request.user

    # initialize rooms
    for i in range(1,101):
        r = Room()
        r.id = i
        r.value = room_dict[r.room_type]
        r.save()

    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()

    rooms = Room.objects.all()
    return JsonResponse({rooms, {'value': player.calories, 'killed': player.num_rooms_eaten}, {'room_id':1}})


# @csrf_exempt
@api_view(["POST"])
def move(request):

    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    player.eat(direction)
    player.save()
    players = nextRoom.playerNames(player_id)
    return JsonResponse({rooms, {'value': player.calories, 'killed': player.num_rooms_eaten}, {'room_id':1}})

@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error':"Not yet implemented"}, safe=True, status=500)