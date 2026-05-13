import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def ace_check(deck):
    total_aces = deck.count(11)
    total = sum(deck)
    while total > 21 and total_aces > 0:
        total -= 10
        total_aces -= 1
    return total

def blackjack_check(c, p):
    if p == 21 and c == 21:
        print(f"Both have BLACKJACK → GAME DRAW\nComputer Points: {c}\nYour Points: {p}")
    elif p == 21:
        print(f"You have BLACKJACK → YOU WON\nComputer Points: {c}\nYour Points: {p}")
    elif c == 21:
        print(f"Computer has BLACKJACK → YOU LOST\nComputer Points: {c}\nYour Points: {p}")


def blackjack():
    print(r"""
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
              |  \/ K|                            _/ |                
              '------'                           |__/
        """)

    player = random.choices(cards, k=2)
    player_points = ace_check(player)

    computer = random.choices(cards, k=2)
    computer_points = ace_check(computer)

    blackjack_check(computer_points, player_points)

    print(f"Your cards are: {player}, TOTAL POINTS: {player_points} ")
    print(f"Computer first card is: {computer[0]}, Second card is hidden.")

    game = True
    while game:

        card_draw = input(f"Press H for HIT or Press S for STAND: ").lower()

        if card_draw == "h":
            player.extend(random.choices(cards, k=1))
            player_points = ace_check(player)
            print(f"Your cards are: {player}, TOTAL POINTS: {player_points} ")
            if player_points == 21:
                print(f"\nYOU WON,\n\tYour cards are: {player}, TOTAL POINTS: {player_points}\n"
                        f"\tComputer's cards are: {computer}, TOTAL POINTS: {computer_points}")
                game = False
            elif player_points > 21:
                print(f"\nYOU LOST,\n\t Computer's cards are: {computer}, TOTAL POINTS: {computer_points}")
                game = False

        elif card_draw == "s":
            print(f"Computer's cards are: {computer}, TOTAL POINTS: {computer_points}")
            computer_points = ace_check(computer)
            while computer_points < 17:
                computer.extend(random.choices(cards, k=1))
                computer_points = ace_check(computer)
            if computer_points > 21:
                print(f"\nYOU WON,\n\tYour cards are: {player}, TOTAL POINTS: {player_points}\n"
                    f"\tComputer's cards are: {computer}, TOTAL POINTS: {computer_points}")
                game = False
            elif computer_points > player_points  or computer_points == 21:
                print(f"\nYOU LOST,\n\tComputer's cards are: {computer}, TOTAL POINTS: {computer_points}")
                game = False
            elif computer_points == player_points:
                print(f"\nGAME DRAW,\n\tYour cards: {player}, TOTAL POINTS: {player_points}\n"
                      f"\tComputer's cards: {computer}, TOTAL POINTS: {computer_points}")
                game = False

black = True
while black:
    option = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if option == "y":
        print("\n"*20)
        blackjack()
    else:
        break