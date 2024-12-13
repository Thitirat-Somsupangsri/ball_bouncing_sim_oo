import turtle


class Heart:
    def __init__(self, color, my_turtle):
        self.size = 10
        self.location = [0, 0]
        self.color = color
        self.my_turtle = my_turtle
        self.my_turtle.penup()
        self.my_turtle.setheading(0)
        self.my_turtle.hideturtle()
        self.my_turtle.speed(10)

    def set_location(self, location):
        self.location = location
        self.my_turtle.goto(self.location[0], self.location[1])

    def draw(self):
        self.my_turtle.penup()
        self.my_turtle.goto(self.location)
        self.my_turtle.pendown()

        self.my_turtle.begin_fill()
        self.my_turtle.fillcolor(self.color)

        self.my_turtle.left(50)
        self.my_turtle.forward(self.size)
        self.my_turtle.circle(self.size / 2, 200)
        self.my_turtle.right(140)
        self.my_turtle.circle(self.size / 2, 200)
        self.my_turtle.forward(self.size)

        self.my_turtle.end_fill()

    def clear(self):
        self.my_turtle.clear()


'''
tom = turtle.Turtle()
hearts = Heart("Blue", tom)
hearts.draw()

turtle.done()
'''