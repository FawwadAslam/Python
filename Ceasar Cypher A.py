alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(text_input, shift_number, choice):
    def encrypt(original_text, shift_amount):
        encryption = ""
        for letter in original_text:
            shifted = (alphabet.index(letter) + shift_amount) % 26
            encryption += alphabet[shifted]
        print(f"Here is the encoded result: {encryption}")

    def decrypt(original_text, shift_amount):
        decryption = ""
        for letter in original_text:
            shifted = (alphabet.index(letter) - shift_amount) % 26
            decryption += alphabet[shifted]
        print(f"Here is the decoded result: {decryption}")

    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift)
    else:
        exit("WRONG CHOICE")

ceaser(text_input=text, shift_number=shift, choice=direction)

