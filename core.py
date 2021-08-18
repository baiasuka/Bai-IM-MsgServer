import socket
import json
import time
from threading import Thread

# 消息比特字符终结标识
MESSAGE_OVER_FLAG = b'2xx@oo$n'

ip_list = {}


def send_msg(cilent, addr):
    try:
        bytes_queue = b''
        while True:
            new_bytes = cilent.recv(1024)
            if new_bytes:
                bytes_queue += new_bytes
                byte_split = bytes_queue.split(MESSAGE_OVER_FLAG)
                if len(byte_split) == 2:
                    byte_content, bytes_queue = byte_split
                    for cil in ip_list.values():
                        cil.send(byte_content + MESSAGE_OVER_FLAG)
    except Exception as e:
        print(e)

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
