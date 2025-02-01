class Veiculo():
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

    def exibir_info(self):
        print(f'O veículo {self.modelo} é da marca {self.marca} e do ano {self.ano}')

exibir_info = Veiculo('Cruze', 'Chevrolet', '2015')
exibir_info.exibir_info()
