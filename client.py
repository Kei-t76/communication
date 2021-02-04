import socket

class Client:
    def __init__(self):
        self.server = "127.0.0.1"                #string!
        self.server_port = 7700                     #int!
        self.socket_make(self.ip, self.port) #socket作成

    def socket_make(ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET IPv4指定, SOCK_STREAM プロトコル: TCP
        self.s.connect((ip, port)) #connectする相手のip, port入力

server = Server()