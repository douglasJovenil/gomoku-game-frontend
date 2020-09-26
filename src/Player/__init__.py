from Piece import Piece
from Client import Client
from Board import Board
from Point import Point
from Data import Data
from threading import Thread
from json import dumps, loads

class Player(object):
  def __init__(self):
    self.board = Board()
    self.opponent_piece = Piece()
    self.piece = Piece()
    self.sock = Client()
    self.data = Data()

    self.sock.connect()

    self.addThread(self.checkMove)
    self.addThread(self.checkData)

    self.board.mainloop()

  def checkMove(self):
    while (True):
      if (self.board.eventMovePiece and self.data.getTurn() == self.data.getName() and self.data.getStarted()):
        self.piece.setPos(self.board.clickedPos)    
        
        if (self.board.drawPiece(self.piece, self.data.getName())):
          if (self.board.verifyWin(self.piece)): 
            aux = self.data
            aux.setWinner(self.data.getName())
            aux.setXY(*self.piece.getCoord())
            self.sock.send(aux.toString())
            color = self.piece.getColor()
            self.piece = Piece()
            self.piece.setColor(color)
          else:
            self.data.setXY(*self.piece.getCoord())        
            self.sock.send(self.data.toString()) 
            
          self.board.disable()
          self.board.restartEventMovePiece()

  def checkData(self):
    while(True):
      recv_data = loads(self.sock.recv())
      
      if (recv_data):
        if (self.data.getStarted()):
          self.data.setTurn(recv_data['turn'])
          opponent_data = Data()
          opponent_data.setFromDict(recv_data)
          
          if (recv_data['turn'] == self.data.getName()): # Jogando
            self.opponent_piece.setColor(opponent_data.getColor())
            self.opponent_piece.setPos(Point(opponent_data.getX(), opponent_data.getY()))
            self.board.drawPiece(self.opponent_piece, opponent_data.getName())
            self.board.enable()

          if (recv_data['winner'] != None): # Verifica vitoria
            print(f'Vencedor: {opponent_data.getName()} ganhou')
            print(f'Cor: {opponent_data.getColor()}')
            print(self.data.toString())
            self.data.resetInfo()
            self.board.clearBoard()
        else:
          if (self.data.getName() == None): # Aguardando jogadores
            self.data.setFromDict(recv_data)
            self.data.setColor(self.piece.getColor())
            self.board.setTitle(f'Jogador: {self.data.getName()}')
            print(f'Jogador: {self.data.getName()}')
          if (recv_data['started']): # Iniciando jogo
            self.data.setStarted(recv_data['started'])
      self.data.setWinner(None)
        
  def addThread(self, f):
    Thread(target=f, daemon=True).start()