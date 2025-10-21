import art # IMPORTING LOGO ART

print(art.logo) # PRINTING LOGO ART
data = {}   # DECLARING VARIABLES
new_user = True
while new_user:
    name = input("What is your name: ")  # USER INPUT
    bid = int(input("What is your bid: $ "))
    data[name] = bid
    option = input("Are there any other bidders? Type 'yes' or 'no': ").lower() # FOR OTHER USERS

    if option == "yes":
        print("\n"*100) # FOR PLACING GAP BETWEEN THE INPUT OF USERS
    else:
        new_user = False
        print(f"The winner is {max(data, key=data.get).title()} with a bid of ${data[max(data, key=data.get)]}") # PRINTING RESULTS