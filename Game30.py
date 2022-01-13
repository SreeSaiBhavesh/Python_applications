import random


def user1(n):
    if(n!=0):
        print("Take no of chocolates between 1 and 6 both inclusive ")
        a = int(input())
        if a>=1 and a<=6:
            if(n>=a):
                n=n-a;
                print(n," chocolates are left")
                
            else:
                print("Only ",n," chocolates are left.")
                print("So select chocolates less than or equal to ",n)
            if n!=0:
                print("Now, user2 turn")
            user2(n)
            
                
        else:
            print("Enter a valid number between 1 to 6 both inclusive")
            user1(n)
    else:
        print("Congrats User2 has won the game")


def user2(n):
    if(n!=0):
        print("Take no of chocolates between 1 and 6 both inclusive ")
        b = int(input())
        if b>=1 and b<=6:
            if(n>=b):
                n=n-b;
                print(n," chocolates are left")
            else:
                print("Only ",n," chocolates are left.")
                print("So select chocolates less than or equal to ",n)
            if n!=0:
                print("Now, user1 turn")
            user1(n)
            
                
        else:
            print("Enter a valid number between 1 to 6 both inclusive")
            user2(n)
    else:
        print("Congrats User1 has won the game")
n=30
print("Toss to decide who starts the game")
toss = random.choice([0,1])
if toss==0:
    print("User1 start the game")
    user1(n)
else:
    print("User2 start the game")
    user2(n)
