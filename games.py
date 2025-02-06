import random as r
class game:
    def __init__(self, player,type,playing,turn):
        self.player = player
        self.type = type
        self.isPlaying = playing
        self.result = 'none'
        self.turn = 'player turn'
        if self.type == 'rps':
            self.initialstate = 'no choice'
        if self.type == 'ticTacToe':
            self.initialstate = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    def reset(self):
        self.player = 'nobody'
        self.isPlaying = False
        self.state = self.initialstate
    def takeTurn(self,playerchoice):
        if self.type == 'rps':
            myDecision = r.choice['rock','paper','scissors']
            if myDecision == 'rock':
                if playerchoice == 'rock':
                    self.result = "I choose Rock. The game is a draw."
                if playerchoice == 'paper':
                    self.result = 'I choose Rock. Paper beats Rock. You win.'
                if playerchoice == 'scissors':
                    self.result = 'I choose Rock. Rock beats Scissors. I win.'
            elif myDecision == 'paper':
                if playerchoice == 'paper':
                    self.result = "I choose Paper. The game is a draw."
                if playerchoice == 'scissors':
                    self.result = 'I choose Paper. Scissors beats Paper. You win.'
                if playerchoice == 'rock':
                    self.result = 'I choose Paper. Paper beats Rock. I win.'
            if myDecision == 'scissors':
                if playerchoice == 'scissors':
                    self.result = "I choose Scissors. The game is a draw."
                if playerchoice == 'paper':
                    self.result = 'I choose Scissors. Scissors beats Paper. I win.'
                if playerchoice == 'rock':
                    self.result = 'I choose Scissors. Rock beats Scissors. You win.'
        if self.type == 'ticTacToe':
            if self.state[playerchoice] != ' ':
                self.turn = 'player turn'
                self.error = 'You cannot play in a space that is already taken!'
rps=game('none','rps',False)
ticTacToe = game('none','ticTacToe',False)