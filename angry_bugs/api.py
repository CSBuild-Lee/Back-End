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
import random

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

    def get_queryset(self):
        user = self.request.user

    rooms = [room for room in Room.objects.all()]
    rooms = Room.objects.all()
    return JsonResponse({'rooms': list(rooms), 'value': player.calories, 'killed': player.num_rooms_eaten, 'room_id':1})


# @csrf_exempt
@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def move(request):

    player = request.user.player
    data = json.loads(request.body)
    direction = data['direction']
    player.eat(direction)
    player.save()
    rooms = Room.objects.all()

    return JsonResponse({'rooms': str(rooms), 'value': player.calories, 'killed': player.num_rooms_eaten, 'room_id':player.room_id})