import random as r
class game:
    global playerchoice
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
    def takeTurn(self):
        if self.type == 'rps':
            myDecision = r.choice['rock','paper','scissors']
            if myDecision == 'rock':
                if playerchoice == 'rock':
                    self.result = "The game is a draw."
                if playerchoice == 'paper':
                    self.result = 'You win.'
                if playerchoice == 'scissors':
                    self.result = 'I win.'
            elif myDecision == 'paper':
                if playerchoice == 'paper':
                    self.result = "The game is a draw."
                if playerchoice == 'scissors':
                    self.result = 'You win.'
                if playerchoice == 'rock':
                    self.result = 'I win.'
            if myDecision == 'scissors':
                if playerchoice == 'scissors':
                    self.result = "The game is a draw."
                if playerchoice == 'paper':
                    self.result = 'I win.'
                if playerchoice == 'rock':
                    self.result = 'You win.'
        if self.type == 'ticTacToe':
            pass
rps=game('none','rps',False)
ticTacToe = game('none','ticTacToe',False)