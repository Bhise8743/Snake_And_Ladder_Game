"""

@Author: Omkar Bhise

@Date: 2023-12-03 12:00:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-03 12:30:00

@Title :  Snake and ladder game

"""
import random


def die():
    """
        Description:
            it returns the random number between one and six
        Parameter: None

        Return: int value
    """
    return random.randint(1, 6)


def wining_position():
    """
        Description:
            it is the play the game and go to 100 position
        Parameter: None

        Return: None
    """
    player_pos = 0
    moves = 0
    while player_pos != 100:
        moves += 1
        dies = die()

        check_player = random.randint(0, 1)
        if check_player == 0:  # ladder
            if player_pos + dies > 100:
                continue
            else:
                player_pos += dies
        elif check_player == 1:  # snake
            player_pos -= dies
        else:
            continue
        if player_pos < 0:
            player_pos = 0
        # print(f"{player_pos} ", end="")

    print(f"\n{player_pos} Players wins after the {moves}")


if __name__ == '__main__':
    print(f"Snake and Ladder game played with single player at start position 0 ")
    wining_position()
