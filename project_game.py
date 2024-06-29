   
import random
    
def game(computer,Manasa):
    if computer==Manasa:
            return None
    elif computer=="s":
            if Manasa=='p':
              return False
            elif Manasa=='r':
                return True
    elif computer=="p":
            if Manasa=='r':
              return False
            elif Manasa=='s':
                return True
    elif computer=="r":
            if Manasa=='s':
              return False
            elif Manasa=='p':
                return True 
               
print("Computer turn!  Rock(r),Scissor(s) or paper(p)")    
randno=random.randint(1,3)
print(randno)
if randno==1:
    computer="r"
elif randno==2:
    computer="s"
elif randno==3:
    computer="p"  
    
Manasa=input("Your Turn! Rock(r) ,Scissor(s), or paper(p)")      
a=game(computer,Manasa)       
print(f"The computer choose  {computer}") 
print(f"You choose  {Manasa}")    

if a==None:
    print("game is Tie!")
elif a:
    print("you won the game")     
else:
    print('You lose the game')    


