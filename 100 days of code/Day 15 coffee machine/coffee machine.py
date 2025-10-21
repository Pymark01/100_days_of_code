MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1 Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
#     a. Check the user’s input to decide what to do next.
#     b. The prompt should show every time action has completed, e.g. once the drink is
#     dispensed. The prompt should show again to serve the next customer.




# TODO 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
#     a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
#     the machine. Your code should end execution when this happens.
# use a boolean to end the code

# TODO 3. Print report.
#     a. When the user enters “report” to the prompt, a report should be generated that shows
#     the current resource values. e.g.
#     Water: 100ml
#     Milk: 50ml
#     Coffee: 76g
#     Money: $2.5

#report = input(f"enter 'report' to check resources : ")

# TODO 4. Check resources sufficient?
#     a. When the user chooses a drink, the program should check if there are enough
#     resources to make that drink.
#     b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
#     not continue to make the drink but print: “ Sorry there is not enough water. ”
#     c. The same should happen if another resource is depleted, e.g. milk or coffee.
# Create a function that checks if there are enough resources
choice = input(f"What would you like? (espresso/ latte/ cappuccino): ")
drink = MENU[choice]
okay = True
def check(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            okay = False
        return okay

check(drink["ingredients"])

# TODO 5. Process coins.
#     a. If there are sufficient resources to make the drink selected, then the program should
#     prompt the user to insert coins.
#     b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#     c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#     pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
#create a function that processes the money

money = {
    "quarters" : 0.25,
    "dimes" : 0.10,
    "nickels" : 0.05,
    "pennies" : 0.01,
}


if okay:
    print(" Pls insert coins.")
    quarters_amount = int(input(f"How many quarters?"))*0.25
    money =+ quarters_amount
    dimes_amount = int(input(f"How many dimes?"))*0.10
    money =+ dimes_amount
    nickels_amount = int(input(f"How many nickles?"))*0.05
    money =+ nickels_amount
    pennies_amount = int(input(f"How many pennies?"))*0.01
    money =+ pennies_amount
    print(money)




# TODO 6. Check transaction successful?
#     a. Check that the user has inserted enough money to purchase the drink they selected.
#     E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#     program should say “ Sorry that's not enough money. Money refunded. ”.
#     b. But if the user has inserted enough money, then the cost of the drink gets added to the
#     machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#     Water: 100ml
#     Milk: 50ml
#     Coffee: 76g
#     Money: $2.5
#     c. If the user has inserted too much money, the machine should offer change.
#     E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
#     places.
# TODO 7. Make Coffee.
#     a. If the transaction is successful and there are enough resources to make the drink the
#     user selected, then the ingredients to make the drink should be deducted from the
#     coffee machine resources.
#     E.g. report before purchasing latte:
#     Water: 300ml
#     Milk: 200ml
#     Coffee: 100g
#     Money: $0
#     Report after purchasing latte:
#     Water: 100ml
#     Milk: 50ml
#     Coffee: 76g
#     Money: $2.5
#     b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
#     latte was their choice of drink.