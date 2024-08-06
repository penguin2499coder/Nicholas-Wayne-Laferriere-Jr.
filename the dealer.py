import random

score = 0
comp_score = 0

print("Let's play rock, paper, scissors! \n")

rounds = int(input("How many rounds would you like to play mate?"))

for i in range(rounds):
    player = int(input("Choose rock (1), paper (2), or scissors (3): "))

    comp = random.randint(1,3)
    if comp == 1:
        print("The computer chose rock mate.")
    elif comp == 2:
        print("The computer chose paper mate.")
    else:
        print("The computer chose scissors mate.")

    if player == comp:
        print("It's a tie mate, you havin't won yet.")

    if player == 1 and comp == 2:
        print("*chuckles* The computer won mate.")
        comp_score +=1

    if player == 1 and comp == 3:
        print("*sigh* You won this round mate, you got beginers luck in you're blood, I can tell.")
        score +=1

    if player == 2 and comp == 1:
        print("*sigh* You won this round you won't get lucky again, trust me.")
        score +=1

    if player == 2 and comp == 3:
        print("*chuckles* You lost, I get the point too bad for you mate I got good luck.")
        comp_score +=1

    if player == 3 and comp == 1:
        print("*chuckles* You lost, I have the most luck of playing this game in the world you know, so good luck winning again mate.")
        comp_score +=1

    if player == 3 and comp == 2:
        print("*sigh* You won you just get luck sometimes, trust me you won't get lucky again mate.")
        score +=1
