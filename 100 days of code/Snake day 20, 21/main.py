from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=1000, height=1000)
screen.title("Snake!!!")
screen.bgcolor("black")
screen.tracer(0)

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

snake = []
for start_coordinates in START_POSITIONS:
    segments = Turtle()
    segments.shape("square")
    segments.color("white")
    segments.penup()
    segments.goto(start_coordinates)
    snake.append(segments)


moving = True

while moving:
    screen.update()
    time.sleep(0.1)
    for seg in snake:
        seg.forward(20)

    for


screen.exitonclick()