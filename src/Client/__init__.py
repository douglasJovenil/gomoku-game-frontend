from Config import HOST, PORT, BUFFER_SIZE, ENCODING
from Connection import Connection
from threading import Thread
from json import loads, dumps
from time import sleep

class Client(Connection):
  def __init__(self, host=HOST, port=PORT, buffer_size=BUFFER_SIZE, encoding=ENCODING):
    Connection.__init__(self, host, port, buffer_size, encoding)
    self.data = None
    self.name = None

  def connect(self):
    self.sock.connect(self.addr)
    
  def keepConn(self):
    while (True):
      data = self.recv()

      if (data): 
        print(data, 'from class Client.py')
        self.data = loads(data) 
  
  def waitConn(self):
    # Aguarda os jogadores se conectarem
    while (True): 
      data = self.recv()
      if (data): break
  
  def send(self, data):
    self.sock.send(bytes(data, self.encoding))

  def recv(self):
    return self.sock.recv(self.buffer_size).decode(self.encoding)

  def keepConnThread(self):
    Thread(target=self.keepConn, daemon=True).start()

  def setdata(self, data):
    self.data = data
    
  def getData(self):
    if (self.data):
      return dumps(self.data)

  def getName(self):
    return self.name