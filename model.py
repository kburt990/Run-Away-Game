import pygame
from abc import ABC,abstractmethod
import random





class Unit:
    def __init__(self,x,y):
        self._x=x
        self._y=y

    def get_coords(self):
        return (self._x,self._y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y





class Player(Unit):
    def __init__(self):
        Unit.__init__(self,0,0)
        self.velocity = 1
        self._height = 25
        self._width = 25

    def move_left(self):
        self._x-=self.velocity

    def move_right(self):
        self._x+=self.velocity

    def move_up(self):
        self._y-=self.velocity

    def move_down(self):
        self._y+=self.velocity

    def get_veloctiy(self):
        return self.velocity

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

class Enemy(Unit):
    def __init__(self):
        rand_x=random.randint(0,800)
        rand_y=random.randint(0,800)
        Unit.__init__(self, rand_x,rand_y)
        self.velocity = 3
        self._height = 8
        self._width = 8







