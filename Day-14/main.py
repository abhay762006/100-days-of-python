from art import logo, vs
import game_data
import random

print(logo)


def game():
    count = 0

    while True:

        # Select two different people
        A, B = random.sample(game_data.data, 2)

        print("A")
        print(f"Name: {A['name']}")
        print(f"Description: {A['description']}")
        print(f"Country: {A['country']}")

        print(vs)

        print("B")
        print(f"Name: {B['name']}")
        print(f"Description: {B['description']}")
        print(f"Country: {B['country']}")

        user = input("Who has the highest Instagram followers? A or B: ").upper()

        # Check answer
        if user == "A":
            if A["follower_count"] > B["follower_count"]:
                count += 1
                print("You guessed correctly!")
                game()
            else:
                print("You guessed wrong!")

        elif user == "B":
            if B["follower_count"] > A["follower_count"]:
                count += 1
                print("You guessed correctly!")
                game()
            else:
                print("You guessed wrong!")

        else:
            print("Invalid choice!")

        retry = input("Would you like to try again? yes or no: ").lower()

        if retry != "yes":
            break

    print(f"You guessed {count} times correctly!")


game()