"""Module that controls the drawing of the snake onto the screen,
and receives movement commands"""
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Instantiates, draws, and moves the actual on-screen snake"""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Initial starting position of the snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Grows the snake by a unit of one segment"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        """Controls snake movement"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        """Move the snake up, if able"""
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def move_down(self):
        """Move the snake down, if able"""
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def move_left(self):
        """Move the snake left, if able"""
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def move_right(self):
        """Move the snake right, if able"""
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def extend(self):
        """Calls add_segment to add a new block to the snake's tail"""
        self.add_segment(self.segments[-1].position())
