from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(hand):
    score = sum(hand)

    # Blackjack
    if score == 21 and len(hand) == 2:
        return 0

    # Change Ace from 11 to 1 if score is over 21
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)

    return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"

    elif computer_score == 0:
        return "You lose! Computer has Blackjack."

    elif user_score == 0:
        return "You win with Blackjack!"

    elif user_score > 21:
        return "You went over 21. You lose!"

    elif computer_score > 21:
        return "Computer went over 21. You win!"

    elif user_score > computer_score:
        return "You win!"

    else:
        return "You lose!"


def play_game():

    user_hand = []
    computer_hand = []

    # Give 2 cards to each
    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    print(f"Your cards: {user_hand}, current score: {user_score}")
    print(f"Computer's first card: {computer_hand[0]}")

    # -------------------------
    # USER'S TURN
    # -------------------------

    while user_score != 0 and user_score < 21:

        choice = input("Do you want to draw another card? Type 'yes' or 'no': ")

        if choice == "yes":
            user_hand.append(deal_card())
            user_score = calculate_score(user_hand)

            print(f"Your cards: {user_hand}, current score: {user_score}")

        else:
            break

    # -------------------------
    # COMPUTER'S TURN
    # -------------------------

    if user_score <= 21:

        while computer_score != 0 and computer_score < 17:
            computer_hand.append(deal_card())
            computer_score = calculate_score(computer_hand)

    # -------------------------
    # FINAL RESULT
    # -------------------------

    print(f"\nYour final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

    print(compare(user_score, computer_score))


# Start the game
play_game()