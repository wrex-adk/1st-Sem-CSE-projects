import random
print("Welcome to Guess the Number !")
print("I'm thinking of a number between 1 and 10.")
y= random.randint(1, 10)
a=0
while True:
    x=int(input("Enter your guess: "))
    a=a+1
    if x< y:
        print("Too Low! tRY AGAIN.")
    elif x>y :
        print("To high. Try again")
    else:
        print(f"CONGRATULATIONS! You gussed in {a} attempts.")
    


    