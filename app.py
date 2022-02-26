'''
1 - Criar imagens para serem usadas
2 - Logica basica
3 - Player vs player
4 - Quadro de pontos
5 - Player vs AI
'''

class Jokenpo:
    player1 = ''
    player2 = ''
    player1Score = 0
    player2Score = 0
    player1Choice = ''
    player2Choice = ''
    turn = ''
    def setGameMode(self):
        return
    def setPlayerName(self):
        return
    def setChoice(self):
        return
    def play(self):
        return
    def chageTurn(self):
        self.turn = self.player1 if self.turn == self.player2 else self.player2
    def startTurn(self):
        # Set choice
        # Change turn
        return
    def start(self):
        print('INICIOU !!!')
        # Set game mode (player vs player | player vs AI)
        # Set players names
        self.turn = self.player1
        self.player1Score = 0
        self.player2Score = 0
        self.player1Choise = ''
        self.player2Choise = ''

# Tests
print(Jokenpo.player1Score, Jokenpo.player1Choice)
Jokenpo.start(Jokenpo)