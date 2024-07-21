import random

def Games(computer,user):
    if computer==1:
        if user=="r":
            return None
        elif user=="p":
            return True
        else:
            return False
    elif computer==2:
        if user=="r":
            return False
        elif user=="p":
            return None
        else:
            return True
    else:
        if user=="r":
            return True
        elif user=="p":
            return False
        else:
            return None

Yscore=0
Cscore=0
condition="y"

while condition=="y":
    computer=random.randint(1,3)
    user=input("Your turn: Rock(r), Paper(p) or Scissor(s)? : ")
    x=Games(computer,user)
    if computer==1:
        print("Computer choose: Rock")
    elif computer==2:
        print("Computer choose: Paper")
    else:
        print("Computer choose: Scissor")

    if user=="r":
        print("You choose: Rock")
    elif user=="p":
        print("You choose: Paper")
    else:
        print("You choose: Scissor")

    if x:
        Yscore+=1
        print("You wins!")
    elif x==False:
        Cscore+=1
        print("You loses!")
    else:
        print("Game tie!")
    
    print(f"Total score: Computer score = {Cscore}, Your score = {Yscore}")
    
    condition=input("You want to play another round! Yes(y) or No(n): ")


