import random as r
gameState = "not playing"
class game:
    def __init__(self, player,type,playing):
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
            myDecision = r.choice(['rock','paper','scissors'])
            if myDecision == 'rock':
                if playerchoice == 'rock':
                    self.result = "I choose Rock. The game is a draw."
                if playerchoice == 'paper':
                    self.result = 'I choose Rock. Paper beats Rock. You win.'
                if playerchoice == 'scissors':
                    self.result = 'I choose Rock. Rock beats Scissors. I win.'
            if myDecision == 'paper':
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
            self.isPlaying = False
            self.player = 'none'    
        if self.type == 'ticTacToe':
            if self.state[playerchoice] != ' ':
                self.turn = 'player turn'
                self.error = 'You cannot play in a space that is already taken!'
            elif playerchoice >8:
                self.error = 'You cannot play outside the board!'
            else:
                self.something = 'Terminate'
                self.state[playerchoice] = 'x'
                for space in self.state:
                    if space == ' ':
                        self.something = 'ongoing'
                win = self.checkForWinner
                if win == 'x':
                    self.result = "You win"
                if win == 'o':
                    self.result = "I win"
                else:
                    if self.something == 'ongoing':
                        attempt = 'undecided'
                        while not attempt == ' ':
                            myChoice = r.randint(0,8)
                            attempt = self.state[myChoice]
                        self.state[myChoice]='o'
                    else:
                        win = self.checkForWinner
                        if win == 'x':
                            self.result = "You win"
                        if win == 'o':
                            self.result = "I win" 
                        else:
                            self.result = 'The board is full and nobody has won'    
    def checkForWinner(self):
        if self.type == 'ticTacToe':
                if  self.state[0] == self.state[1] == self.state[2] != ' ':
                    return self.state[0]
                if self.state[0] == self.state[3] == self.state[6] != ' ':
                    return self.state[1]
                if self.state[0] == self.state[4] == self.state[8]!= ' ':
                    return self.state[0]
                if self.state[1] == self.state[4] == self.state[7]!= ' ':
                    return self.state[1]
                if self.state[3] == self.state[4] == self.state[5]!= ' ':
                    return self.state[3]
                if self.state[2] == self.state[5] == self.state[8] != ' ':
                    return self.state[2]
                if self.state[2] == self.state[4] == self.state[6] != ' ':
                    return self.state[2]
                if self.state[6] == self.state[7] == self.state[8] != ' ':
                    return self.state[6]
                return 'Nobody'
    def displayState(self):
        if self.type == 'ticTacToe':
            self.something = 'No Space'
            for space in self.state:
                    if space == ' ':
                        self.something = 'ongoing'
            if self.checkForWinner() == 'Nobody':
                if self.something == 'No Space':
                    outputString = f'The game is a draw!\n  {self.state[0]}  |   {self.state[1]}   |  {self.state[2]}  \n ----------\n  {self.state[3]}  |   {self.state[4]}   |  {self.state[5]} \n ----------\n  {self.state[6]}  |   {self.state[7]}   |  {self.state[8]}'
                    self.isPlaying = False
                else:
                    outputString = f'\n  {self.state[0]}  |   {self.state[1]}   |  {self.state[2]}  \n ----------\n  {self.state[3]}  |   {self.state[4]}   |  {self.state[5]} \n ----------\n  {self.state[6]}  |   {self.state[7]}   |  {self.state[8]}'
            elif self.checkForWinner() == 'x':
                outputString = f'You Win.\n  {self.state[0]}  |   {self.state[1]}   |  {self.state[2]}  \n ----------\n  {self.state[3]}  |   {self.state[4]}   |  {self.state[5]} \n ----------\n  {self.state[6]}  |   {self.state[7]}   |  {self.state[8]}'
                self.isPlaying = False
            elif self.checkForWinner() == 'o':
                outputString = f'I Win.\n  {self.state[0]}  |   {self.state[1]}   |  {self.state[2]}  \n ----------\n  {self.state[3]}  |   {self.state[4]}   |  {self.state[5]} \n ----------\n  {self.state[6]}  |   {self.state[7]}   |  {self.state[8]}'
                self.isPlaying = False
            return outputString
rps=game('none','rps',False)
ticTacToe = game('none','ticTacToe',False)