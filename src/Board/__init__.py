from Config import BOARD_SIZE, QNT_LINES, BOARD_COLOR, LINE_COLOR, PIECE_SIZE
from tkinter import Tk, Frame, Canvas, TOP, BOTH
from Piece import Piece
from Point import Point
from Client import Client
from threading import Thread
from time import sleep

from os import system

class Board(Tk):
  __slots = ('size', 'c_line', 'lines', 'step', 'canvas')

  def __init__(self, size=BOARD_SIZE, lines=QNT_LINES, c_background=BOARD_COLOR, c_line=LINE_COLOR):
    Tk.__init__(self)
    self.size = size
    self.c_line = c_line
    self.lines = lines
    self.step = size / lines
    
    offset = 10
    self.geometry(f'{size + offset}x{size + offset}')
    self.configure(background=c_background)

    self.container = Frame(self, background=c_background)
    self.container.pack(side=TOP, fill=BOTH, expand=True)
    self.container.grid_rowconfigure(0, weight=1)
    self.container.grid_columnconfigure(0, weight=1)

    self.canvas = Canvas(self.container, width=size, height=size, background=c_background, highlightthickness=0)
    self.canvas.pack()
    self.drawMatrix()

    self.pieces = self.emptyBoard()
    self.pieces_id = [] # Utilizadas para limpar o canvas
    self.eventMovePiece = False
    self.clickedPos = Point(0, 0)

    self.enable()

  def setTitle(self, text):
    self.container.winfo_toplevel().title(text)

  def enable(self):
    self.canvas.bind('<Button-1>', lambda e: self.clickEvent(e))

  def disable(self):
    self.canvas.unbind('<Button-1>')

  def drawMatrix(self):
    for i in range(self.lines):
      self.canvas.create_line(i * self.step, 0, i * self.step, self.size, fill=self.c_line)
      self.canvas.create_line(0, i * self.step, self.size, i * self.step, fill=self.c_line)

    self.canvas.create_line(self.size - 1, 0, self.size - 1, self.size - 1, fill=self.c_line)
    self.canvas.create_line(0, self.size - 1, self.size - 1, self.size - 1, fill=self.c_line)

  def clickEvent(self, e):
    for i in range(self.lines):
      for j in range(self.lines):
        if ((e.x > i * self.step) and (e.x < (i + 1) * self.step) and (e.y > j * self.step) and (e.y < (j + 1) * self.step)):
          x = i * self.step + (0.5 * self.step)
          y = j * self.step + (0.5 * self.step)
          self.clickedPos = Point(x, y)
          self.eventMovePiece = True

  def restartEventMovePiece(self):
    self.eventMovePiece = False

  def getClickedPos(self):
    return self.clickedPos

  def drawPiece(self, piece, player_name):
    j = int(piece.getCoordX() / self.step - 0.5)
    i = int(piece.getCoordY() / self.step - 0.5)
    
    if (self.pieces[i][j] == None):
      self.pieces_id.append(self.canvas.create_oval(piece.pos.x - piece.rad, piece.pos.y - piece.rad, piece.pos.x + piece.rad, piece.pos.y + piece.rad, fill=piece.color, outline=''))
      self.pieces[i][j] = piece
      return True
    return False

  def clearBoard(self):
    for id in self.pieces_id: self.canvas.delete(id) # Remove as pecas
    self.pieces = self.emptyBoard()
    
  def emptyBoard(self):
    return [[None for i in range(QNT_LINES)] for i in range(QNT_LINES)] # Gera uma matriz vazia

  # Que orgulho brother
  def verifyWin(self, piece):
    # Remove indices inexistentes
    filter_indexes = lambda lst: [p for p in lst if p.validate()]
    # Recebe a matriz 5x5, filtra os indices e conta a quantidade de pecas
    count = lambda lst: len(list(filter(lambda d: self.pieces[d.getX()][d.getY()] == piece, filter_indexes(lst))))
    
    # Procura pelas pecas e calcula a matriz 5x5 ao redor da mesma
    indexes = filter(lambda p: self.pieces[p.getX()][p.getY()] == piece, [Point(i, j) for i in range(QNT_LINES) for j in range(QNT_LINES)])
    for p in indexes:
      mains = count([Point(p.getX() + i, p.getY() + i) for i in range(-2, 3)])
      secs = count([Point(p.getX() - i, p.getY() + i) for i in range(-2, 3)])
      rows = count([Point(p.getX(), p.getY() + i) for i in range(-2, 3)])
      cols = count([Point(p.getX() + i, p.getY()) for i in range(-2, 3)])
      if (mains == 5 or secs == 5 or rows == 5 or cols == 5): return True
    return False