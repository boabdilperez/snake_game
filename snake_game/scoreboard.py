"""Draw and update the scoreboard"""
from turtle import Turtle

SCOREBOARD_COORDINATES = (0, 275)
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    """Class that controls scoreboard instances"""

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
        """Increases score by one"""
        self.score += 1
        self.clear()
        self.write(
            arg=f"Score: {self.score}", align="center", font=("Arial", 20, "normal")
        )

    def game_over(self):
        """Draws game over message to the screen"""
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 20, "normal"))
