# The Rock, Paper, Scissors Game by Eddy Ruhana
# I might later on improve it for printing the name of the winner

import random

class Players:
    """Class to represent a Player"""

    def __init__(self, name, hand):
        """Player constructor takes the Player's name and Player's hand"""

        self.PlayerName = name
        self.PlayerHand = hand


    def __str__(self):
        """String representation of a Player and his/her hand"""

        return "%s, your hand is a: %s" % (self.PlayerName, self.PlayerHand)


def main():
    Rock_Paper_Scissors = ['Rock', 'Paper', 'Scissors']

    # prompt Players to enter their names
    namePlayer1 = input("You are Player # 1, enter your name: ")
    namePlayer2 = input("You are Player # 2, enter your name: ")

    hand1 = random.choice(Rock_Paper_Scissors)
    hand2 = random.choice(Rock_Paper_Scissors)

    # Players 1 and 2 are created
    Player_1 = Players(namePlayer1, hand1)
    Player_2 = Players(namePlayer2, hand2)

    # Time to play
    print("")
    print(Player_1)
    print(Player_2)

    print("")
    if Player_1.PlayerHand == Player_2.PlayerHand:
        print("This is a draw, try again for a Winner")


if __name__ == "__main__":
    main()
