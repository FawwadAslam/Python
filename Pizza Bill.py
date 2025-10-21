print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

pizza_value = 0
if size == "s":
    pizza_value += 15
    if pepperoni == "y":
        pizza_value += 2
    if extra_cheese == "y":
        pizza_value += 1
    print(f"Your final bill is ${pizza_value}")

elif size == "m":
    pizza_value += 20
    if pepperoni == "y":
        pizza_value += 3
    if extra_cheese == "y":
        pizza_value += 1
    print(f"Your final bill is: ${pizza_value}.")

elif size == "l":
    pizza_value += 25
    if pepperoni == "y":
        pizza_value += 3
    if extra_cheese == "y":
        pizza_value += 1
    print(f"Your final bill is: ${pizza_value}.")

else:
    print("Wrong entry")

