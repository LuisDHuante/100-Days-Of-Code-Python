import random
import os

title = '''
                                                                        
            _                                     _                     
___ ___ ___| |_    ___ ___ ___ ___ ___    ___ ___|_|___ ___ ___ ___ ___ 
|  _| . |  _| '_|  | . | .'| . | -_|  _|  |_ -|  _| |_ -|_ -| . |  _|_ -|
|_| |___|___|_,_|  |  _|__,|  _|___|_|    |___|___|_|___|___|___|_| |___|
                |_|     |_|                                           

'''
victory = """                                        
 _   _  ___  _   _  __      _____  _ __  
| | | |/ _ \| | | | \ \ /\ / / _ \| '_ \ 
| |_| | (_) | |_| |  \ V  V / (_) | | | |
 \__, |\___/ \__,_|   \_/\_/ \___/|_| |_|
  __/ |                                  
 |___/        \n"""


defeat = """

     __                __   __  ___ 
\ / /  \ |  |    |    /  \ /__`  |  
 |  \__/ \__/    |___ \__/ .__/  |  \n
"""

def rock_paper_scissors():

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

    def game():
        player_points = 0
        computer_points = 0
        while True:
            while player_points or computer_points != 3:
                user_choice_flag = True
                user_choice = input("\nType 0 for Rock, 1 for Paper or 2 for Scissors: ")
                os.system("cls")
                if user_choice_flag != user_choice.isnumeric():
                    print("You must enter a valid option! ")
                    continue
                user_choice = int(user_choice)
                if user_choice >= 3 or user_choice < 0:
                    print("You must enter a valid number!: ") 
                    continue
                else:
                    print('You chose: ')
                    print(game_images[user_choice])
                    computer_choice = random.randint(0, 2)
                    print("Computer chose: ")
                    print(game_images[computer_choice])

                    if user_choice == 0 and computer_choice == 2:
                        print("You win this round!\n")
                        player_points += 1
                        print(f'Total points:\nPlayer: {player_points}/3\nComputer: {computer_points}/3')

                    elif computer_choice == 0 and user_choice == 2:
                        print("You lose this round\n")
                        computer_points += 1
                        print(f'Total points: \n Player: {player_points}/3\n Computer: {computer_points}/3')


                    elif computer_choice > user_choice:
                        print("You lose this round\n")
                        computer_points += 1
                        print(f'Total points: \n Player: {player_points}/3\n Computer: {computer_points}/3')

                    elif user_choice > computer_choice:
                        print("You win this round!\n")
                        player_points += 1
                        print(f'Total points: \n Player: {player_points}/3\n Computer: {computer_points}/3')

                    elif computer_choice == user_choice:
                        print("It's a draw\n")
                        print(f'Total points: \n Player: {player_points}/3\n Computer: {computer_points}/3')
                        
                    if player_points == 3: 
                        os.system("cls")
                        print(victory)
                        input("Press any key to return to menu: ")
                        break
                    elif computer_points == 3:
                        os.system("cls")
                        print(defeat)
                        print('The computer won the game :( \n')
                        input("Press any key to return to menu: ")
                        break
            break
                    
                    

    os.system ("cls")
    print(title)
    game()
   




if __name__ == '__main__':
    while True:
        os.system("cls")
        print(title)
        new_game = input('Press Y to start a new game or any key to exit: ').upper()
        if new_game == 'Y':
            os.system ("cls")
            rock_paper_scissors()
        else:
            break

