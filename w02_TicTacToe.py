# CSE210 | Week 2 Prove: Developer - Solo Code Submission
# Tic-Tac-Toe Game
# Author: Ruth Alejandra Bravo Pérez

def main():
    # Get the players' name 
    player_1 = input ("Type the name of Player 1: ")
    player_2 = input ("Type the name of Player 2: ")
    
    # Create an empty dictionary to save the player's taken spaces
    taken_spaces_dict = {}

    occupied_spaces = 0

    # Create a loop to ask for the players' input until one
    # of them have completed a line, or all the spaces are occupied
    while occupied_spaces < 9:

        # Display the game interface
        interface_spaces = interface_data(taken_spaces_dict)
        print ()
        create_interface_grid (interface_spaces)
        print ()

        # Players input the spaces they want to mark
        print (f"\n{player_1}'s turn")
        space_player1 = input ("Type the number of the space you want to mark: ")
        taken_spaces_dict[space_player1]= "X"
        occupied_spaces += 1

        print (f"\n{player_2}'s turn")
        space_player2 = input ("Type the number of the space you want to mark: ")
        taken_spaces_dict[space_player2]= "O"
        occupied_spaces += 1

def interface_data(taken_spaces_dict):
    """This function will check the numbers indicating
    available spaces for the users to put their marks to create 
    the layout interface."""

    # Create a list with the numbers of the spaces in the board
    spaces_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Create an empty list to append the spaces with the places 
    # taken by the players
    modifyied_spaces = []

    # If a key in the taken_spaces_dict matches a number in the 
    # spaces list, the player's mark will replace the number
    for i in spaces_list:
        if i in taken_spaces_dict:
            mark = taken_spaces_dict[i]
            modifyied_spaces.append(mark)
        else:
            modifyied_spaces.append(i)

    return modifyied_spaces

def create_interface_grid (interface_data_list):
    """Take a list with the numbers and marks to print in the 
    form of a grid."""

    for i in range (0, 3):
        print (interface_data_list[i], end="|")

    print ("\n-+-+-")
    for i in range (3, 6):
        print (interface_data_list[i], end="|")

    print ("\n-+-+-")
    for i in range (6, 9):
        print (interface_data_list[i], end="|")

def find_winner (modified_spaces):
    winner_x = ["X", "X", "X"]
    winner_o = ["O", "O", "O"]
    
    


if __name__ == "__main__":
    main()