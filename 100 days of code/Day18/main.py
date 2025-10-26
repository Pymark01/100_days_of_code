import turtle
from turtle import Turtle, Screen

tim = Turtle()

for x in range(3, 11):
    for _ in range(x):
        for _ in range(5):
            tim.forward(10)
            tim.penup()
            tim.forward(10)
            tim.pendown()
        tim.left(360/x)

turtle.exitonclick()