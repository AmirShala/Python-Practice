"""
Crossing Game (Frogger Style)
-----------------------------
A simple arcade-style game where the player moves upward to cross the road
while avoiding moving cars.

Features:
- Player movement controlled by keyboard (Up arrow)
- Continuously spawning and moving cars
- Collision detection with cars
- Level progression with increasing difficulty
- Scoreboard displaying current level
- Game over on collision

Logic:
- The game runs in a loop updating the screen
- Cars are generated and move across the screen
- If the player collides with a car, the game ends
- When the player reaches the finish line, they reset position,
  the level increases, and car speed increases

Technologies:
- Python
- turtle
- time

Structure:
- `Player`: Handles movement and position reset
- `CarManager`: Manages car creation, movement, and speed
- `Scoreboard`: Tracks level and displays game status
"""


import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        scoreboard.level_up()

screen.exitonclick()
