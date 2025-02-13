class Pessoa:
    def __init__(self, nome, cpf: int):
        self.nome = nome
        self.cpf = cpf
        
    def existir(self):
        print(f'O estudante {self.nome} existe com o CPF {self.cpf}')

class Aluno(Pessoa): #Aqui eu estou dizendo que a nova classe Aluno está herdando atributos e métodos da classe Pessoa
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf) #Método super() permite que Aluno herde corretamente os atributos e comportamentos de Pessoa, evitando a necessidade de reescrever o código da classe base.
    
student = Aluno('João', '05952172148')
student.existir()

 
