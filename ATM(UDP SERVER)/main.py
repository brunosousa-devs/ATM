from atm.Atm import *


def runATM(name):
    atm = Atm()
    print(f'ATM {name} has started.')
    atm.run()


if __name__ == '__main__':
    runATM("ATM TEST")

