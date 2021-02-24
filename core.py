import socket
import json
import time
from threading import Thread


ip_list = {}

def send_msg(cilent, addr):
    try:
        while True:
            content = cilent.recv(1024)
            if content:
                print(json.loads(content.decode("utf-8")))
                for cil in ip_list.values():
                    cil.send(content)
    except Exception as e:
        print(e)
        cilent.close()

class Core:
    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 5000

    def start(self):
        print("server start")
        try:
            s = socket.socket()
            s.bind((self.host, self.port))
            s.listen(5)
            while True:
                cilent, addr = s.accept()
                if addr not in ip_list or ip_list[addr] != cilent:
                    rev_thread = Thread(target=send_msg, args=(cilent, addr))
                    rev_thread.start()
                ip_list[addr] = cilent
        except Exception as e:
            print("server shutdown")

if __name__ == '__main__':
    core = Core()
    core.start()
