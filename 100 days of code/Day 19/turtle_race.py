from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
tim = Turtle()
timmy = Turtle()
tom = Turtle()
#Turtles need a color
colors = ["red", "blue", "green"]

distance = [5, 10, 15, 20]
tim.color(colors[0])
tim.penup()
tim.goto(x=-230, y=0)
timmy.penup()
timmy.color(colors[1])
timmy.goto(x=-230, y=25)
tom.color(colors[2])
tom.penup()
tom.goto(x=-230, y=-25)

for x in range (500):
    tim.pendown()
    tim.forward(random.choice(distance))
    timmy.pendown()
    timmy.forward(random.choice(distance))
    tom.pendown()
    tom.forward(random.choice(distance))



screen.exitonclick()