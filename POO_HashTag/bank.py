class ContaCorrente():
    
    def __init__(self, titular, cpf):
        self.titular = titular
        self.saldo = 0
        self.cpf = cpf
    
    def deposito(self, deposito) -> None:
        self.saldo += deposito
    
    def saque(self, saque) -> None:
        self.saldo -= saque
    
    def exibe_saldo(self):
        print(f'Seu saldo é R$ {self.saldo}')

titular = input('Digite seu nome: ')
cpf = int(input('Digite seu CPF: '))
conta = ContaCorrente(titular, cpf)

print(f'Bem vindo, {conta.titular}')
opt = input('Deseja realizar um depósito? Digite S ou N \n').strip().upper()


if opt == 'S':
    valor = float(input('Digite o valor para depósito: '))
    conta.deposito(valor)
    print(f'Saldo da conta: {conta.saldo}')
elif opt == 'N':
    print(f'Seu saldo atualizado é de: R${conta.exibe_saldo()}')
else:
    print('Opção não reconhecida, tente novamente.')

opt = input('Deseja realizar um saque? Digite S ou N \n').strip().upper()
if opt == 'S':
    valor = float(input('Digite o valor do saque: '))
    if valor <= conta.saldo:
        conta.saque(valor)
        print('Saque realizado com sucesso. \n')
        print(f'Saldo da sua conta atualizado: R${conta.saldo}')
    else:
        print('Saldo insuficiente, consulte o valor do seu saldo bancário e tente novamente.')


    




