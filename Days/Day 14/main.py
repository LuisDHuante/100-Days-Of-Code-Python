from game_data import data
from art import logo, vs
import random
import os


def check_answer(guess, followers_a, followers_b):
    if guess == "A" and followers_a > followers_b:
        return True
    elif guess == "B" and followers_b > followers_a:
        return True
    else:
        return False


def random_choice():
    return random.choice(data)


def data_from_choice(choice):
    name = choice["name"]
    description = choice["description"]
    country = choice["country"]

    return f"{name}, a {description} from {country}"


def game():

    print(logo)
    score = 0
    a = random_choice()
    b = random_choice()

    game_is_on = True
    while game_is_on:
        print(f"Compare A: {data_from_choice(a)}:")
        print(vs)
        print(f"Against B: {data_from_choice(b)}")
        guess = input("Who has more followers? Type 'A' or 'B':  ").upper()
        os.system("cls")
        print(logo)
        if check_answer(guess, a["follower_count"], b["follower_count"]) == True:
            score += 1
            print(f"You're right! Current score: {score}")
            a = b
            b = random_choice()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_is_on = False


game()
