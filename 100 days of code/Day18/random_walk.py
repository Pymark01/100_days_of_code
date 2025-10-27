import turtle
from turtle import Turtle, Screen
import random

directions = [0, 90, 180, 270]
tim = Turtle()
tim.pensize(10)

for _ in range(200):

    tim.forward(25)
    tim.setheading(random.choice(directions))


turtle.exitonclick()
