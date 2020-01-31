from cliente import Cliente
from conta import Conta


class ContaCorrente(Conta):
    __total_contas = 0

    def __init__(self, titular: Cliente, saldo: float, limite=1000):
        super().__init__(titular, saldo, limite)
        ContaCorrente.incrementa_total_contas()

    @classmethod
    def incrementa_total_contas(cls):
        cls.__total_contas += 1

    def atualiza(self, taxa, fator_de_aumento=2):
        super().atualiza(taxa, fator_de_aumento)
        return self.saldo

    def deposita(self, valor):
        valor_final = valor - 0.1
        self.saldo += valor_final
        self.historico.transacoes.append(
            'Depósito realizado no valor de R${:.2f}'.format(valor))
