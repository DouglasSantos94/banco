class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self.__total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        if hasattr(obj, 'bonificacao'):
            self.__total_bonificacoes += obj.bonificacao()
        else:
            print('Instância de {} não implementa o método bonificações'.format(self.__class__.__name__))

    @property
    def total_bonificacoes(self):
        return self.__total_bonificacoes

