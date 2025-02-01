class Pessoa():
    def __init__(self, cpf):
        self.nome = 'Adam'
        self.idade = 26
        self.__cpf = cpf #Adicionamos também o __ na frente do atributo que não pode ser acessado fora da nossa classe.

    def apresentar(self):
        print('Olá, meu nome é {} e tenho {} anos.'.format(self.nome, self.idade))
        self.__andar() #Eu quero que meu método andar possa ser utilizado pelo método apresentar, mas que não fique visível para outras pessoas.
    
    def __coletar_documento(self): #Quando eu adiciono __ na frente do nome do método, ele se torna privado, visível apenas dentro da própria classe.
        print('Eu estou andando.')

pessoa = Pessoa()
pessoa.apresentar() #Como dentro do método apresentar() já possui um print, eu não preciso utilizar o print aqui fora 
pessoa.__coletar_documento() 



#UML
'''
Encapsulamento

+altura: float /  #O + significa que o atributo é público
-cpf: string /  #O - significa que o atributo é privado

'''

