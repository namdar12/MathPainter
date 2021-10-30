import numpy as np


class Cavnas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def make(self):
        data = np.zeros((self.width, self.height, 3), dtype=np.unit8)  # Create a 3d numpy array of zeros
        data[:] = self.color


class Square:

    def __init__(self, point0, point1, size_of_side, color):
        self.point0 = point0
        self.point1 = point1
        self.size_of_side = size_of_side
        self.color = color

    def draw(self):
        square = np.zeros((self.size_of_side,self.size_of_side,3))
        square[self.point0:self.point1+1] = self.color




class Rectangle:

    def __init__(self, point0, point1, width, height, color):
        self.point0 = point0
        self.point1 = point1
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        rectangle = np.zeros((self.width, self.height, 3))
        rectangle[self.point0:self.point1 + 1] = self.color


if __import__(name="main.py"):


# Challenge create a circle shape class
