import random
print("Enter to the Dice Stimulator")
x="S"

while x == "S":
    number = random.choice([1,2,3,4,5,6])

    if number == 1:
        print("-----------")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("-----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if number == 3:
        print("-----------")
        print("|    O    |")
        print("|    O    |")
        print("|    O    |")
        print("-----------")
    if number == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if number == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
    if number == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
    x = input("Press S to roll again ")
    
