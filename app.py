'''
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
    player1Choice = '' # rock, scissors and paper
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

# Interface
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Jokenpo')
window.setFixedWidth(800)
window.setFixedHeight(600)
window.setStyleSheet('background: #000000')

imageScissors = QPixmap('images/scissors.png')
imageScissorsLabel = QLabel()
imageScissorsLabel.setPixmap(imageScissors)
imageScissorsLabel.setStyleSheet('')

imagePaper = QPixmap('images/paper.png')
imagePaperLabel = QLabel()
imagePaperLabel.setPixmap(imagePaper)
imagePaperLabel.setStyleSheet('')

button = QPushButton('Play')
button.setStyleSheet(
    '*{border: 4px solid "#009933"; border-radius: 15px; font-size: 35px; color: "white"; padding: 25px 0px; margin: 10px 20px}' +
    '*:hover{border-color: "#CCFFCC"; background: "#009933"}')

grid = QGridLayout()
grid.addWidget(imageScissorsLabel, 0, 0)
grid.addWidget(imagePaperLabel, 0, 1)
grid.addWidget(button, 1, 0)
window.setLayout(grid)

window.show()
sys.exit(app.exec())
