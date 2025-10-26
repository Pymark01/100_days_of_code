from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(5)

def turn_right():
    tim.right(5)

def clear():
    tim.clear()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, key="c")

screen.exitonclick()