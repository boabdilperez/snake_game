"""Controls the snake food drawing and placement"""
from turtle import Turtle
from random import randint


class Food(Turtle):
    """Class that represents the snake food"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Places new food in a random grid square"""
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(x=random_x, y=random_y)
