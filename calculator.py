from math import *

print("Select the type of calculator you want")
calculator=["Standard", "programmer","Trignometric"]
print("Enter 1 for standard calculator")
print("Enter 2 for programmer calculator")
print("Enter 3 for Trignometric calculator")
print()
q=input("Enter the number to activate calculator")

if q=="1":
    datatypes = ['integer','float']
    print(datatypes)
    y=input("Enter the datatype you want: ")  
    print("   .......................   ")
    print()
    tasks = ["1", "2","3","4","5","6","7","8","9","10"]
    print("Enter 1 for Addition")
    print("Enter 2 for Subtraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division")
    print("Enter 5 for squaring number")
    print("Enter 6 for squareroot")
    print("Enter 7 for logarithmic")
    print("Enter 8 for 1/x")
    print("Enter 9 for modulo operator")
    print("Enter 10 for factorial")
    print()
    print("   ..........   ")
    z = input("Enter the numbers for your task: ")
    
    if y==datatypes[0]:
        if z==tasks[0]:
            number1 = input("Enter the number1: ")
            number2 = input("Enter the number2: ")
            print(int(number1)+int(number2))
        if z==tasks[1]:
            number1 = input("Enter the number1: ")
            number2 = input("Enter the number2: ")
            print(int(number1)-int(number2))
        if z==tasks[2]:
            number1 = input("Enter the number1: ")
            number2 = input("Enter the number2: ")
            print(int(number1)*int(number2))
        if z==tasks[3]:
            number1 = input("Enter the number1: ")
            number2 = input("Enter the number2: ")
            print(int(number1)/int(number2))
        if z==tasks[4]:
            number=int(input("Enter the number: "))
            print(number*number)
        if z==tasks[5]:
            number = int(input("Enter the number: "))
            print(sqrt(number))
        if z==tasks[6]:
            number=int(input("Enter the number: "))
            print(log(number)/2.3)
        if z==tasks[7]:
            number=int(input("Enter the number: "))
            print(1/number)
        if z==tasks[8]:
            number1=int(input("Enter the Dividend: "))
            number2 = int(input("Enter the divisor: "))
            print(number1%number2)
        if z==task[9]:
            number=int(input("Enter the number to find factorial: "))
            print(factorial(number))
                                   
                
    elif y==datatypes[1]:
        if z==tasks[0]:
            number1 = input("Enter the number1: ")
            number2 = input("Enter the number2: ")
            print(float(number1)+float(number2))
        if z==tasks[1]:
            number1 = input("Enter the number1: ")
            number2 = input("Enter the number2: ")
            print(float(number1)-float(number2))
        if z==tasks[2]:
            number1 = input("Enter the number1: ")
            number2 = input("Enter the number2: ")
            print(float(number1)*float(number2))
        if z==tasks[3]:
            number1 = input("Enter the number1: ")
            number2 = input("Enter the number2: ")
            print(float(number1)/float(number2))
        if z==tasks[4]:
            number = float(input("Enter the number: "))
            print(number*number)
        if z==tasks[5]:
            number = float(input("Enter the number: "))
            print(sqrt(number))
        if z==tasks[6]:
            number=float(input("Enter the number: "))
            print(log(number)/2.3)
        if z==tasks[7]:
            number = float(input("Enter the number: "))
            print(1/number)
        if z==tasks[8]:
            number1=float(input("Enter the Dividend: "))
            number2 = float(input("Enter the divisor: "))
            print(number1%number2)
        if z==tasks[9]:
            print("Factorial of a number is applicable for only integer values")
            
    else:
        print("Invalid datatype, Please Try again")

elif q=="2":
    datatypes = ["binary","octal","hexadecimal"]
    print(datatypes)
    y=input("Enter the datatype you want: ")
    print("   .......................   ")
    print()
    tasks = ["1", "2","3","4","5","6","7"]
    print("Enter 1 for Addition, using decimal inputs")
    print("Enter 2 for Subtraction, using decimal inputs")
    print("Enter 3 for Multiplication, using decimal inputs")
    print("Enter 4 for Division, using decimal inputs")
    print("Enter 5 for decimal to binary")
    print("Enter 6 for decimal to octal")
    print("Enter 7 for decimal to hexadecimal")
    print()
    print("   ..........   ")
    w=input("Enter the number to perform the task")
      
    if y==datatypes[0]:
        if w==tasks[0]:
            number1 = input("Enter the Decimal number1: ")
            number2 = input("Enter the Decimal number2: ")
            print(bin(int(number1)+int(number2)))
        if w==tasks[1]:
            number1 = input("Enter the Decimal number1: ")
            number2 = input("Enter the Decimal number2: ")
            print(bin(int(number1)-int(number2)))
        if w==tasks[2]:
            number1 = input("Enter the Decimal number1: ")
            number2 = input("Enter the Decimal number2: ")
            print(bin(int(number1)*int(number2)))
        if w==tasks[3]:
            number1 = input("Enter the Decimal number1: ")
            number2 = input("Enter the Decimal number2: ")
            print(bin(int(number1)/int(number2)))
        if w==tasks[4]:
            number = int(input("Enter the decimal number to convert to binary: "))
            print(bin(number))
        if w==tasks[5]:
            print("Please select octal datatypes for this")
        if w==tasks[6]:
            print("Please select hexadecimal datatype for this")
            
    elif y==datatypes[1]:
        if w==tasks[0]:
            number1 = input("Enter the Decimal number1: ")
            number2 = input("Enter the Decimal number2: ")
            print(oct(int(number1)+int(number2)))
        if w==tasks[1]:
            number1 = input("Enter the Decimal number1: ")
            number2 = input("Enter the Decimal number2: ")
            print(oct(int(number1)-int(number2)))
        if w==tasks[2]:
            number1 = input("Enter the Decimal number1: ")
            number2 = input("Enter the Decimal number2: ")
            print(oct(int(number1)*int(number2)))
        if w==tasks[3]:
            number1 = input("Enter the Decimal number1: ")
            number2 = input("Enter the Decimal number2: ")
            print(oct(int(number1)/int(number2)))
        if w==tasks[5]:
            number = int(input("Enter the decimal number to convert to Octal: "))
        if w==tasks[4]:
            print("Please select binary datatypes for this")
        if w==tasks[6]:
            print("Please select hexadecimal datatype for this")
            print(oct(number))
            
    elif y==datatypes[2]:
        if w==tasks[0]:
            number1 = input("Enter the Decimal number1: ")
            number2 = input("Enter the Decimal number2: ")
            print(hex(int(number1)+int(number2)))
        if w==tasks[1]:
            number1 = input("Enter the Decimal number1: ")
            number2 = input("Enter the Decimal number2: ")
            print(hex(int(number1)-int(number2)))
        if w==tasks[2]:
            number1 = input("Enter the Decimal number1: ")
            number2 = input("Enter the Decimal number2: ")
            print(hex(int(number1)*int(number2)))
        if w==tasks[3]:
            number1 = input("Enter the Decimal number1: ")
            number2 = input("Enter the Decimal number2: ")
            print(hex(int(number1)/int(number2)))
        if w==tasks[6]:
            number = int(input("Enter the decimal number to convert to hexadecimal: "))
            print(hex(number))
        if w==tasks[5]:
            print("Please select octal datatypes for this")
        if w==tasks[4]:
            print("Please select binary datatype for this")
            
    else:
        print("Invalid datatype, Please try again")
        
if q=="3":
    trig_fns = ["sine","cosine","tangent","cotangent","secant","cosecant"]
    print(trig_fns)
    y=input("Enter the trignometric function you want: ")
    print("   .......................   ")
    print()
    operation = ["1", "2"]
    print("1 for normal function")
    print("2 for inverse trignometric functions")
    print()
    print("   ..........   ")
    w=input("Enter the number to perform the operation")
    if y==trig_fns[0]:
        if w==operation[0]:
            num = int(input("Enter the degrees: "))
            print(sin(radians(num)))
        if w==operation[1]:
            num = float(input("Enter the radian to know degree: "))
            print(degrees(asin(num)))
    elif y==trig_fns[1]:
        if w==operation[0]:
            num = int(input("Enter the degrees: "))
            print(cos(radians(num)))
        if w==operation[1]:
            num = float(input("Enter the radian to know degree: "))
            print(degrees(acos(num)))
    elif y==trig_fns[2]:
        if w==operation[0]:
            num = int(input("Enter the degrees: "))
            print(tan(radians(num)))
        if w==operation[1]:
            num = float(input("Enter the radian to know degree: "))
            print(degrees(atan(num)))
    elif y==trig_fns[3]:
        if w==operation[0]:
            num = int(input("Enter the degrees: "))
            print(1/tan(radians(num)))
        if w==operation[1]:
            num = float(input("Enter the radian to know degree: "))
            print(degrees(atan(1/num)))
    elif y==trig_fns[4]:
        if w==operation[0]:
            num = int(input("Enter the degrees: "))
            print(1/cos(radians(num)))
        if w==operation[1]:
            num = float(input("Enter the radian to know degree: "))
            print(degrees(acos(1/num)))
    elif y==trig_fns[5]:
        if w==operation[0]:
            num = int(input("Enter the degrees: "))
            print(1/sin(radians(num)))
        if w==operation[1]:
            num = float(input("Enter the radian to know degree: "))
            print(degrees(asin(1/num)))
                  
                      
else:
    print("Invalid input! Please Once check your input. Try again")
