from RockPaperScissors import scissorsPaperRock
import sys

userPlaying = True

while userPlaying:
    players_action = input("Please type the letter corresponding to your action (Paper[p], Scissors[s], Rock[r]:")
    scissorsPaperRock.gameEngine(players_action)
    
