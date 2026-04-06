"""
Pong Game
---------
A classic two-player Pong game built using Python's turtle module.
Players control paddles to bounce the ball and score points against each other.

Features:
- Two-player gameplay (keyboard controlled)
- Ball movement with increasing speed over time
- Collision detection with walls and paddles
- Score tracking system
- Ball resets after each point

Controls:
- Right paddle: Up / Down arrows
- Left paddle: W / S keys

Logic:
- The game runs in a continuous loop updating the screen
- The ball moves automatically and bounces off top/bottom walls
- When the ball hits a paddle, it reverses direction and speeds up
- If the ball passes a paddle, the opponent scores a point
- The ball resets to the center after each score

Technologies:
- Python
- turtle
- time

Structure:
- `Paddle`: Controls paddle movement
- `Ball`: Handles movement, speed, and collisions
- `Scoreboard`: Tracks and displays player scores
"""

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
game_is_on = True


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.speed(ball.speed() + 1)
        ball.bounce_x()
    if ball.xcor() > 380:
        score.l_point()
        ball.restart()
    if ball.xcor() < -380:
        score.r_point()
        ball.restart()


screen.exitonclick()
