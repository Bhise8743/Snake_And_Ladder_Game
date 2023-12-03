"""

@Author: Omkar Bhise

@Date: 2023-12-02 05:00:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-03 11:30:00

@Title :  Snake and ladder game

"""
import random




def die():  # UC2
    """
        Description:
            it returns the random number between one and six
        Parameter:
            None

        Return: int value
    """
    return random.randint(1, 6)


def check_for_the_option(counter):  # UC3
    """
        Description:
            The player then check for an Option if player then check the ladder or snake

        Parameter: None

        Return: None

    """

    check_option = random.randint(0, 2)
    if check_option == 0:  # ladder
        counter += die()
    elif check_option == 1:  # snake
        counter -= die()
    else:  # no play
        print("No Play")
    return counter


def main():
    """
        Description:
            in this function we call the other functions

        Parameter: None

        Return: None

    """
    player_pos = 0
    print(f"Snake and Ladder game played with single player at start position 0 and it percent at {player_pos} ")

    player_pos = check_for_the_option(player_pos)
    if player_pos < 0:
        player_pos = 0
    print(player_pos)


if __name__ == '__main__':  # UC1
    main()