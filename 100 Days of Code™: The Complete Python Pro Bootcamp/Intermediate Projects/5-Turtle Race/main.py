"""
Turtle Race Game
----------------
A simple interactive racing game built with Python's turtle module.
The user places a bet on a turtle color and watches multiple turtles
race across the screen with random movement.

Features:
- User input for selecting a turtle color
- Six turtles with different colors
- Randomized movement to simulate a race
- Real-time animation using turtle graphics
- Displays win/lose result based on the user's bet

Logic:
- Turtles start from the same x position with different y positions
- Each turtle moves forward by a random distance in each loop
- The first turtle to reach the finish line wins

Technologies:
- Python
- turtle
- random
"""



from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=900, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:\n red, orange, yellow, green, blue, purple")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
is_race_on = False

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-430, y=-100 + (i * 50))
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() >= 415:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                screen.title(f"You've won! The {winner_color} turtle is the winner!")
            else:
                screen.title(f"You've lost! The {winner_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)









screen.exitonclick()
