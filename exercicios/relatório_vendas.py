vendas = {}
'''
    #Quando usamos while True, estamos criando um loop infinito, ou seja, ele continuará executando os comandos dentro dele sem parar.

    #Esse tipo de loop é útil quando não sabemos, de antemão, quantas vezes o usuário vai fornecer dados.
'''

while True:
    nome = input("Digite o nome do vendedor (ou 'sair' para sair): ")
    if nome.lower() == 'sair':
        print('Programa encerrado!')
        break
    try:
        valor = float(input('Digite o valor da venda: '))
    except ValueError:
        print('Valor incorreto, tente novamente. ')
        continue
    if nome in vendas:
        vendas[nome].append(valor)
    else:
        vendas[nome] = [valor]

print('Atualização sobre vendas: ')
for vendedor, lista_vendas in vendas.items(): #O método .items() de um dicionário retorna uma (view) dos pares (chave, valor) - Ex: "João": [100, 300], lista_vendas será [100, 300].
    total = sum(lista_vendas)
    media = total / len(lista_vendas)
    print(f'{vendedor}: Total de vendas = R${total}. Média de vendas = R${media}')
    print(vendas.items())
       




    