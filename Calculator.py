logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2

def divide(n1,n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

def subtract(n1,n2):
    return n1 - n2

symbols = {"+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,}

print(symbols["*"](4,8))
# Coding sucks
# def math (answer):


keeping_track = 0

def to_continue(user_choice1, num):
   last_total = num
   choice = user_choice1
   while choice == "y":
      print(logo)
      for key2 in symbols:
          print(key2)
      user_operation1 = input("Enter your operation.\n")
      user_num3 = float(input("Please enter number.\n"))
      new_total = symbols[user_operation1](last_total, user_num3)
      print(f"{last_total} {user_operation1} {user_num3} = {new_total}")
      choice = input("Type 'y' to continue with this total. Type 'n' to wipe and start over.\n")


never_ending = True

while never_ending:
    print(logo)
    user_num = float(input("Please enter first number.\n"))
    for key in symbols:
        print(key)
    user_operation = input("Enter your operation.\n")
    user_num2 = float(input("Please enter 2nd number.\n"))
    jar = 0
    if keeping_track == 2:
        never_ending = False
    if user_operation in symbols:
        jar = symbols[user_operation](user_num, user_num2)
        print(f"{user_num} {user_operation} {user_num2} = {jar}")
        user_choice = input("Type 'y' to continue with this total. Type 'n' to wipe and start over.\n").lower()
        keeping_track += 1
        to_continue(user_choice, jar)
