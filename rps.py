""" Terminal rock, paper, scissors game """

import random
import numpy

input_dict = {1: 'rock', 2: 'paper', 3: 'scissors'}
win_loss_arr = numpy.array([[False, False, True], #-- matrix to represent outcomes
                            [True, False, False], #-- first index represents player choice, second is comp choice
                            [False, True, False]])#-- True represents a player win

inp = None #-- Input starts off un-initialised to activate while loop
while True: #-- This while loop will continue until there is valid input
    inp = input("Input 1 for rock, 2 for paper, or 3 for scissors\n")
    if inp not in ('1', '2', '3'):
        continue
    else:
        break

player_turn = int(inp) #-- Converts the string input into an integer

comp_turn = random.randint(1, 3) #-- Generates a random number representing the computer's turn

print(f"You chose: {input_dict[player_turn]}") #-- Prints the string representation of the player's choice
print(f"The computer chose: {input_dict[comp_turn]}") #-- Prints the string representation of the computer's choice
print("...")
if player_turn == comp_turn:
    print("It's a tie.")
elif win_loss_arr[player_turn-1, comp_turn-1]:
    print("You win!")
else:
    print("You lose...")
