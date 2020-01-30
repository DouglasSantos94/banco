class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0):
        self.__selic = selic
        self.__saldo_total = saldo_total

    @property
    def selic(self):
        return self.__selic

    @property
    def saldo_total(self):
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self, novo_saldo):
        self.__saldo_total = novo_saldo

    def roda(self, conta):
        print('Saldo anterior: R${:.2f}'.format(conta.saldo))
        self.saldo_total += conta.atualiza(self.selic)
        print('Saldo atual: R${:.2f}'.format(conta.saldo))
