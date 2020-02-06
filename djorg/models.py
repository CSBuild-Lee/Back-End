import random
from django.db import models
from django.contrib.auth.models import User

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
    room_type = models.CharField(default = random.choice(room_dict.keys()))
    value = models.IntegerField(default = room_dict[room_type])
    isDead = models.BooleanField(default=False)

    def __str__(self)

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __init__(self):
        
        self.row = models.IntegerField(default = 0)
        self.col = models.IntegerField(default = 0)
        self.calories = models.IntegerField(default = 0)
        self.room_id = models.IntegerField(default = 1)
        # changing room where player spawns to eaten without updating calories
        # so that room will only show player and not vegetable
        self.Room().isDead = True
        self.num_rooms_eaten = models.IntegerField(default = 0)
    
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
