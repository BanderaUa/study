import random

tries = 0

number = random.randint(1,50)
print("try to guess number between 1-50")

while tries < 6 :
    guess = int(input())
    tries+= 1
    if guess < number:
        print("too low")
    elif guess > number:
        print("too big")
    else:
        print("Cheers!")

