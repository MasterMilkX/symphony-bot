import random
import sys
import numpy as np


class SongMap():
    def __init__(self, width, height):
        self.ascii_map = []
        self.width = width
        self.height = height

        #assumate a pokemon map for now
        self.characters = {"player":"@",'tree':'♣',"trainer":"O","grass":".","path":"_"}
        
    #create a map of the given size
    def init_rand_map(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(self.characters["grass"])
            self.ascii_map.append(row)

    #print the map
    def print_map(self):
        for row in self.ascii_map:
            print("".join(row))
    
    #place the player on the map
    def place_player(self):
        #get a random position
        x = random.randint(0,self.width-1)
        y = random.randint(0,self.height-1)
        self.ascii_map[y][x] = self.characters["player"]


        
