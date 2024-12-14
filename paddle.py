class Paddle:
    def __init__(self, height, width, image, my_turtle):
        self.location = [0, 0]
        self.image = image
        self.height = height
        self.width = width
        self.my_turtle = my_turtle

    def set_location(self, location):
        self.location = location
        self.my_turtle.goto(self.location[0], self.location[1])

    def draw(self):
        self.my_turtle.shape(self.image)

    def clear(self):
        self.my_turtle.clear()

    def __str__(self):
        return "paddle"
