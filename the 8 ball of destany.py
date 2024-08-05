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
    print("My head says nien.")
