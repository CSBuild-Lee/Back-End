# from rest_framework import serializers, viewsets
# # from .models import PersonalNote
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# # from pusher import Pusher
# from django.http import JsonResponse
# from decouple import config
# from django.contrib.auth.models import User 
# import json
# from .models import Room, room_dict, Player
# from rest_framework import permissions
# from rest_framework.decorators import api_view, permission_classes
# from uuid import uuid4
# import random
# from django.core.serializers.json import DjangoJSONEncoder

# @csrf_exempt
# @api_view(["GET"])
# @permission_classes((permissions.AllowAny,))
# def initialize(request):
#     user = request.user
#     # initialize rooms
#     for i in range(1,101):
#         r = Room()
#         r.id = i
#         r.room_type = random.choice(list(room_dict.keys()))
#         r.value = room_dict[r.room_type]
#         r.save()
#     user.player = Player()
#     player = user.player
#     # player_id = player.id
#     # # uuid4 = player.uuid
#     # room = player.room()
#     def get_queryset(self):
#         user = self.request.user
#     rooms = Room.objects.all().values_list('id','room_type','value','isDead')
#     # prices = Price.objects.filter(product=product).values_list('price','valid_from')
#     # rooms = [room for room in Room.objects.all()]
#     print(rooms)
#     rooms_json = json.dumps(list(rooms), cls=DjangoJSONEncoder)
#     # rooms_json = rooms_json[1:-1]
#     print(rooms_json)
#     return JsonResponse({'rooms': rooms_json, 'value': player.calories, 'killed': player.num_rooms_eaten, 'room_id':1})

# @api_view(["POST"])
# @permission_classes((permissions.AllowAny,))
# def move(request):
#     player = request.user.player
#     data = json.loads(request.body)
#     direction = data['direction']
#     player.eat(direction)
#     player.save()
#     rooms = [room for room in Room.objects.all()]
#     return JsonResponse({'rooms': rooms, 'value': player.calories, 'killed': player.num_rooms_eaten, 'room_id':player.room_id})



from rest_framework import serializers, viewsets
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User 
import json
from .models import Room, room_dict, Player
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from uuid import uuid4
import random
from django.core.serializers.json import DjangoJSONEncoder

@csrf_exempt
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def initialize(request):
    user = request.user
    # initialize rooms
    for i in range(1,101):
        r = Room()
        r.id = i
        r.room_type = random.choice(list(room_dict.keys()))
        r.value = room_dict[r.room_type]
        r.save()
    user.player = Player()
    player = user.player
    def get_queryset(self):
        user = self.request.user
    rooms = Room.objects.all().values_list('id','room_type','value','isDead')
    rooms_json = json.dumps(list(rooms), cls=DjangoJSONEncoder)
    rooms_list = json.loads(rooms_json)
    return JsonResponse({'rooms': rooms_list, 'value': player.calories, 'killed': player.num_rooms_eaten, 'room_id':1})

@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def move(request):
    player = request.user.player
    data = json.loads(request.body)
    direction = data['direction']
    player.eat(direction)
    player.save()
    # getting list of rooms to return
    rooms = Room.objects.all().values_list('id','room_type','value','isDead')
    rooms_json = json.dumps(list(rooms), cls=DjangoJSONEncoder)
    rooms_list = json.loads(rooms_json)
    return JsonResponse({'rooms': rooms_list, 'value': player.calories, 'killed': player.num_rooms_eaten, 'room_id':player.room_id})