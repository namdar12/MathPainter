from Canvas import Canvas
from Rectangle import Rectangle
from Square import Square

if __name__ == "__main__":
    canvas_width = int(input("Please enter the width of the canvas: "))
    canvas_height = int(input("Please enter the height of the canvas: "))
    canvas_red = int(input("Please enter the how much red for canvas: "))
    canvas_blue = int(input("Please enter the how much blue for canvas: "))
    canvas_green = int(input("Please enter the how much green for canvas: "))

    canvas = Canvas(canvas_width, canvas_height, [canvas_red, canvas_blue, canvas_green])
    if canvas_height != None:
        while True:
            shape = input("Please enter the shape you would like to draw: ")
            if shape.lower() == "square":
                square_x = int(input("Please enter the point x of the square: "))
                square_y = int(input("Please enter the point y of the square: "))
                square_size = int(input("Please enter the size of the square: "))
                square_red = int(input("Please enter the how much red for square: "))
                square_blue = int(input("Please enter the how much blue for square: "))
                square_green = int(input("Please enter the how much green for square: "))
                square = Square(square_x, square_y, square_size, [square_red, square_blue, square_green])
                square.draw(canvas)
            elif shape.lower() == "rectangle":
                rectangle_x = int(input("Please enter the point x of the rectangle: "))
                rectangle_y = int(input("Please enter the point y of the rectangle: "))
                rectangle_width = int(input("Please enter the width of the rectangle: "))
                rectangle_height = int(input("Please enter the height of the rectangle: "))
                rectangle_red = int(input("Please enter the how much red for rectangle: "))
                rectangle_blue = int(input("Please enter the how much blue for rectangle: "))
                rectangle_green = int(input("Please enter the how much green for rectangle: "))
                rectangle = Rectangle(rectangle_x, rectangle_y, rectangle_width, rectangle_height,
                                      [rectangle_red,rectangle_blue,rectangle_green])
                rectangle.draw(canvas)
            elif shape.lower() == "quit":
                break
            else:
                print("Please enter Square or rectangle...Thanks: ")

    canvas.make()

