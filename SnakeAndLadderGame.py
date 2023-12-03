"""

@Author: Omkar Bhise

@Date: 2023-12-02 05:00:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-01 5:30:00

@Title :  Snake and ladder game

"""
import random

player_pos = 0


def die():  # UC2
    """
        Description:
            it returns the random number between one and six
        Parameter:
            None

        Return: int value
    """
    return random.randint(1, 6)


if __name__ == '__main__':  # UC1
    print(f"Snake and Ladder game played with single player at start position {player_pos} ")
