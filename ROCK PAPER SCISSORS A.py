import random
rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("\t\t\t\t**** ROCK  PAPER  SCISSORS ****")

#DEFINEING VARIABLES
user = int(input("PLEASE CHOOSE: Type 0 For ROCK, Type 1 For PAPER, Type 2 For SCISSORS\n"))
rps = [rock, paper, scissors]
computer = random.randint(0,2)

#USER CHOICE
print(f"You Choose: {rps[user]}")

#COMPUTER CHOICE
print(f"Computer Choose: {rps[computer]}")

#LOGIC
if user == computer:
    print("DRAW!")
elif ((user == 0 and computer == 2) or
      (user == 2 and computer == 1) or
      (user == 1 and computer == 0)):
    print("You WIN!")
else:
    print("You LOSE!")