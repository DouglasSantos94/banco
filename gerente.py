from funcionario import Funcionario


class Gerente(Funcionario):

    __slots__ = ['__senha', '__num_funcionarios']

    def __init__(self, nome, cpf, salario, senha, num_funcionarios):
        super().__init__(nome, cpf, salario)
        self.__senha = senha
        self.__num_funcionarios = num_funcionarios

    @property
    def senha(self):
        return self.__senha

    @property
    def num_funcionarios(self):
        return self.__num_funcionarios

    def autentica(self, senha):
        if self.senha == senha:
            print('Acesso permitido!')
            return True
        print('Acesso negado!')
        return False

    def bonificacao(self):
        return self.salario * 0.15 #override do método bonificação
