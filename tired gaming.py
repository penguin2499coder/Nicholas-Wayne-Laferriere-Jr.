import random

number = random.randint(1, 100)
guess = int(input("Please guess a number from 1 to 100,: "))

while number != guess:
    count += 1
    if number > guess:
        print("Too low mate.")
    else:
        print("Too high mate.")
    guess = int(input("Please try again."))

print("You got it in "+ str(count) +" times.")
print("Congrats, Now LEAVE GET OUT OF MY SIGHT!")
