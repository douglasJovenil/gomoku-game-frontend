from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

class Connection(object):
  def __init__(self, host, port, buffer_size, encoding):
    self.host = host
    self.port = port
    self.addr = (host, port)
    self.buffer_size = buffer_size
    self.encoding = encoding
    self.sock = socket(AF_INET, SOCK_STREAM)

  def send(self, sock, data):
    sock.send(bytes(data, self.encoding))

  def recv(self, sock):
    return sock.recv(self.buffer_size).decode(self.encoding)

  def utf(self, data):
    return bytes(data, self.encoding)

  def close(self):
    self.sock.close()

