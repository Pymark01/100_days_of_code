from turtle import Turtle


class Soldier:
    def __init__(self):
        self.soldier = Turtle("square")
        self.soldier.color("white")
        self.soldier.penup()
        self.soldier.goto(0, 50)
        self.soldier.setheading(90)
        self.action_used = False  #Initialise the flag

    def forward(self):
        self.soldier.forward(10)
        self.action_used = True

    def backwards(self):
        self.soldier.backward(10)
        self.action_used = True

    def turn_left(self):
        self.soldier.rt(-15)
        self.action_used = True

    def turn_right(self):
        self.soldier.rt(15)
        self.action_used = True
