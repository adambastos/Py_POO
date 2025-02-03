def add(prod, qnt):
    print('')
    print('--Adicionar produto--')
    prod = input('Nome do produto: ')
    qnt = int(input('Quantidade: '))
    dicio_produtos[prod] = qnt

def remove(prod, qnt_rm):
    print('')
    print('--Remover produto--')
    prod = input('Nome do produto: ')
    if prod in dicio_produtos:
        qnt_rm = int(input('Quantidade: '))
    if qnt_rm <= dicio_produtos[prod]:
        dicio_produtos[prod] -= qnt_rm

def show_list():
    print('')
    print('Lista atualizada: ')
    print(dicio_produtos)


dicio_produtos = {}
prod = ''
qnt = 0
opt = 0
qnt_rm = 0

while opt != 4:
    print('')
    print('--Escolha uma opção--')
    opt = int(input(' 1 - Inserir produto \n 2 - Remover produto \n 3 - Mostrar lista \n 4 - Sair \n'))
    if opt == 1:
        add(prod, qnt)
    elif opt == 2:
        remove(prod, qnt_rm)
    elif opt == 3:
        show_list()
    else:
        print('Encerrando!')
        break    
