import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("\t\t\t\t**** ROCK  PAPER  SCISSORS ****")

#DEFINEING VARIABLES
user = str(input("PLEASE CHOOSE: Type 0 For ROCK, Type 1 For PAPER, Type 2 For SCISSORS\n"))
computer = str(random.randint(0,2))

#MAKING LIST
rps = [rock,paper, scissors]

#USER CHOICE
if user == "0":
    print(f"You Choose ROCK : {rock}")
elif user == "1":
    print(f"You Choose PAPER : {paper}")
elif user == "2":
    print(f"You Choose SCISSORS : {scissors}")
else:
    print("Wrong Input, You LOSE!")
    exit("FUCK OFF YOU IDIOT! YOU CAN ONLY CHOOSE 1, 2 & 3 ")

#COMPUTER CHOICE
print(f"Computer Choose: {rps[int(computer)]}")

#LOGIC
if user == computer:
    print("It is a DRAW!")
elif ((user == "0" and computer == "2") or
      (user == "2" and computer == "1") or
      (user == "1" and computer == "0")):
    print("You WIN!")
else:
    print("You LOSE!")