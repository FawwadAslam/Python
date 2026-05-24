from game_data import data
from art import logo
from art import vs
import random

def top_celeb(a, b):
    """Takes two inputs from dictionary and outputs celebrity with more followers as winner."""
    if a["follower_count"] > b["follower_count"]:
        return a
    else:
        return b

def celeb_randomize():
    """This functions randomizes celebrities to avoids the comparison of the same celebrity"""
    a = random.choice(data)
    b = random.choice(data)
    while a == b:
        a = random.choice(data) # To avoid same celebrity being compared
    else:
        return a, b

def main_logic(user_inp, cel_a, cel_b, win, games):
    """Main logic of game, It takes User input, Randomized celebrities, Celebrity with more followers,
     Games boolean value & initial points. Returns Celebrity A, Current Boolean Value, Points Count and User's Choice
     for later use"""
    if user_inp == "a" and cel_a == win:
        cel_a = cel_b # The celebrity B will become celebrity A, to be compared with next random celebrity
        return cel_a, games, "a"
    elif user_inp == "b" and cel_b == win:
        cel_a = cel_b
        return cel_a, games, "b"
    else:
        games = False
        return cel_a, games, " "

print(logo)
def high_low():
    """HIGH & LOW Game"""
    celeb_a , per_b = celeb_randomize() # Randomize Celebrity
    # Value of celebrity for single use.

    points = 0
    game = True
    while game:

        per_a, per_b = celeb_randomize()
        celeb_b = per_b # Saving value of celebrity for constant random use inside loop

        winner = top_celeb(celeb_a, celeb_b) # Checking celebrity with more followers

        print(f"COMPARE A: {celeb_a['name']}, a {celeb_a['description']}, from {celeb_a['country']}")
        print(vs)
        print(f"COMPARE B: {celeb_b['name']}, a {celeb_b['description']}, from {celeb_b['country']}")

        user_choice = input("Guess! which celebrity has more follower? Choose A or B: ").lower()

        print(f"\n" * 20)
        print(logo)

        celeb_a, game, choice = main_logic(user_choice, celeb_a, celeb_b, winner, game) # Main logic

        if choice:
            points += 1
            print(f"You're right! Current score: {points}")
        else:
            print(f"Sorry, that's wrong. Final score: {points}")

high_low() # Main Function