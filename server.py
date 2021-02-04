#coding: utf-8
#server side
import socket

class Server:
    def __init__(self):
        self.ip = "127.0.0.1"                #string
        self.port = 7700                     #int
        self.socket_make(self.ip, self.port) #socket作成

    def socket_make(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET IPv4指定, SOCK_STREAM プロトコル: TCP
        self.s.bind((ip, port))             #サーバー立ち上げ, tuple
        self.s.listen(1)                    #接続依頼の窓口

        while True:
            print("Waiting communication...")
            conn, addr = self.s.accept()
            print("Connected by {}".format(addr))
            data = conn.recv(1024)          #1024biteで受け取り
            if not data:
                break                       #中身なければ終了
            print(data)                     #受け取りのメッセージ表示
            conn.send(b"I recerived")       #受け取り確認

server = Server()                           #インスタンス作成