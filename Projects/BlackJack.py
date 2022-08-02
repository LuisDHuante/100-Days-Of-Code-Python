"""BlackJack"""

import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    cards = (11, 2, 3, 4, 5, 6, 7 ,8, 9, 10,10,10,10)    
    card = random.choice(cards)
    return card


def calculate_score(deck):
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    return sum(deck)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, your opponent has Blackjack\n"
    elif user_score == 0:
        return "You win! You have a Blackjack! :)\n"
    elif user_score > 21:
        return "You went over 21 points, you lose :(\n"
    elif computer_score > 21:
        return "Opponent went over 21 points, you win! :)\n"
    elif user_score > computer_score:
        return "You win! :)\n"
    else:
        return "You lose :( \n"


def blackjack():

#We define 2 lists belonging to the computer and the player

    user_cards = []
    computer_cards = []

#We deal 2 cards to the player and the computer

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

#We then assign two variables with the scores of both the user and the computer

    print(logo)
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, your current score: {user_score}")


#While game is not over, we ask the player if he wants to draw another
#card, and display both their score and the computer's

    game_over = False

    while game_over == False:
        option = input("Do you want to draw another card? (Y/N): ").upper()
        os.system('cls')

        if option == 'Y':
            print(logo)
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, your current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}\n")
            if user_score or  computer_score == 0 or user_score > 21:
                game_over = True

        elif option == 'N':
            break
        else:
            input('You must enter a valid option. Press any key to return:  ')
            os.system('cls')


#When this condition is satisfied, the final score of both players is printed onscreen
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final score: {user_score}, your final hand: {user_cards}")
    print(f"Your opponent's score: {computer_score}, your opponent's hand: {computer_cards}\n")
    print(compare(user_score, computer_score))
    input("Press any key to return to menu: ")
    os.system ("cls")

#Game is finished afterwards
    game_over = True
    

if __name__ == '__main__':
    while True:
        print(logo)
        new_game = input('Press Y to start a new game or any key to exit: ').upper()
        os.system ("cls")
        if new_game == 'Y':
            os.system ("cls")
            blackjack()
        else:
            break