class Square:

    def __init__(self, point0, point1, size_of_side, color):
        self.point0 = point0
        self.point1 = point1
        self.size_of_side = size_of_side
        self.color = color

    def draw(self,canvas):
        canvas.data[self.point0:self.point0+self.size_of_side,self.point1:self.point1+self.size_of_side] = self.color