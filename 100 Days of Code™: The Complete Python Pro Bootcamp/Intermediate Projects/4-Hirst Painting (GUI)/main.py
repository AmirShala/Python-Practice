"""
Turtle Dot Painting (Hirst Style)

Overview:
---------
This script uses the turtle module to generate a grid of colored dots,
inspired by Damien Hirst-style artwork. Colors are randomly selected
from a predefined RGB list (optionally extracted using colorgram).

Functionality:
--------------
- Sets turtle color mode to RGB (0–255)
- Positions turtle at a starting point
- Draws a 10x10 grid of dots
- Each dot is randomly colored from a predefined palette
- Moves horizontally to draw a row, then shifts vertically for the next row

Functions:
----------
draw_dot(line_number: int) -> None
    Draws a single row of 10 dots and repositions the turtle
    to the beginning of the next line.

Variables:
----------
color_list (list[tuple]):
    List of RGB color tuples used for dot coloring

tim (Turtle):
    Turtle object used for drawing

Notes:
------
- Uses turtle.dot(size, color) for clean circular dots
- turtle.colormode(255) is required for RGB tuples
- Turtle is hidden and set to fastest speed for performance
- Grid spacing is controlled by forward(50) and line positioning logic

Optional:
---------
- Colors can be dynamically extracted from an image using colorgram
"""


import turtle
from turtle import Turtle, Screen
import random
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(199, 175, 118), (125, 36, 24), (187, 158, 50), (170, 105, 56),
               (5, 57, 83), (222, 223, 226), (200, 216, 205), (108, 67, 85), (39, 36, 35), (86, 142, 58), (20, 123, 176),
               (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186),
               (210, 200, 113), (179, 175, 177), (151, 176, 164), (93, 142, 156), (28, 80, 59), (194, 190, 192), (17, 78, 98),
               (213, 184, 173), (145, 116, 121), (176, 197, 202)]


tim = Turtle()
turtle.colormode(255)
tim.teleport(-250,-200)
tim.hideturtle()
tim.speed("fastest")

def draw_dot(line_number):
    for i in range(1, 11):
        color = random.choice(color_list)
        tim.dot(25,color)
        tim.up()
        tim.forward(50)
    tim.setposition(-250, (50 * line_number) -200)

for j in range(1,11):
    draw_dot(j)

my_Screen = Screen()
my_Screen.exitonclick()
