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
direction = input("You are at crossroads, where you wanna go 'Left' or 'Right' CHOOSE: ").lower()
if direction == "right":
    river = input("You have reached a river bank, There is an island in the middle, will you wait for 'Boat' or 'Swim' CHOOSE: ").lower()
    if river == "boat":
        island = input("You have reached the island, There is a castle with three doors, 'Red', 'Yellow', 'Black' CHOOSE: ").lower()
        if island == "red":
            print("CONGRATULATIONS! You have found the treasure")
        elif island == "yellow":
            print("Demon have eaten you, GAME OVER")
        elif island == "black":
            print("Spirits have eaten you, GAME OVER")
    elif river == "swim":
        print("You were eaten by crocodile")
elif direction == "left":
    print("You have fallen into a ditch")
else:
    print("WRONG ENTRY")

