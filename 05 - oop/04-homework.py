class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.__balance}")
        else:
            print("Deposit amount must be greater then zero")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew, ${amount},New balance: ${self.__balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def inquiry(self):
        print(f"Current Balance: ${self.__balance}")


if __name__ == '__main__':
    account = BankAccount(1000)
    account.deposit(500)
    account.withdraw(200)

    account.inquiry()
