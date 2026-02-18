import random

print("welcome to number guessing game... u would get 3 chance to guess the number ...\n please enter the lower and upper bound range for guessing range")

low= int(input("enter the low bound:"))
high= int(input("enter the higher bound:"))

num=random.randint(low,high)
ch=3
gc=0

while gc<ch:
    gc+=1
    guess=int(input("guess the number :"))

    if guess == num:
        print(f"correct! u guessed it in {gc} attempts")
        break
    elif gc>=ch and guess != num:
        print(f"sorry the number was {num} try next time....")
    elif guess > num:
        print("too high guess again...")
    elif guess < num:
        print("too low, guess again...")
    