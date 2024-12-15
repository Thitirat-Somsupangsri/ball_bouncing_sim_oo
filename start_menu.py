import turtle


class StartSimulator:
    def __init__(self, bg_image="bg.gif", game_class=None):
        self.screen = turtle.Screen()
        self.screen.title("Collecting Snow Time!")
        self.screen.bgcolor("grey")
        self.screen.setup(width=800, height=600)
        self.screen.bgpic(bg_image)
        self.start_button_drawn = False
        self.game_class = game_class

        turtle.hideturtle()

    def draw_start_button(self):
        turtle.penup()
        turtle.goto(-60, -10)
        turtle.pendown()
        turtle.color("Lavender")
        turtle.pensize(3)
        turtle.begin_fill()
        turtle.color("Lavender", "pink")
        for _ in range(2):
            turtle.forward(120)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(0, -5)
        turtle.color("black")
        turtle.write("START", align="center", font=("American Typewriter", 24, "bold"))
        self.start_button_drawn = True

    def draw_welcome_message(self):
        turtle.speed("fastest")
        turtle.penup()
        turtle.goto(0, 150)
        turtle.color("LightYellow")
        turtle.write("Summer has passed!", align="center", font=("American Typewriter", 32, "bold"))

        turtle.goto(0, 80)
        turtle.write("Help the snowman collect snows and get ready for Christmas!",
                     align="center", font=("American Typewriter", 22, "normal"))

    def button_clicked(self, x, y):
        if -60 <= x <= 60 and -10 <= y <= 40:
            return True
        return False

    def start_simulation(self, x, y):
        if self.button_clicked(x, y):
            self.screen.clear()
            game = self.game_class()
            game.run()
            turtle.done()

    def run(self):
        self.draw_welcome_message()
        self.draw_start_button()
        turtle.onscreenclick(self.start_simulation)
        turtle.done()
