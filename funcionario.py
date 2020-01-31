from abc import ABC, abstractmethod


class Funcionario(ABC):
    __slots__ = ['__salario', '__cpf', '__nome']

    def __init__(self, nome, cpf, salario):
        self.__salario = salario
        self.__cpf = cpf
        self.__nome = nome

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.salario = salario

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @abstractmethod
    def bonificacao(self):
        pass
