#coding: utf-8
#client side

import socket

class Client:
    def __init__(self):
        self.server_ip = "127.0.0.1"                #string!
        self.server_port = 7700                     #int!
        self.socket_make(self.server_ip, self.server_port) #socket作成

    def socket_make(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET IPv4指定, SOCK_STREAM プロトコル: TCP
        self.s.connect((ip, port))                  #connectする相手のip, port入力
        self.s.send(b"Hello")                       #ソケットメッセージは全てバイナリ形式
        data = self.s.recv(1024)
        print(data)                                 #受け取ったデータを表示

client = Client()