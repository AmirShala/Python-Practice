from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

my_snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # Detect a collision with food
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        score.increase_score()

    # Detect a collision with a wall
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -300 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()


    # Detect tail collision
    for segment in my_snake.segments[1:]: 
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()




















screen.exitonclick()