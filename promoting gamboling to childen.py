import random
lotto = []
bets = []

while len(lotto) < 5:
    lotto.append(random.randint(1,100))
    lotto = list(set(lotto))


for i in range(5):
    guess = int(input("Guess the nubmer mate: "))
    bets.append(guess)


wins = 0

for num in bets:
    if num in lotto:
        wins += 1

if wins == 0:
    print("You win nothing mate.")
elif wins == 1:
    print ("You win $10 mate, you got lucky.")
elif wins == 2:
    print("You win $100 dollars mate, you got extremly lucky.")
elif winsm== 3:
    print("You won $1,000 dollars, how lucky can you be mate?")
elif wins == 4:
    print("Y-You won $10,000 dollors, ARE YOU CHEATING MATE, HOW LUCKY CAN YOU GET?!")
else:
    print("Y-You w-won $100,000 dollors, what are you who are you? The luck machine or something mate?")


print(lotto)
