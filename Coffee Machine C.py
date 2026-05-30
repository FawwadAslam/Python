from art import logo, machine
from coffee_data import resources, MENU
from coffee_data import money

def report(finances):
    """Displays reamining resources and money in account."""
    resources["money"] = finances
    for x , y in resources.items():
        if x == "money":
            print(f"{x}: ${y}")
        elif x == "coffee":
            print(f"{x}: {y}gm")
        else:
            print(f"{x}: {y}ml")

def money_management(order, menu_cost):
    """Accumulates user's money, Sums it and then checks if user's money
    is sufficient to purcase coffee or not (Less than , Equal, or More than required)"""
    user_money = 0
    print("Please insert coins 🪙:")
    for x in money.keys():
        count = float(input(f"How many {x}: "))
        user_money += count * money[x]
    if user_money > menu_cost[order]["cost"]:
        user_money -= menu_cost[order]["cost"]
        return True, user_money
    elif user_money == menu_cost[order]["cost"]:
        return True, user_money
    else:
        return False, user_money

def check_resources(ingredients, menu, order):
    """Checks if sufficient ingredients are available, to make coffee as per order. """
    for k, v in menu[order]["ingredients"].items():
        if ingredients[k] < menu[order]["ingredients"][k]:
            return False, k
    return True, k

def inventory_management(ingredients, menu, order):
    """Subtracts the indresients from resources used to make ordered coffee"""
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
    if user_order == "off": # Power off coffee machine.
        print("🅾️ Power Off...")
        coffee_machine = False

    elif user_order in MENU: # Main logic of coffee machine code.
        stat, low_ingredient = check_resources(resources, MENU, user_order)
        if  stat == False:
            print(f"Sorry we ran out of {low_ingredient}.")
        else:
            status, payment = money_management(user_order, MENU)
            if status == True and payment == MENU[user_order]["cost"]:
                bank += payment
                print(f"Here is your {user_order}, Enjoy!")
                resources = inventory_management(resources, MENU, user_order)
            elif status == True:
                bank += MENU[user_order]["cost"]
                print(f"\n    🪙 Take your change: ${payment:.2f} 🪙")
                print(f"==>> Here is your ☕︎ {user_order}, Enjoy! <==\n")
                resources = inventory_management(resources, MENU, user_order)
            else:
                print(f"Sorry that's not enough money. ${payment} refunded.")

    elif user_order == "report": # Prints stock status of coffee machine.
        print("📋STOCK STATUS📋\n----------------")
        report(bank)
        print("--------------")
        
    else: # To capture any wrong user input
        print("⚠️ Wrong input, Retry ⚠️\n")