import random

print("Welcome to the number guessing game. You have to guess the number that the computer has thought of.\nThe number will be between 1 and 100.")
difficulty = input("Enter 'Easy' for 10 tries and 'hard' for 5 tries. ").lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
number = random.randint(1, 100)

while attempts > 0:
    guess = int(input(f"You have {attempts} attempts left.\n Guess a number: "))
    if guess == number:
        print(f"You win! the number was {number}")
        attempts = -1
    elif guess > number:
        attempts -= 1
        print("Too high.")
    elif guess < number:
        attempts -= 1
        print("Too low.")
    

if attempts == 0:
    print("Game over! you ran out of tries.")