from random import randint

class player:
    def __init__(self):
        row = randint(0,9)
        col = randint(0,9)
        self.location = [row, col]
        self.calories = 0


room_dict = {
    'Lettuce' : 5,
    'Cucumber': 16,
    'Tomato': 18,
    'Eggplant': 20,
    'Carrot': 25,
    'Pepper': 30,
    'Broccoli': 50,
    'Corn': 85,
    'Potato': 163,
    'Yam': 177,
}

class Room:
    def __init__(self):
        random_num = randint(0,len(list(room_dict.keys()))-1)
        self.room_type = list(room_dict.keys())[random_num]
        self.calories = room_dict[self.room_type]
        self.eaten = False

class Board:
    def __init__(self):
        self.rows = []
        for row_num in range(10):
            self.rows.append([])
            for _ in range(10):
                self.rows[row_num].append(Room())