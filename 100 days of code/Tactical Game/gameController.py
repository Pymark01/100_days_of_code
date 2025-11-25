from turtle import Screen


class GameController:
    def __init__(self, screen):
        self.screen = screen

    def disable_movement(self):
        self.screen.onkey(None, "Up")
        self.screen.onkey(None, "Down")
        self.screen.onkey(None, "Left")
        self.screen.onkey(None, "Right")
