from game_data import data
from art import logo
from art import vs
import random

def top_celeb(a, b):
    if a["follower_count"] > b["follower_count"]:
        return a
    else:
        return b

def celeb_randomize():
    a = random.choice(data)
    b = random.choice(data)
    while a == b:
        a = random.choice(data)
    else:
        return a, b

print(logo)

per_a, per_b = celeb_randomize()
celeb_a = per_a

points = 0
game = True
while game:

    per_a, per_b = celeb_randomize()
    celeb_b = per_b

    winner = top_celeb(celeb_a, celeb_b)
    print(f"COMPARE A: {celeb_a['name']}, {celeb_a['description']}, from {celeb_a['country']}")
    print(vs)
    print(f"COMPARE B: {celeb_b['name']}, {celeb_b['description']}, from {celeb_b['country']}")

    user_choice = input("Guess! which celebrity has more follower? Choose A or B: ").lower()
    if user_choice == "a" and celeb_a == winner:
        points += 1
        celeb_a = celeb_b
        print(logo)
        print(f"You're right! Current score: {points}")

    elif user_choice == "b" and celeb_b == winner:
        points += 1
        celeb_a = celeb_b
        print(logo)
        print(f"You're right! Current score: {points}")

    else:
        print(f"\n" * 20)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {points}")
        game = False