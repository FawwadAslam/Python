import random
zero = """
  +---+
  |   |
  O   |
 !|!  |
 ! !  |
      |
=========
"""
one ="""
  +---+
  |   |
  O   |
 !|!  |
 !    |
      |
=========
"""
two = """
  +---+
  |   |
  O   |
 !|!  |
      |
      |
=========
"""
three = """
  +---+
  |   |
  O   |
 !|   |
      |
      |
=========
"""
four = """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
"""
five = """
  +---+
  |   |
  O   |
      |
      |
      |
=========
"""
six = """
  +---+
  |   |
      |
      |
      |
      |
=========
"""

# LISTS FOR STAGES AND WORDS
stages = [zero,one,two,three,four,five,six]
word_list = ["aardvark", "baboon", "camel", "python", "brick", "funny", "witch"]

print(""" 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ | | _` | '_ | | _` | '_ ` _ | | _` | '_ | 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_||__,_|_| |_||__, |_| |_| |_||__,_|_| |_|
                    __| |                      
                   |____|                       """)

# CHOOSING RANDOM WORD
word = random.choice(word_list)

# DECLARING VARIABLES
dash = ["_" for x in range(len(word))]
life = 6
guess = ""
guessed = []

# LOGIC OF GAME
while "".join(dash) != word:

    # INPUT FOR USER
    print(f"Word to guess : {"".join(dash)}")
    guess = input(f"Guess a letter : ").lower() #USER INPUT
    guessed.append(guess)

    # LOGIC FOR ANY WRONG ENTRY, IDENTICAL ENTRY AND LIVES
    if len(guess) > 1:
        print("⚠️Choose only one letter!")
    elif guess not in word:
        life -= 1
        print(f"\t**** You guessed {guess}, That is not the word, You lose a life ****")
        print(f"\t***********************-{life}/6 LIVES LEFT-*********************** ")
    elif guess in dash:
        print(f"\t*** ⚠️You have already chosen the letter {guess.upper()} ***")

    # PRINTING IMAGES
    print(stages[life])

    # LIVES LOST
    if life == 0:
        print(f"*********************** WORD WAS: {word.upper()}, YOU LOSE! **********************")
        break

    # SAVING VALUE IN VARIABLE DASH
    for index in range(len(word)):
        if word[index] in guessed:
            dash[index] = word[index]

# IF USER GUESSED ALL WORDS
if "".join(dash) == word:
    print(f"Correct Guess : {"".join(dash).upper()}")
    print(f"\t************************-{life}/6 LIVES LEFT-************************")
    print(f"\t*-CONGRATULATIONS ! You have guessed the word {word.upper()}, YOU WON-*")