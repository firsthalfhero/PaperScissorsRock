import random
import sys


global opponents_action
global result

class scissorsPaperRock():
    def __init__(self, opponents_action, result):
        self.opponents_action = opponents_action
        self.result = result
    
    def scissors(opponents_action):
        global result
        if opponents_action == 'paper':
            result = 'win'
        elif opponents_action == 'rock':
            result = 'lose'
        elif opponents_action == 'scissors':
            result = 'draw'
        else:
            result = 'Please enter a valid action'
        return result
            
    def paper(opponents_action):
        global result
        # print("In paper:",opponents_action)
        if opponents_action == 'paper':
            result = 'draw'
        elif opponents_action == 'rock':
            result = 'win'
        elif opponents_action == 'scissors':
            result = 'lose'
        else:
            result = 'Please enter a valid action'
        return result
    
    def rock(opponents_action):
        global result
        
        if opponents_action == 'paper':
            result = 'lose'
        elif opponents_action == 'rock':
            result = 'draw'
        elif opponents_action == 'scissors':
            result = 'win'
        else:
            result = 'Please enter a valid action'
        return result

    def opponents_move():
        global opponents_action
        pick = random.randrange(0,2,1)
        opponents_action = ['rock','paper','scissors']
        # print("Opponents action:", opponents_action[pick])
        return opponents_action[pick]
    

    def gameEngine(players_action):
        global result
        opponents_action = scissorsPaperRock.opponents_move()
        if players_action == 'p':
            players_action = 'paper'
            result = scissorsPaperRock.paper(opponents_action)
        elif players_action == 'r':
            players_action = 'rock'
            result = scissorsPaperRock.rock(opponents_action)
        elif players_action == 's':
            players_action = 'scissors'
            result = scissorsPaperRock.scissors(opponents_action)
        else:
            print("Oops, ",players_action," doesn't seem to be a valid action. Please try again")
            sys.exit()
        
        #announce result
        
        if result == 'win':
            print("Congratulations you've won. The computer played", opponents_action,"and you played", players_action)
        elif result == 'lose':
            print("Sorry you've lost. The computer played", opponents_action,"and you played", players_action)
        elif result == 'draw':
            print("Play again, its a draw. The computer played", opponents_action,"and you played", players_action)
        else:
            print("Oops, something went wrong")
