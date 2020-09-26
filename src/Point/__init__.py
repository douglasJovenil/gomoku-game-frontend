from Config import QNT_LINES

class Point(object):
  __slots__ = ('x', 'y')

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def compare(self, point):
    if (self.x == point.x and self.y == point.y): return True
    return False

  def setX(self, x):
    self.x = x

  def getX(self):
    return self.x

  def setY(self, y):
    self.y = y

  def getY(self):
    return self.y

  def validate(self):
    if (self.x >= 0 and self.x < QNT_LINES and self.y >= 0 and self.y < QNT_LINES): return True
    return False

  def __repr__(self):
    return f'x: {self.x} y: {self.y}'