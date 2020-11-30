from scoreboard import Scoreboard
from food import Food
from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

game_start = True
while game_start:
    # Animate the snake
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision w/food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_increase()

    # Detect Wall Collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_start = False

    # Detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_start = False
            scoreboard.game_over()

screen.exitonclick()
