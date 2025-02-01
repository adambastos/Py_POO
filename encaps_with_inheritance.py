class Pessoa:
    def __init__(self, nome, cpf: int):
        self.nome = nome
        self.cpf = cpf
        
    def existir(self):
        print(f'O estudante {self.nome} existe com o CPF {self.cpf}')

    def _dormir(self) -> None: #Deixando o método com apenas um _ você o torna protegido, ou seja, ele só acessível dentro da própria classe e dentro de classes filhas
        print('A pessoa está dormindo')

class Aluno(Pessoa): 
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
    
    def assistir_aula(self):
        print('O aluno está assistindo a aula.')

student = Aluno('Adam', '05952172148')
student._dormir()