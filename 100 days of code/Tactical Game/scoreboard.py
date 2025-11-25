from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 200)

    def update_display(self, current_ap):
        self.clear()
        self.write(f"AP: {current_ap}", align="center", font=("courier", 16, "normal"))

