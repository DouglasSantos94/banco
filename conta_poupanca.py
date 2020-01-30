from cliente import Cliente
from conta import Conta


class ContaPoupanca(Conta):
    __total_contas = 0

    def __init__(self, titular: Cliente, saldo: float, limite=0):
        super().__init__(titular, saldo, limite)
        ContaPoupanca.incrementa_total_contas()

    @classmethod
    def incrementa_total_contas(cls):
        cls.__total_contas += 1

    def atualiza(self, taxa):
        taxa_total = taxa * 3
        super().atualiza(taxa_total)
        return self.saldo * taxa_total
