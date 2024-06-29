import random

randomnumber=random.randint(1,100)

Player1=None
Player2=0
while(Player1!=randomnumber):
    Player1=int(input("Enter your guess: "))
    Player2+= 1
    if(Player1==randomnumber):
        print('You guessed the Right')
    else:
        if(Player1 > randomnumber):
            print("Your guess is wrong ! Enter a smaller Number")  
        else:
            print("Your guess is wrong ! Enter a Greater Number")      

print(f"You guessed the number in {Player2} guesses")  
        
with open("highscore")  as f:
    high=int(f.read())
if(high > Player2):
    print("You just broken the record")
    with open("highscore","w") as f:
        f.write(str(Player2))
    
            
    
    
