class Banco:
    def __init__(self):
        self.__lista_contas = []

    @property
    def lista_contas(self):
        return self.__lista_contas

    @lista_contas.setter
    def lista_contas(self, lista):
        self.__lista_contas = lista

    def adiciona(self, conta):
        self.lista_contas.append(conta)

    def pega_conta(self, posicao):
        try:
            print(self.lista_contas[posicao])
        except IndexError:
            print('Posição não existente!')

    def pega_total_contas(self):
        return len(self.lista_contas)

