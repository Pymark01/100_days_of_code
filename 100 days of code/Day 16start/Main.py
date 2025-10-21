

from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvasheight)
# my_screen.exitonclick()


table = PrettyTable()
table.add_column("test", ["testee","dsfdsf"])
table.add_column("type", [ "ddf", "dd"])
table.align = "l"


print(table)
