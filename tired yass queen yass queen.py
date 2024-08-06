import random

number = random.randint(1, 100)
guess = int(input("Please guess a number from 1 too 100: "))
count = 1

for i in range(5):
    count += 1
    if number > guess:
        print("Too low mate.")
    elif number < guess:
            print("Too high mate.")
    else:
        break
    guess = int(input("Please try again: "))

if number == guess:
    print("You guessed the number mate.")
else:
    print("Better luck next time mate, the number was "+str(number))

print("You guessed " +str(count)+" times.")
