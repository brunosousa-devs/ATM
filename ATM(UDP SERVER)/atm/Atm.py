from server.UDP import *
from db.DataBaseManager import *
from utils.Constants import *


class Atm:
    def __init__(self):
        db = DataBaseManager()
        self.udpServer = UDP(IP_LOCALHOST, PORT_LOCALHOST, db, self)
        self.available = True

    def run(self):
        while self.available:
            self.udpServer.start()

