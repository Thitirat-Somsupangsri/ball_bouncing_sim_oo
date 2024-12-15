import turtle
import random
import time
from paddle import Player
from object import Snow, Fire
from ending import EndingScene


class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=600)
        self.canvas_width = 800
        self.canvas_height = 600

        self.screen.bgcolor("LightBlue")
        self.screen.title("Snowman Game")
        self.screen.tracer(0)

        self.screen.register_shape("paddle_display.gif")
        self.screen.register_shape("fire.gif")

        self.player = Player("paddle_display.gif", 2, self.screen)

        self.balls = []
        for _ in range(20):
            self.balls.append(Snow(screen=self.screen))
        for _ in range(4):
            self.balls.append(Fire(screen=self.screen))

        self.score = 0
        self.heart = 3
        self.needed_ball = random.randint(40, 80)

        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.color("OliveDrab")
        self.update_pen()

        self.screen.listen()
        self.screen.onkeypress(self.player.move_left, "Left")
        self.screen.onkeypress(self.player.move_right, "Right")
        self.screen.onkeypress(self.player.move_up, "Up")
        self.screen.onkeypress(self.player.move_down, "Down")

        self.game_over = False

        self.drawer_snow = turtle.Turtle()
        self.drawer_snow.hideturtle()
        self.drawer_snow.penup()
        self.drawer_snow.speed(0)

        self.drawer_fire = turtle.Turtle()
        self.drawer_fire.hideturtle()
        self.drawer_fire.penup()
        self.drawer_fire.speed(0)
        self.drawer_fire.shape("fire.gif")

        self.__draw_border()

    def __draw_border(self):
        border = turtle.Turtle()
        border.hideturtle()
        border.penup()
        border.pensize(5)
        border.color("black")

        border.goto(-self.canvas_width / 2, self.canvas_height / 2)  # top-left corner
        border.pendown()

        for _ in range(2):
            border.forward(self.canvas_width)
            border.right(90)
            border.forward(self.canvas_height)
            border.right(90)

        border.penup()

    def update_pen(self):
        self.pen.clear()
        self.pen.goto(0, 260)
        self.pen.write(f"I need {self.needed_ball} snowballs. Please help me",
                       align="center", font=("American Typewriter", 24, "normal"))
        self.pen.goto(0, 230)
        self.pen.write(f"Snow Collected: {self.score} / {self.needed_ball}   Heart: {self.heart}",
                       align="Center", font=("American Typewriter", 24, "bold"))

    def run(self):
        dt = 1.5
        while not self.game_over and self.score < self.needed_ball:
            width = self.screen.window_width()
            height = self.screen.window_height()

            for ball in self.balls:
                ball.move(dt)
                ball.bounce(width, height)

                px, py = self.player.get_position()
                dist = ball.distance_to(px, py)
                if dist < (ball.size * 10 + self.player.size * 10):
                    if ball.status == "player":
                        self.score += 1
                    else:
                        self.heart -= 1
                        if self.heart <= 0:
                            self.game_over = True
                    ball.reset_position(width, height)

            self.drawer_snow.clear()
            self.drawer_fire.clearstamps()

            for ball in self.balls:
                if ball.status == "player":
                    self.drawer_snow.goto(ball.x, ball.y)
                    self.drawer_snow.dot(ball.size * 4, ball.color)
                else:
                    self.drawer_fire.goto(ball.x, ball.y)
                    self.drawer_fire.stamp()

            self.update_pen()
            self.screen.update()
            time.sleep(0.01)

            ending_scene = EndingScene(self.score, self.needed_ball, self.heart)
            ending_scene.display_ending()


if __name__ == "__main__":
    game = Game()
    game.run()
    turtle.done()
