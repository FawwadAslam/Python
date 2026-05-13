import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

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
    player_points = sum(player)

    computer = random.choices(cards, k=2)
    computer_points = sum(computer)

    print(f"Your cards are: {player}, TOTAL POINTS: {player_points} ")
    print(f"Computer first card is: {computer[0]}, Second card is hidden.")

    game = True
    while game:
        if player_points == 21:
            print("You have BLACKJACK, YOU WON ")
            if computer_points == 21:
                print("Computer have BLACKJACK, YOU LOST ")

            ask = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
            if ask == "y":
                print("\n" * 20)
                blackjack()
            else:
                break
        if game:
            card_draw = input(f"Press H for HIT or Press S for STAND: ").lower()

            if card_draw == "h":
                player.extend(random.choices(cards, k=1))
                player_points = sum(player)
                print(f"Your cards are: {player}, TOTAL POINTS: {player_points} ")
                if player_points == 21:
                    print(f"YOU WON, Your cards are: {player}, TOTAL POINTS: {player_points}\n"
                          f"Computer's cards are: {computer}, TOTAL POINTS: {computer_points}")
                    game = False
                elif player_points > 21:
                    print(f"YOU LOST, Computer's cards are: {computer}, TOTAL POINTS: {computer_points}")
                    game = False

            elif card_draw == "s":
                computer.extend(random.choices(cards, k=1))
                computer_points = sum(computer)
                while computer_points < 17:
                    computer.extend(random.choices(cards, k=1))
                    computer_points = sum(computer)
                if computer_points > 21:
                    print(f"YOU WON, Your cards are: {player}, TOTAL POINTS: {player_points}\n"
                        f"Computer's cards are: {computer}, TOTAL POINTS: {computer_points}")
                    game = False
                elif computer_points > player_points  or computer_points == 21:
                    print(f"YOU LOST, Computer's cards are: {computer}, TOTAL POINTS: {computer_points}")
                    game = False

black = True
while black:
    option = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if option == "y":
        print("\n"*20)
        blackjack()
    else:
        break