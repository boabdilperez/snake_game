from turtle import Turtle

SCOREBOARD_COORDINATES = (0, 275)
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.color("white")
        self.pu()
        self.speed("fastest")
        self.goto(SCOREBOARD_COORDINATES)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 20, "normal"))