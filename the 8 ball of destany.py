print("I I'm the 8 ball of desaniy, what do you want to ask me?")
import random

choice = random.randint(1,4)
question = input("Ask a yes or no question. ")

if choice == 1:
    print("Yes.")
elif choice == 2:
    print("Don't cound on it.")
elif choice == 3:
    print("Can't predict now.")
elif choice == 4:
    print("Without a doubt.")
elif choice == 5:
    print("No just no.")
elif choice == 6:
    print("You're cancelled 4K dude bye!")
