from rest_framework import serializers, viewsets
# from .models import PersonalNote
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
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

# class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
#     # Inner class nested inside PersonalNoteSerializer
#     class Meta:
#         model = PersonalNote
#         fields = ('title', 'content')

#     def create(self, validated_data):
#         user = self.context['request'].user
#         note = PersonalNote.objects.create(user=user, **validated_data)
#         return note


# class PersonalNoteViewSet(viewsets.ModelViewSet):
#         serializer_class = PersonalNoteSerializer
#         # queryset = PersonalNote.objects.all()
#         queryset = PersonalNote.objects.none()

#         def get_queryset(self):
#             user = self.request.user

#             if user.is_anonymous:
#                 return PersonalNote.objects.none()
#             else:
#                 return PersonalNote.objects.filter(user=user)


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
    # player_id = player.id
    # # uuid4 = player.uuid
    # room = player.room()

    def get_queryset(self):
        user = self.request.user

    # rooms = [room for room in Room.objects.all()]
    print(rooms)
    print(type(rooms))

    rooms = Room.objects.all().values_list('id','type','value','isDead')
    # prices = Price.objects.filter(product=product).values_list('price','valid_from')

    rooms_json = json.dumps(list(rooms), cls=DjangoJSONEncoder)

    return JsonResponse({'rooms': rooms, 'value': player.calories, 'killed': player.num_rooms_eaten, 'room_id':1})
# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((permissions.AllowAny,))
# def move(request):

#     player = request.user.player
#     player_id = player.id
#     player_uuid = player.uuid
#     data = json.loads(request.body)
#     direction = data['direction']
#     room = player.room()
#     nextRoomID = None
#     if direction == "n":
#         nextRoomID = room.n_to
#     elif direction == "s":
#         nextRoomID = room.s_to
#     elif direction == "e":
#         nextRoomID = room.e_to
#     elif direction == "w":
#         nextRoomID = room.w_to
#     if nextRoomID is not None and nextRoomID > 0:
#         nextRoom = Room.objects.get(id=nextRoomID)
#         player.currentRoom=nextRoomID
#         player.save()
#         players = nextRoom.playerNames(player_id)
#         currentPlayerUUIDs = room.playerUUIDs(player_id)
#         nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
#         for p_uuid in currentPlayerUUIDs:
#             pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
#         for p_uuid in nextPlayerUUIDs:
#             pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
#         return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'players':players, 'error_msg':""}, safe=True)
#     else:
#         players = room.playerNames(player_id)
#         return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'error_msg':"You cannot move that way."}, safe=True)

# @csrf_exempt
@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def move(request):
    player = request.user.player
    data = json.loads(request.body)
    direction = data['direction']
    player.eat(direction)
    player.save()
    rooms = [room for room in Room.objects.all()]
    return JsonResponse({'rooms': rooms, 'value': player.calories, 'killed': player.num_rooms_eaten, 'room_id':player.room_id})