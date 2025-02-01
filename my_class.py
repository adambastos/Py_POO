class minhaclasse():
    def helloworld(self):
        print('Hello, World!')

myclass = minhaclasse() #Instanciando o objeto minhaclasse
myclass.helloworld()


class test_return():
    def retornando(self):
        idade = 26
        return idade

pegar_o_return = test_return()
response = pegar_o_return.retornando() #Guardando o retorno (return idade) na variável response.
print(response)
