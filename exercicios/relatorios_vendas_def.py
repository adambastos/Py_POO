def coletar_vendas():
    vendas = {}
    while True:
        nome = input("Digite o nome do vendedor (ou 'sair' para sair): ")
        if nome.lower() == 'sair':
            print('Programa encerrado.')
            break
        try:
            valor = float(input('Digite a venda: '))
        except ValueError:
            print('Valor incorreto, tente novamente. ')
            continue
        if nome in vendas:
            vendas[nome].append(valor)
        else:
            vendas[nome] = [valor]
    return vendas

def calcula(vendas):
    relatorio = {}
    for vendedor, lista_vendas in vendas.items():
        total = sum(lista_vendas)
        media = total / len(lista_vendas) if lista_vendas else 0
        relatorio[vendedor] = {"total": total, "media": media} #Adicionando outro dicionário ao dicionário já existente
    return relatorio

def show_relatorio(relatorio):
    print('Relatorio atualizado')
    for vendedor, dados in relatorio.items():
        total = dados["total"]
        media = dados["media"]
        print(f'{vendedor}: Total de vendas = R${total}. Média de vendas = R${media}')

def main(): #A função main() tem o objetivo de integrar todas as funções, controlando o fluxo do programa.
    vendas = coletar_vendas()
    relatorio = calcula(vendas)
    exibir = show_relatorio(relatorio)

if __name__ == "__main__":
    main()