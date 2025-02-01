class Fodase() :
    def fazer(self) -> None:
        print('Estou fazendo algo')

class Naofodase(Fodase):
    def naofazer(self) -> None:
        print('Não estou fazendo')

nofuedase = Naofodase()
nofuedase.fazer()