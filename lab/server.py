import socket


class Server:
    def __init__(self, address=('', 80005)):
        self.main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address

    def bind(self):
        self.main_socket.bind(self.address)

    def listen(self):
        self.main_socket.listen(5)

    def accept(self):
        self.new_socket, self.address_info = self.main_socket.accept()

    def send(self, data):
        data = data.encode()
        self.new_socket.send(data)

    def recv(self, buffersize=1024):
        data = self.new_socket.recv(buffersize)
        return data

    def close(self):
        self.new_socket.close()
        self.main_socket.close()
