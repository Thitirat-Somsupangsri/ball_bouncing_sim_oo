import turtle


class Player:
    def __init__(self, shape, size,
                 screen, x=0, y=-100):
        self.screen = screen
        self.size = size
        self.x = x
        self.y = y
        self.player_turtle = turtle.Turtle()
        self.screen.register_shape(shape)
        self.player_turtle.shape(shape)
        self.player_turtle.shapesize(stretch_wid=size, stretch_len=size)
        self.player_turtle.penup()
        self.player_turtle.goto(self.x, self.y)

    def move_left(self):
        boundary = self.screen.window_width()//2 - self.size * 10
        new_x = self.x - 20
        new_x = max(new_x, -boundary)
        self.x = new_x
        self.player_turtle.goto(self.x, self.y)

    def move_right(self):
        boundary = self.screen.window_width()//2 - self.size * 10
        new_x = self.x + 20
        new_x = min(new_x, boundary)
        self.x = new_x
        self.player_turtle.goto(self.x, self.y)

    def move_up(self):
        boundary = self.screen.window_height()//2 - self.size * 10
        new_y = self.y + 20
        if new_y > boundary:
            new_y = - boundary
        self.y = new_y
        self.player_turtle.goto(self.x, self.y)

    def move_down(self):
        boundary = self.screen.window_height()//2 - self.size * 10
        new_y = self.y - 20
        if new_y < - boundary:
            new_y = boundary
        self.y = new_y
        self.player_turtle.goto(self.x, self.y)

    def get_position(self):
        return self.x, self.y
