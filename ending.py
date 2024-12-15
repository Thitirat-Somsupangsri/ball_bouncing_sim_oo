import turtle


class EndingScene:
    def __init__(self, score, needed_ball, heart):
        self.screen = turtle.Screen()
        self.screen.title("Collecting Snow Time!")
        self.screen.bgcolor("LightBlue")
        self.screen.setup(width=800, height=600)
        self.start_button_drawn = False
        self.score = score
        self.needed_ball = needed_ball
        self.heart = heart
        turtle.hideturtle()

    def draw_lose_ending(self):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.color("MediumVioletRed")
        turtle.write("You lose", align="center", font=("American Typewriter", 24, "normal"))
        turtle.penup()
        turtle.goto(0, -30)
        turtle.write("Try again?", align="center", font=("American Typewriter", 24, "normal"))

    def draw_win_ending(self):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.color("SlateGray")
        turtle.write("All Snowballs Collected!",
                     align="center", font=("American Typewriter", 24, "normal"))
        turtle.penup()
        turtle.goto(0, -30)
        turtle.write("The snowman is very satisfied!",
                     align="center", font=("American Typewriter", 24, "normal"))

    def display_ending(self):
        if self.heart <= 0:
            self.draw_lose_ending()
        elif self.score >= self.needed_ball:
            self.draw_win_ending()
