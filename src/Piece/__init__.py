from Point import Point
from random import randint
from Config import PIECE_SIZE

class Piece(object):
  __slots__ = ('color', 'rad', 'pos')

  def __init__(self):
    randColor = lambda: f'#{hex(randint(16, 255))}{hex(randint(16, 255))}{hex(randint(16, 255))}'.replace('0x', '')
  
    self.color = randColor()

    self.rad = PIECE_SIZE
    self.pos = Point(0, 0)

  def getCoord(self):
    return (self.pos.x, self.pos.y)

  def getCoordX(self):
    return self.pos.x

  def getCoordY(self):
    return self.pos.y

  def getColor(self):
    return self.color

  def setPos(self, point):
    self.pos = point

  def getPos(self):
    return self.pos

  def setColor(self, color):
    self.color = color