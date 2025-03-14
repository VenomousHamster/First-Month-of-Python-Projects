from lief import type_error
from Coffee_Menu import menu, resources


change = {"pennies": 0.01, "nickels": 0.05, "dimes": 0.10, "quarters": 0.25}

def resource_check(selection):
    """ checks to see if there are enough resources, and returns the drink if there is. And returns the low resource if it can't """
# Probably could simplify code by adding milk to espresso as zero. But I wanted to try it without adding it, but other than that, this is the best I can do.
    water_level = resources["water"]
    coffee_level = resources["coffee"]
    milk_level = resources["milk"]

    if selection in menu and len(menu[selection]["ingredients"]) > 2:
        water_needed = menu[selection]["ingredients"]["water"]
        coffee_needed = menu[selection]["ingredients"]["coffee"]
        milk_needed = menu[selection]["ingredients"]["milk"]
        if water_needed > water_level:
            return "Need water."
        elif coffee_needed > coffee_level:
            return "Need more coffee."
        elif milk_needed > milk_level:
            return "Need more milk."
        else:
             return selection
    elif selection in menu and len(menu[selection]["ingredients"]) == 2:
        water_needed = menu[selection]["ingredients"]["water"]
        coffee_needed = menu[selection]["ingredients"]["coffee"]
        if water_needed > water_level:
            return "Need water."
        elif coffee_needed > coffee_level:
            return "Need more coffee."
        else:
            return selection
    elif selection == "report":
        return "report"
    elif selection == "off":
        return "off"
    else:
        return "Invalid choice."

def cash_check(order):
    user_money = 0
    price = menu[order]["cost"]
    for coins in change:
      try:
        user_money += change[coins]*int(input(f"How many {coins} do you want to use?\n"))
      except type_error:
        print("You have to enter a number.")
      user_money = round(user_money, 1)
      print(user_money)
    if user_money == price:
         return price
    elif user_money > price:
         user_money -= price
         user_money = round(user_money, 2)
         print(f"Your change is: {user_money}¢")
         return price
    else:
        print(f"Not enough money. Here is your: {user_money}¢ back.")
        return 0

def use_resources(coffee):

    if len(menu[coffee]["ingredients"]) > 2:
        water_used = menu[coffee]["ingredients"]["water"]
        coffee_used = menu[coffee]["ingredients"]["coffee"]
        milk_used = menu[coffee]["ingredients"]["milk"]
        resources["water"] -=  water_used
        resources["coffee"] -= coffee_used
        resources["milk"] -= milk_used
    else:
        water_used = menu[coffee]["ingredients"]["water"]
        coffee_used = menu[coffee]["ingredients"]["coffee"]
        resources["water"] -= water_used
        resources["coffee"] -= coffee_used

    print(f"Here is your {coffee}☕ Have a nice day😄")

def options(choice):

    if choice in menu:
        total_money = cash_check(choice)
        if total_money > 0:
            use_resources(choice)
            return total_money
        else:
            return 0
    elif choice == "report":
        for status in resources:
            print(f"Here is the amount left of {status}: {resources[status]}")
        print(f"Current money in machine: ${money_earned}")
        return 0
    else:
       print(choice)
       return 0

machine_on = True
money_earned = 0

while machine_on:
    user_choice = input("What would you like? (espresso / latte / cappuccino):\n").lower()
    if user_choice == 'off':
        machine_on = False
    else:
      can_make_coffee = resource_check(user_choice)
      money_earned += options(can_make_coffee)





