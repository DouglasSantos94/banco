class Cliente:
    __slots__ = ['__nome', '__cpf']

    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf

    def __str__(self):
        return 'Instância de {}; endereço: {}'.format(self.__class__.__name__, id(self))

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
