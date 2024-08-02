'''anything=["Nah i'd win badge",25,False,5.53]

print(anything[1])
anything.append("random")
print(anything)

anything.remove(False)
print(anything)'''

import random

print("Welcome to the nuber war game")
myHand=[]
compHand=[]

score=0
Cscore=0

for i in range(10):
    myHand.append(random.randint(1,100))
    compHand.append(random.randint(1,100))

print("Here is you're hand: ")
print(myHand)
print("Here is the computers hand: ")
print(compHand)

myScore=0
compScore=0

while len(myHand)!=0 or len(compHand)!=0:
    print("Here is you're updated hand.")
    print(myHand)
    choice=int(input("What number would you like to play?"))
    while choice not in myHand:
        choice=int(input("What number would you like to play?"))
    myHand.remove(choice)
    compChoice=random.choice(compHand)
    compHand.remove(compChoice)
    print("The computer chose",compChoice)
    if choice>compChoice:
             print("You won this round.")
             score+=score
             myHand.append(choice)
             myHand.append(compChoice)
    elif choice<compChoice:
              print("You lost this round.")
              Cscore+=2
              compHand.append(choice)
              compHand.append(compChoice)
    else:
             print("Tie")
             compHand.append(compChoice)
             myHand.append(choice)
if len(myHand)>len(comHand):
     print("you won this war.")
else:
    print("Computer won this war.")
