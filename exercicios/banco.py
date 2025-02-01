class Bank():
    def __init__(self):
        self.titular = ''
        self.saldo = 0.0
    
    def deposito(self, valor_dep):
        self.saldo += valor_dep
    
    def saque(self, valor_saque):
        self.saldo -= valor_saque

    def exibe_saldo(self):
        print(f'Seu saldo é de {self.saldo}') 

print('Seja bem vindo ao Adam Bank.')

banco = Bank()
opt_dep = input('Deseja realizar um depósito? S ou N   ').strip().upper()
if opt_dep == 'S':
    valor_dep = float(input('Digite o valor do depósito: '))
    banco.deposito(valor_dep)
    banco.exibe_saldo()
elif opt_dep == 'N':
    print(f'Seu saldo é de {banco.saldo}')
else: 
    print('Opção não reconhecida.')

opt_saque = input('Deseja realizar um saque? S ou N   ').strip().upper()
if opt_saque == 'S':
    valor_saque = float(input('Digite o valor do saque: '))
    if valor_saque > banco.saldo:
        print('Você não possui saldo suficiente.')
    else:
        banco.saque(valor_saque)
    print(f'Seu saldo é de {banco.saldo}')
elif opt_saque == 'N':
    print('Obrigado e volte sempre!')

