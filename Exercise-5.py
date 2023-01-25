# the naming of file is done according to the 
# # sample test case given
# i saw a couple of videos to understand how classes work and how
# to initiate methods under a class
# https://www.youtube.com/watch?v=lVfGQOzzRCM
# https://www.youtube.com/watch?v=8O5kX73OkIY
class BankAccount:
    def __init__(self, name):
        self._name = name
        self._balance = 0
    
    def deposite(self, name, amount):
        if name != self._name:
            print("Wrong name")
            return
        self._balance += amount
        return self._balance


    def withdraw(self, name, amount):
        if name != self._name:
            print("Wrong name")
            return
        if amount > self._balance:
            print("Not sufficient balance")
        else:
            self._balance -= amount
        return self._balance



    def get_balance(self, name):
        if name != self._name:
            print("Wrong name")
            return
        return (f"{self._name } has a balance of ${ self._balance}")


def main():
    account = BankAccount("Wally")
    deposit = account.deposite("Wally",100)
    withdraw = account.withdraw("Wally", 29.84)
    balance = account.get_balance("Wally")
    print(balance)

if __name__ == '__main__':
    main()