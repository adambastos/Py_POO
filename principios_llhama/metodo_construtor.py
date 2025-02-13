class adam():
    def __init__(self): #O método construtor é onde ficam os atributos
        self.nome = 'Adam' #Definindo os atributos
        self.idade = 26
        self.altura = 1.80
    
    def metodo2(self):
        print(self.nome) #Posso usar os atributos do método construtor dentro de outros métodos
    
    def soma(self, num1, num2):
        self.metodo2() #Eu posso utilizar um método dentro de outro método, também.
        print(num1 + num2)


adam_carac = adam() #Só de você instanciar o objeto da classe, o método construtor já chamado automaticamente, precisa nem chamar o método diretamente.
print(adam_carac.nome) #Usando os atributos fora do método

adam_carac.soma(5, 4)