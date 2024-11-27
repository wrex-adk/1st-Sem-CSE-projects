import random
print("Welcome to Rock Paper Scissors game")
score=0
while True: 
    x=int(input("Enter one number Rock(1),Scissors(2) and Paper(3). If you want to quit press 4.: "))
    y=random.randint(1,3)
    if  x==1 and y==2 or \
        x==2 and y==3 or \
        x==3 and y==1:
        print("You win!")
        score+=1
    elif x==y:
        print("Its a tie")
    elif x==4:
        print(f"Your score is {score}")
    else:
        print("You lose")
