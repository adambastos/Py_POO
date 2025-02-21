class Bank():
    def __init__(self, name, balance, cpf):
        self.name = name
        self.balance = balance
    

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, account2):
        self.balance -= amount
        print(f'Transferência realizada com sucesso! Novo saldo de {self.name}: {self.balance}')
        account2.balance += amount
        print(f'Saldo da conta de {account2.name}: {account2.balance}')
    

bank = Bank("John", 1000, "12345678900")
account2 = Bank("Jane", 500, "12345678901")
print(bank.get_balance())
print(bank.name)
bank.transfer(200, account2)
print(account2.balance)
print(account2.name)