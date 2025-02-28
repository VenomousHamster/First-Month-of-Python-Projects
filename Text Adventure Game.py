from sympy import false

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
user_choice = input("You have wandered the island, and found some caves. Inside the caves, you can go left or right. Type your choice. ").lower()
flower = 0


if user_choice == "right":
    print("A giant mole burrows out of the ground and slices your stomach, and you bleed out.\n GAME OVER!")
if user_choice == "left":
    print("The tunnel is lit by dim lanterns. As you walk through the tunnel, the echo of your footsteps"
          "and the sound of dripping water is all that accompanies you. ")
    user_choice = input("You've made it to a fork of tunnels which path do you take? Left, mid, or right. Type your choice. ").lower()
    print(user_choice)
    if user_choice == "right":
        print("There is a stunning garden with mist settling over all the plants.\n A mesmerizing blue flower calls out to you. "
        "When you pick it, vines snatch into them slowly,\n stifling the air from your lungs until you die. GAME OVER!")
    if user_choice == "left":
        print("You see, a glowing yellow key. You start to approach it when a suit of armor comes to life, charging at you."
              "\n When it swings its sword, you too panicked to move, and the blade slices you open. "
              "You lay on the cold ground as you bleed out slowly, drifting off to death. GAME OVER! ")
    if user_choice == "mid":
      user_choice = input("You've to another two paths which do you take left or right. Type right or left. ").lower()
      if user_choice == "left":
        print("You make it to a dead end, but when you go to the turn around the floor is eating like quick sande until all the air has left your lungs. GAME OVER!")
      if user_choice == "right":
        print("You've made it to a door. You open a door inside the room, is glistening treasure spread throughout the room.\n YOU WIN!")