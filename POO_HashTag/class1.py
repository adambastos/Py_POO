class Pessoa:
    def __init__(self):
        self.nome = 'Adam'
        self.idade = 26 

    def muda_nome(self, novo_nome):
        self.nome = novo_nome #self.canal refere-se ao atributo nome presente na classe do método principal __init__

pessoa = Pessoa()
print(pessoa.nome)
pessoa.muda_nome('João')
print(pessoa.nome)

