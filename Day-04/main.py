import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if user_choice < 0 or user_choice > 2:
    print("Invalid choice! You lose.")
else:
    computer_choice = random.randint(0, 2)

    print(f"\nYou chose: {choices[user_choice]}")
    print(game_images[user_choice])

    print(f"Computer chose: {choices[computer_choice]}")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a Draw!")

    elif user_choice == 0 and computer_choice == 2:
        print("You Win!")

    elif user_choice == 2 and computer_choice == 0:
        print("You Lose!")

    elif user_choice > computer_choice:
        print("You Win!")

    else:
        print("You Lose!")