import socket
from utils.Constants import *


class UDP:
    def __init__(self, ip, port, db, atm):
        self.ip = ip
        self.port = port

        self.serverInfo = (ip, port)    # tuple with server info
        self.serverSocket = None
        self.server_active = NOT_ACTIVE
        self.db = db  # reference for a db class to check
        self.atm = atm

    def activate_server(self):
        self.serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # datagram socket
        self.serverSocket.bind(self.serverInfo)

    def receive_clients(self):
        while self.server_active:
            print("Waiting For Client...")
            bytes_address_pair = self.serverSocket.recvfrom(BUFFER_SIZE)

            code = bytes_address_pair[0]

            client_address = bytes_address_pair[1]

            client_msg = "Message from Client:{}".format(code)
            client_ip = "Client IP Address:{}".format(client_address)

            print(client_msg)
            print(client_ip)

            # Sending a reply to client with the verification of the code

            self.serverSocket.sendto(self.encode_info("Allow"), client_address)

            # Receive Action

            bytes_address_pair = self.serverSocket.recvfrom(BUFFER_SIZE)

            action = bytes_address_pair[0]

            self.serverSocket.sendto(action, client_address)

    @staticmethod
    def encode_info(string):
        return str.encode(string)

    def getInfo(self):
        return self.encode_info("TEST")

    def verifyCode(self):
        return True

    def response_action(self, action):
        return self.encode_info(action)

    def start(self):
        self.activate_server()
        self.server_active = ACTIVE
        self.receive_clients()

    def turnOffAtm(self):
        self.atm.available = False
