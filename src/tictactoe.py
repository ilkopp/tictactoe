import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class tictactoe(QMainWindow):
   def __init__(self):
        super().__init__()
  
        self.counter=0

        self.setWindowTitle("TicTacToe")
  
        self.setGeometry(200,200,200,200)

        widget = QWidget(self)

        self.layout = QGridLayout()

        widget.setLayout(self.layout)

        self.setCentralWidget(widget)

        self.createField()
  
        self.show()
    

   def perform_move(self):
      button = self.sender()

      #Mark the field selected by the user accordingly
      #TODO: Replace strings by pictures
      if self.counter %2 == 0:
         button.setText("x")
      else:
         button.setText("o")
      self.counter+=1
      #tictactoe fields can only be selected once
      button.setEnabled(False)
      #after each move, check whether the game ended by this move
      gameEnd, winner = self.checkGameEnd()
      if gameEnd:
         self.handleGameEnd(winner)
          
         
   def handleGameEnd(self, winner):
      for button in self.buttons:
         button.setEnabled(False)

      #TODO: Use an overlay or similar to indicate game end, dont use terminal only
      print("Game ended")
      if winner == 0:
         print("X won")
      elif winner == 1:
         print("O won")
      else:
         print("undecided")

      #TODO: offer option to reset the game and restart


   def createField(self):
      self.buttons = []
      #add buttons in a 3x3 field to create tictactoe
      for i in range(3):
         for j in range(3):
            button = QPushButton(self)
            #to access buttons later on, we need to save them
            self.buttons.append(button)
            button.setText("")
            button.setFixedSize(80,80)
            #button.setFlat(True)
            button.clicked.connect(self.perform_move)
            self.layout.addWidget(button, i, j)


   def checkGameEnd(self):
      gameEnd = False
  
      #if a winner exists, the game ends
      winner = self.checkWinner()
      if winner != -1:
         gameEnd = True
         return gameEnd, winner

      #if there is no winner and fields in the game are still empty, then the game is still running
      if self.counter<9:
         return gameEnd, winner   
      else:
         gameEnd = True

      return gameEnd, winner


   def checkWinner(self):
      winner = -1
      
      #vertical case
      for i in range(3):
         if self.buttons[i].text() == self.buttons[i+3].text() and self.buttons[i].text() == self.buttons[i+6].text():
            if self.buttons[i].text() == "x":
               winner = 0
               break
            elif self.buttons[i].text() == "o":
               winner = 1
               break

      #horizontal case
      for i in [0,3,6]:
         if self.buttons[i].text() == self.buttons[i+1].text() and self.buttons[i].text() == self.buttons[i+2].text():
            if self.buttons[i].text() == "x":
               winner = 0
               break
            elif self.buttons[i].text() == "o":
               winner = 1
               break

      #diagonal case
      if (self.buttons[0].text() == self.buttons[4].text() and self.buttons[0].text() == self.buttons[8].text()) \
         or (self.buttons[2].text() == self.buttons[4].text() and self.buttons[2].text() == self.buttons[6].text()):
         #use button 4 beceause its relevant for both diagonals
         if self.buttons[4].text() == "x":
            winner = 0
         elif self.buttons[4].text() == "o":
            winner = 1

      return winner
  

if __name__ == '__main__':
   App = QApplication(sys.argv)
   
   # create the instance of our Window
   window = tictactoe()
   
   # start the app
   sys.exit(App.exec())
