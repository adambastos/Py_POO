clientes = {}
while True:
    nome = input("Digite o nome do cliente (ou 'sair' para sair): ")
    if nome.lower() == 'sair':
        break

    try:
        valor = float(input('Digite o valor das compras: '))
    except ValueError():
        print('Valor incorreto, tente novamente.')
        continue

    if nome in clientes:
        clientes[nome].append(valor)
    else:
        clientes[nome] = [valor]
    

for cliente, valor in clientes.items():
    total_vendas = sum(valor)
    if total_vendas <= 1000:
        print(f'O cliente {cliente} está na categoria Bronze com R${total_vendas} em vendas. ')
    elif 1000 <= total_vendas <= 5000:
        print(f'O cliente {cliente} está na categoria Prata com R${total_vendas} em vendas.')
    elif total_vendas > 5000:
        print(f'O cliente {cliente} está na categoria Ouro com R${total_vendas} em vendas')
        