"""

@Author: Omkar Bhise

@Date: 2023-12-04 11:45:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-04 03:30:00

@Title : Two players playing Snake and ladder game

"""

import random


def dice():
    """
        Description:
            this function returns the random number between one and six

        Parameter: None

        Return: int value
    """
    return random.randint(1,6)


def play():
    """
        Description:
            this function check the option of player No Player , Snake or Ladder and return the dice value
        Parameter: None

        Return: int value
    """
    die = dice()
    check_option = random.randint(0,2)
    if check_option == 0:  # Ladder
        return die
    elif check_option == 1:  # Snake
        return -die
    else:  # No Play
        return 0


def two_players():  # UC7
    """
        Description:
            this function is used find who is the winner of the game Player 1 or player 2

        Parameter: None

        Return: None
    """

    player_pos1 = 0  # Player Position one
    player_pos2 = 0  # Player Position Two
    option = 1

    while player_pos2 != 100 and player_pos1 != 100:

        match option:
            case 1:
                dice1 = play()  # player one
                if dice1 > 0:
                    if player_pos1 + dice1 > 100:
                        pass
                    else:
                        player_pos1 += dice1
                    option = 1
                    continue
                else:
                    player_pos1 += dice1
                    if player_pos1 < 0:
                        player_pos1 = 0
                    option = 2

            case 2:
                dice2 = play()  # player two
                if dice2 > 0:
                    if player_pos2 + dice2 > 100:
                        pass
                    else:
                        player_pos2 += dice2
                    option = 2
                else:
                    player_pos2 += dice2
                    if player_pos2 < 0:
                        player_pos2 = 0
                    option = 1

        print(f"{player_pos1}\t\t{player_pos2}")

    if player_pos1 == 100:
        print(f"Player Position {player_pos1} Player One is Winner ")
    else:
        print(f"Player Position {player_pos2} Player Two is Winner ")


if __name__ == '__main__':
    two_players()