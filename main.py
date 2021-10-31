import numpy as np
from PIL import Image

class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.data[:] = self.color


    def make(self):  # Create a 3d numpy array of zeros
        img = Image.fromarray(self.data, 'RGB')
        img.save("canvas.png")


class Square:

    def __init__(self, point0, point1, size_of_side, color):
        self.point0 = point0
        self.point1 = point1
        self.size_of_side = size_of_side
        self.color = color

    def draw(self,canvas):
        canvas.data[self.point0:self.point0+self.size_of_side,self.point1:self.point1+self.size_of_side] = self.color


class Rectangle:

    def __init__(self, point0, point1, width, height, color):
        self.point0 = point0
        self.point1 = point1
        self.width = width
        self.height = height
        self.color = color

    def draw(self,canvas):
        canvas.data[self.point0:self.point0 + self.width,self.point1:self.point1 + self.height] = self.color

if __name__ == "__main__":
    canvas = Canvas(1000,1000,[100,100,100])
    square = Square(0,5,100,[105,110,115])
    square.draw(canvas)
    rectangle = Rectangle(110,115,100,200,[125,130,125])
    rectangle.draw(canvas)
    canvas.make()

# Challenge create a circle shape class
