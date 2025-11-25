from turtle import Turtle, Screen
from soldier import Soldier
from scoreboard import Scoreboard
from gameController import GameController
import time


def start_next_turn():
    # this handles turn transitions
    global next_turn
    next_turn = True


AP = 50
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Tactical game")
screen.tracer(0)


hicks = Soldier()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(hicks.forward, "Up")
screen.onkey(hicks.backwards, "Down")
screen.onkey(hicks.turn_left, "Left")
screen.onkey(hicks.turn_right, "Right")
screen.onkey(start_next_turn, "Return")  #Better to use return than enter

game_is_on = True
next_turn = False
waiting_for_next_turn = False

while game_is_on:
    screen.update()  # we have to call the screen.update() ourselves, and choose its location carefully
    time.sleep(0.1)
    #game logic goes here

    if hicks.action_used and AP > 0 and not waiting_for_next_turn: # This runs whether playing Or waiting for the next turn
        AP -= 1                                                    #added the waiting check
        scoreboard.update_display(AP)
        hicks.action_used = False       #Reset the flag

    if AP <= 0 and not waiting_for_next_turn:
        #Display "Press Enter" message
        print("End of turn - Press Enter to continue")
        waiting_for_next_turn = True # Now we're waiting

    if waiting_for_next_turn and next_turn: # Only reset if Enter was pressed
        AP = 50
        next_turn = False # Reset the flag
        waiting_for_next_turn = False # No longer waiting
        scoreboard.update_display(AP)
        #Udate Scoreboard
        print("New turn started! AP reset to 50")

screen.exitonclick()
