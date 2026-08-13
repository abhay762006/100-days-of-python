from art import logo
print(logo)
import random
computer = random.randint(1, 100)
print("Welcome to the Guessing Game!")

def game():
    level = input("Enter the level: Easy or Hard ")
    if level == "easy":
        attempts = 10
        print("You have 10 attempts")
    else:
        attempts = 5
        print("You have 5 attempts")
    guess = int(input("Guess the number between 1 to 100 "))
    while attempts > 0:
        if guess == computer:
            print("You guessed the right number")
            break
        elif guess < computer:
            print("You guessed too low")

        else:
            print("You guessed too high")

        attempts -= 1
        guess = int(input("Guess the number again"))
    if attempts <= 0:
        print(f"You failed the number was {computer}")

game()

