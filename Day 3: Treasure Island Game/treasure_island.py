print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("You're at a cross road. Where do you want to go? Type 'left' or 'right'")
choice = input()
choice = choice.upper()

if choice == "RIGHT":
    print("You fell into quick sand and died...")
elif choice == "LEFT":
    print("It rained heavily the night before. A raging river lays before you. It looks deep... do you swim or wait?")
    swim_wait = input()
    swim_wait = swim_wait.upper()
    if swim_wait == "SWIM":
        print("You drowned. GAME OVER.")
    else:
        print("The river dies down by the next morning.")
        print("You successfully cross the river and continue to walk through the woods.")
        print("You come across a small cabin made of stones with three doors.")
        print("There's a red door, a blue door, and a yellow door.")
        print("Which door do you choose?")
        door = input()
        door = door.upper()
        if door == "RED":
            print("You open the door and a snake bites you.")
            print("YOU DIE. GAME OVER.")
        elif door == "BLUE":
            print("Stones above the door break free and crush your skull.")
            print("You lay on the ground and bleed out.")
            print("GAME OVER.")
        elif door == "YELLOW":
            print("A golden ray of light shines on your face.")
            print("For a moment your blinded, but then you see it.")
            print("A large wooden chest.")
            print("Congrats! You found the treasure!")
