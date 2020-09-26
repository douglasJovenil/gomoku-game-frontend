from json import dumps

class Data(object):
  def __init__(self, x=0, y=0, color=None, name=None, turn=None, started=False, winner=None):
    self.x = x
    self.y = y
    self.color = color
    self.name = name
    self.turn = turn
    self.started = started
    self.winner = winner

  # Reseta informacoes menos started
  def resetInfo(self):
    self.x = 0
    self.y = 0
    self.winner = None

  def toString(self):
    return dumps(self.getDict())  
  
  def setFromDict(self, data):
    self.x, self.y, self.color, self.name, self.turn, self.started, self.winner = data.values()

  def getDict(self):
    return {'x': self.x, 'y': self.y, 'color': self.color, 'name': self.name, 'turn': self.turn, 'started': self.started, 'winner': self.winner} 

  def getX(self):
    return self.x

  def setX(self, value):
    self.x = value

  def getY(self):
    return self.y

  def setY(self, value):
    self.y = value

  def setXY(self, x, y):
    self.x = x
    self.y = y

  def getColor(self):
    return self.color

  def setColor(self, value):
    self.color = value

  def getName(self):
    return self.name

  def setName(self, value):
    self.name = value

  def getTurn(self):
    return self.turn

  def setTurn(self, value):
    self.turn = value

  def getStarted(self):
    return self.started

  def setStarted(self, value):
    self.started = value
    
  def getWinner(self):
    return self.winner

  def setWinner(self, value):
    self.winner = value
