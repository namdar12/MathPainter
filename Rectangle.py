class Rectangle:

    def __init__(self, point0, point1, width, height, color):
        self.point0 = point0
        self.point1 = point1
        self.width = width
        self.height = height
        self.color = color

    def draw(self,canvas):
        canvas.data[self.point0:self.point0 + self.width, self.point1:self.point1 + self.height] = self.color