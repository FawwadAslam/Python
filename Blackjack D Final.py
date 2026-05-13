import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def ace_check(deck): # ACE Check Function
    total_aces = deck.count(11)
    total = sum(deck)
    while total > 21 and total_aces > 0:
        total -= 10
        total_aces -= 1
    return total


def blackjack_check(c, p): # Blackjack Checking Function
    if p == 21 and c == 21:
        print(f"Both have BLACKJACK -> GAME DRAW 🙃\nComputer Points: {c}\n Your Points: {p}")
        return False
    elif p == 21:
        print(f"You have BLACKJACK -> YOU WON 😁\nComputer Points: {c}\nYour Points: {p}")
        return False
    elif c == 21:
        print(f"Computer has BLACKJACK -> YOU LOST 😭\nComputer Points: {c}\nYour Points: {p}")
        return False
    else:
        return True

def check_winner(c_score, c_cards, p_score, p_cards ):
    if p_score == 21:
        return (f"\nYOU WON 😁,\n\tYour cards are: {p_cards}, TOTAL POINTS: {p_score}\n"
                f"\tComputer's cards are: {c_cards}, TOTAL POINTS: {c_score}")
    elif p_score > 21:
        return (f"\nYOU LOST 😭,\n\t Computer's cards are: {c_cards}, TOTAL POINTS: {c_score}\n"
                f"\tYour cards are: {p_cards}, TOTAL POINTS: {p_score}")
    elif c_score > 21:
        return (f"\nYOU WON 😁,\n\tYour cards are: {p_cards}, TOTAL POINTS: {p_score}\n"
                f"\tComputer's cards are: {c_cards}, TOTAL POINTS: {c_score}")
    elif c_score > p_score or c_score == 21:
        return (f"\nYOU LOST 😭,\n\tComputer's cards are: {c_cards}, TOTAL POINTS: {c_score}\n"
                f"\tYour cards are: {p_cards}, TOTAL POINTS: {p_score}")
    elif p_score == c_score:
        return(f"\nGAME DRAW 🙃,\n\tYour cards: {p_cards}, TOTAL POINTS: {p_score}\n"
               f"\tComputer's cards: {c_cards}, TOTAL POINTS: {c_score}")
    else:
        return True


def blackjack(): # Game Function
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

    player = random.choices(cards, k=2) # Assigning Cards To Player
    player_points = ace_check(player) # Calculating Total Points

    computer = random.choices(cards, k=2) # Assigning Cards To Computer
    computer_points = ace_check(computer) # Calculating Total Points

    if not blackjack_check(computer_points, player_points): # Checking Blackjack
        return

    print(f"Your cards are: {player}, TOTAL POINTS: {player_points} ")
    print(f"Computer first card is: {computer[0]}, Second card is hidden.")

    # Main Game Logic
    game = True
    while game:

        card_draw = input(f"Press H for HIT or Press S for STAND: ").lower()

        if card_draw == "h":
            player.extend(random.choices(cards, k=1))
            player_points = ace_check(player)

        else:
            print(f"Computer's cards are: {computer}, TOTAL POINTS: {computer_points}")
            computer_points = ace_check(computer)
            while computer_points < 17:
                computer.extend(random.choices(cards, k=1))
                computer_points = ace_check(computer)


        final_result = check_winner(computer_points, computer, player_points, player)
        print(final_result)
        if "YOU WON" in final_result or "YOU LOST" in final_result or "GAME DRAW" in final_result:
            return

# Main Loop
black = True
while black:
    option = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if option == "y":
        print("\n"*20)
        blackjack()
    else:
        break