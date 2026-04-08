import art
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }
def calculator():
    print(art.logo)
    first_number = float(input("choose first number: "))
    prog = True
    while prog:
        for keys in operators:
            print(keys)
        function = input("Choose Function: ")
        second_number = float(input("choose second number: "))
        def calculate(n1, choice, n2):
            operation = operators[choice]
            calculation = float(operation(n1, n2))
            return f"{first_number} {choice} {second_number} = {calculation}", calculation
        full_result, result = calculate(first_number, function, second_number)
        print(full_result)
        option = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation"
                       f" or press any key to close the program: ").lower()

        if option == "y":
            first_number = result
        elif option == "n":
            prog = False
            print("\n" * 100)
            calculator()
        else:
            exit("\n\nTHANKS FOR USING CALCULATOR")
calculator()