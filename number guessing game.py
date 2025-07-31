import random

num = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number (1 to 100): "))
    attempts += 1

    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
        break
