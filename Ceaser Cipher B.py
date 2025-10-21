import art
import string
print(art.logo)
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
            , 'w', 'x', 'y', 'z']
capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
             'W', 'X', 'Y', 'Z']
symbols = list(string.punctuation)
numbers = [str(n) for n in range(10)]
alphabet = capital + small + symbols + numbers

def caesar(original_text, shift_number, encode_decode):
    output = " "

    if encode_decode == "decode":
        shift_number *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_number) % len(alphabet)
            output += alphabet[shifted_position]
        else:
            output += letter
    print(f"Here is the {encode_decode}d result:{output}")

option = True
while option:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n-> ").lower()
    text = input("Type your message:\n-> ")
    shift = int(input("Type the shift number:\n-> "))
    caesar(text, shift, direction)
    choice = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n-> ").lower()
    if choice == "no":
        option = False
        print("THANK YOU FOR USING CAESAR CIPHER")