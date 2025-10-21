# Have a player character with certain stats
# different kind of monsters
# different kind of weapons
# A battle system based on the roll of different dice
# A map which can be shown
# several rooms

# monsters are randomly generated
# how to keep track of stats?
# Create a character sheet
# Create a function that can roll a die
# Create a function that can add results of a die to stats of character sheet


player1 = {
    "str": 8,
    "dex": 12,
    "con": 10,
    "int": 8,
    "cha": 18,
    "wis": 7
}

intelligence = int(player1["int"])
print(intelligence)

actions = ["kick, walk"]



def bad_stuff():
    print("")

def kick():
    print("something else")

def shelter():
    print("something")

def intro():
    directions = ["stay","left","right","forward"]
    print("You're standing in front of an old wooden door. It looks like a good 'kick' might open it. But perhaps it's better "
          "to stay quiet and find some 'shelter' next to the rocks.")
    userInput = ""
    while userInput not in directions:
        print("Options: shelter, kick")
        userInput = input()
        if userInput == "kick":
            kick()
        elif userInput == "shelter":
            shelter()
        #elif userInput == "right":
        #    go1()
        #elif userInput == "forward":
        #    go1()
        else:
            print("Try again.")

if __name__ == "__main__":
    while True:
        print(f"Welcome to Adventure!")
        name = input("Choose a name: ")
        #Make a list of weapons,
        weapon = input("Choose a weapon: (Sword/Axe) ")
        #print(", " +name+ ".")
        print("You have been plowing your way through the snow for the better part of the day. And not very long ago you heard"
              " the cry of the pack. It's very likely that they are tracking you... .")
        print("In the distance you can just make out a clearing with some large boulders, maybe they might offer some protection?")
        print("When you get closer to the rocks you can see a patch of shadows, a bit darker then it's surroundings."
              "'A place to hide or more worries...?' You wonder. You see an old moldy door, it looks like a good 'kick' might open it.")
        print("You look around weighing your options about finding a 'shelter' and getting a fire going or go through that door.")

        intro()

