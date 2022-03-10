import random

def compChoice():
    randomNumber=random.randint(1,3)
    if randomNumber==1:
        return 'R'
    elif randomNumber==2:
        return 'P'
    elif randomNumber==3:
        return 'S'

comp=compChoice()
win=False

def game(comp,user):
    if comp=='R':
        if user=='R':
            win=None
        elif user=='P':
            win=True
        else:
            win=False
    elif comp=='P':
        if user=='R':
            win=False
        elif user=='P':
            win=None
        else:
            win=True
    else:
        if user=='R':
            win=True
        elif user=='P':
            win=False
        else:
            win=None
    return win

print("Enter your choice (only initial)-")
print("Rock(R)\nPaper(P)\nScissor(S)")
user=input()
result=game(comp,user)

print(f"You chose {user}")
print(f"Computer chose {comp}")
if result==True:
    print("Congratulations, you won!")
elif result==False:
    print("You lost, better luck next time!")
else:
    print("It's a draw!")