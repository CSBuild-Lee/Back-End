from random import randint
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

class Room:
    def __init__(self, row, col):
        random_num = randint(0,len(list(room_dict.keys()))-1)
        self.room_type = list(room_dict.keys())[random_num]
        self.calories = room_dict[self.room_type]
        self.eaten = False
        # id from 1-100
        self.id = (10*row + col) + 1

# Board is 10 x 10 list
def init_board():
    rows = []
    for row_num in range(10):
        rows.append([])
        for col_num in range(10):
            rows[row_num].append(Room(row_num, col_num))
    return rows

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __init__(self):
        
        self.row = models.IntegerField(default = randint(0,9))
        self.col = models.IntegerField(default = randint(0,9))
        self.calories = models.IntegerField(default = 0)
        self.board = init_board()
        # changing room where player spawns to eaten without updating calories
        # so that room will only show player and not vegetable
        self.board[self.row][self.col].eaten = True
        self.num_rooms_eaten = 0
    
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
    
    def __eat_current_loc__(self):
        # update player calories
        self.calories += self.board[self.row][self.col].calories
        # change room to eaten
        self.board[self.row][self.col].eaten = True
        self.num_rooms_eaten += 1
# objects to return

