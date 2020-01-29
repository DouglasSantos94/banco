from datetime import datetime


class Historico:
    def __init__(self):
        self.__data_abertura = datetime.today()
        self.__transacoes = []

    @property
    def data_abertura(self):
        return self.__data_abertura

    @property
    def transacoes(self):
        return self.__transacoes

    @transacoes.setter
    def transacoes(self, transacoes):
        self.__transacoes = transacoes

    def imprime(self):
        transacoes = ''
        for transacao in self.transacoes:
            transacoes += '- {}\n'.format(transacao)
        return transacoes
