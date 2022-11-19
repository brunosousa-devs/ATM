from connection.Connection import *


class Client:
    def __init__(self):
        self.conn = Connection()

    def run(self):
        while True:
            code = input("Insert your code: ")
            if code == "-1":
                break
            validation = self.conn.insert_card(code)
            if not validation:
                continue
            action = [int(input("1- Withdraw Money\n"
                                "2- See Account Movements\n"
                                "3- Transfer Money"))]

            if action[0] == 1:
                money = int(input("Insert Quantity: "))
                action.append(str(money))
            if action[0] == 3:
                amount_money = input("")
                nif_account_to_send = input("Insert Nif: ")
                action.append(amount_money)
                action.append(nif_account_to_send)

            result = self.conn.action(str(action))
            print(result)
