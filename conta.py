from historico import Historico
from cliente import Cliente


class Conta:
    __slots__ = ['__numero', '__titular', '__saldo', '__limite', '__historico']
    __total_contas = 0

    def __init__(self, titular: Cliente, saldo: float, limite=1000.0):
        self.__numero = Conta.total_contas()
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__historico = Historico()
        Conta.incrementa_total_contas()

    def __str__(self):
        return 'Objeto do tipo: {}\nAtributos: \nNumero: {}\nTitular: {}\nSaldo: {}\nLimite: {}\n'.format(
            self.__class__.__name__, self.numero, self.titular.nome, self.saldo, self.limite)

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def historico(self):
        return self.__historico

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @classmethod
    def total_contas(cls):
        return cls.__total_contas

    @classmethod
    def incrementa_total_contas(cls):
        cls.__total_contas += 1

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(
            'Depósito realizado no valor de R${:.2f}'.format(valor))

    def saca(self, valor):
        if self.saldo_suficiente(valor):
            self.saldo -= valor
            self.historico.transacoes.append(
                'Saque realizado no valor de: R${:.2f}'.format(valor))
            return True
        return False

    def extrato(self):
        print('Data de abertura da conta: {}\nNumero: {}'.format(
            self.historico.data_abertura, self.numero))
        print('Transações: ')
        transacoes = self.historico.imprime()
        print('{}Saldo: {}'.format(transacoes, self.saldo))

    def saldo_suficiente(self, valor):
        return self.saldo >= valor

    def transfere_para(self, conta_destino, valor):
        if self.saldo_suficiente(valor):
            conta_destino.saldo += valor
            self.historico.transacoes.append(
                'Transferência realizada para a conta número {} no valor de R${:.2f}'
                    .format(conta_destino.numero, valor))
            conta_destino.historico.transacoes.append(
                'Transferência recebida da conta número {} no valor de R${:.2f}'
                    .format(self.numero, valor))
        else:
            print('Saldo insuficiente!')

    def atualiza(self, taxa):
        rendimento = self.saldo * taxa
        self.saldo += rendimento
        return rendimento
