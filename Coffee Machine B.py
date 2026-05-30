from art import logo, machine
from coffee_data import resources, MENU
from coffee_data import money

def report(finances):
    resources["money"] = finances
    for x , y in resources.items():
        if x == "money":
            print(f"{x}: ${y}")
        elif x == "coffee":
            print(f"{x}: {y}gm")
        else:
            print(f"{x}: {y}ml")

def money_management(order):
    user_money = 0
    print("Please insert coins 🪙:")
    for x in money.keys():
        count = float(input(f"How many {x}: "))
        user_money += count * money[x]
    if user_money > MENU[order]["cost"]:
        user_money - MENU[order]["cost"]
        remain = user_money
        return True, remain
    elif user_money == MENU[order]["cost"]:
        return True, user_money
    else:
        return False, user_money

def check_resources(ingredients, menu, order):
    for k, v in menu[order]["ingredients"].items():
        if ingredients[k] < menu[order]["ingredients"][k]:
            return False
    return True

def inventory_management(ingredients, menu, order):
    for k, v in menu[order]["ingredients"].items():
        ingredients[k] -= menu[order]["ingredients"][k]
    return ingredients

print(logo)
print(machine)
bank = 0
coffee_machine = True
while coffee_machine:

    user_order = input("What would you like today?\n‣ Espresso ☕\n‣ Latte 🧋\n‣ Cappuccino 🍵\n"
                       "¤ Please choose from Menu: ").lower()
    if user_order == "off":
        print("Power Off...")
        coffee_machine = False
    elif user_order in MENU:
        if check_resources(resources, MENU, user_order) == False:
            print(f"Sorry we ran out of {user_order}.")
        else:
            status, refund = money_management(user_order)
            if status == True and refund == MENU[user_order]["cost"]:
                bank += refund
                print(f"Here is your {user_order}, Enjoy!")
                resources = inventory_management(resources, MENU, user_order)
            elif status == True:
                bank += MENU[user_order]["cost"]
                print(f"Here is change: ${refund}")
                print(f"Here is your {user_order}, Enjoy!")
                resources = inventory_management(resources, MENU, user_order)
            else:
                print(f"Sorry that's not enough money. ${refund} refunded.")
    elif user_order == "report":
        report(bank)
    else:
        print("Wrong input, Retry")