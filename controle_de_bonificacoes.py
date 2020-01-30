class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self.__total_bonificacoes = total_bonificacoes

    def registra(self, funcionario):
            self.__total_bonificacoes += funcionario.bonificacao()

    @property
    def total_bonificacoes(self):
        return self.__total_bonificacoes

