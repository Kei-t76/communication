import socket

class Server:
    def __init__(self):
        self.ip = "127.0.0.1"                #string!
        self.port = 7700                     #int!
        self.socket_make(self.ip, self.port) #socket作成

    def socket_make(ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET IPv4指定, SOCK_STREAM プロトコル: TCP
        self.s.bind((ip, port)) #サーバー立ち上げ, タプルを渡す!
        self.s.listen(1)        #接続以来の窓口

        while True:
            print("Waiting communication...")
            conn, addr = self.s.accept()
            print("Connected by()".format(addr))

server = Server()