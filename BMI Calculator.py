height = float(input("What is your height in meter ? "))
weight = int(input("What is your weight in kgs ? "))
BMI = round(weight / (height ** 2), 2)
print(f"Your height is {height} cm\nYour weight is {weight} kgs\nYour BMI is {BMI}")
