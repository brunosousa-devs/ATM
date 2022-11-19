from utils.Constants import *
import socket


class Connection:
    def __init__(self):
        self.bank_address = BANK_IP
        self.bank_port = BANK_PORT

        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        self.bank_info = (self.bank_address, self.bank_port)

    def insert_card(self, pin):
        self.socket.sendto(self.encode(pin), self.bank_info)
        return self.socket.recvfrom(BUFFER_SIZE)

    def action(self, action):
        self.socket.sendto(self.encode(action), self.bank_info)
        return self.socket.recvfrom(BUFFER_SIZE)

    @staticmethod
    def encode(pin):
        return str.encode(pin)
