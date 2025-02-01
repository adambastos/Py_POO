class GandS:
    def __init__(self) -> None:
        self.__valor = None
    
    def setter(self, valor: int) -> None: # -> None apenas indica que o método modifica um estado interno do objeto, mas não tem um retorno explícito.
        self.__valor = valor
    
    def getter(self) -> int:
        return self.__valor

ges = GandS()

ges.setter(25)
valor = ges.getter()
print(valor)


