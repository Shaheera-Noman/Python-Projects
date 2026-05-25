import random
from turtle import Turtle, Screen
import turtle as t

tim = t.Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGrey", "SeaGreen"]
num_of_sides = 5

def draw_shape(num_of_sides):
    angle = 360/num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()