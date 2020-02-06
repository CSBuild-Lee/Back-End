from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
import random

# # Create your models here.
# class Note(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     title = models.CharField(max_length=200)
#     content = models.TextField(blank=True)

# class PersonalNote(Note):   # Inherits from Note!
#     user = models.ForeignKey(User, on_delete=models.CASCADE)




room_dict = {
    'Lettuce' : 50,
    'Cucumber': 160,
    'Tomato': 180,
    'Eggplant': 200,
    'Carrot': 250,
    'Pepper': 300,
    'Broccoli': 500,
    'Corn': 850,
    'Potato': 1630,
    'Yam': 1770,
}

class Room(models.Model):
    # id?
    room_type = models.CharField(max_length = 600 , default = random.choice(list(room_dict.keys())))
    # print(room_dict)
    # print(room_type)
    # print(dir(room_type))
    value = models.IntegerField(default = 0)
    isDead = models.BooleanField(default=False)

    def __str__(self):
        string = {
            'id': self.id,
            'type': self.room_type,
            'value': self.value,
            'isDead': self.isDead,
            }
        return string

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid4 = models.UUIDField(default=uuid4, unique=True)
    row = models.IntegerField(default = 0)
    col = models.IntegerField(default = 0)
    calories = models.IntegerField(default = 0)
    room_id = models.IntegerField(default = 1)
    num_rooms_eaten = models.IntegerField(default = 0)
    # changing room where player spawns to eaten without updating calories
    # so that room will only show player and not vegetable
    # Room().isDead = True
    
    def eat(self, direction):
        self.__move__(direction)
        self.__eat_current_loc__()

    def __move__(self, direction):
        error = 'error, can not move in that direction'

        if direction == 'Up':
            # check if player can move
            if self.row == 0:
                return error
            # move player
            else:
                self.row -= 1
        
        if direction == 'Down':
            if self.row == 9:
                return error
            else:
                self.row += 1
        
        if direction == 'Right':
            if self.col == 9:
                return error
            else:
                self.col += 1
        
        if direction == 'Left':
            if self.col == 0:
                return error
            else:
                self.col -= 1

        self.room_id = (self.row*10) + (self.col+1)
    
    def __eat_current_loc__(self):
        # update player calories
        self.calories += self.Room().value
        # change room to eaten
        self.Room().isDead = True
        self.num_rooms_eaten += 1

    def Room(self):
        return Room.objects.get(id=self.room_id)
# objects to return


