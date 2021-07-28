import random
print ("Number Guessing Game")

number=random.randint(1,9)


chances=0
print ("Guess a number between 1 to 9:")


while chances < 5 :

    guess=int(input("Enter your guess-"))

    if guess==number:
        print ("Congratulation you won ") 
        break

    elif guess<number:
        print ("Your number was too low")
        
    else:
        print ("Your number was too high")
    
    chances+=1

if not chances<5:
    print ("Your chances are over", number)
