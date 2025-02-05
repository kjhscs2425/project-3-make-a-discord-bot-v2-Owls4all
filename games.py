class game:
    def __init__(self, player,type,playing):
        self.player = player
        self.type = type
        self.isPlaying = playing
        if self.type == 'rps':
            self.initialstate = 'no choice'
        if self.type == 'ticTacToe':
            self.initialstate = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    def reset(self):
        self.player = 'nobody'
        self.isPlaying = False
        self.state = self.initialstate
    def turn(self):
        pass
rps=game('none','rps',False)
ticTacToe = game('none','ticTacToe',False)