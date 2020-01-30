from atualizador_de_contas import AtualizadorDeContas
from conta import Cliente, Conta
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from controle_de_bonificacoes import ControleDeBonificacoes
from funcionario import Funcionario
from gerente import Gerente
'''
if __name__ == '__main__':
    cliente1 = Cliente('Douglas', '123')
    cliente2 = Cliente('Jaina', '456')
    cliente3 = Cliente('Mia', '789')

    conta1 = Conta(cliente1, 10000.0, 50000)
    conta2 = Conta(cliente2, 15000.0, 100000)
    conta3 = Conta(cliente3, 15000.0, 100000)
    gerente = Gerente('Nino', '354', 2000, '123', 15)

    conta1.deposita(20)

    conta2.deposita(50)
    conta1.saca(50)
    conta1.transfere_para(conta2, 500)
    conta1.extrato()
    conta2.extrato()
    conta3.extrato()
    print(gerente.senha)

if __name__ == '__main__':
    funcionario = Funcionario('João', '111111111-11', 2000.0)
    print("bonificacao funcionario: {}".format(funcionario.bonificacao()))

    gerente = Gerente("José", "222222222-22", 5000.0, '1234', 0)
    print("bonificacao gerente: {}".format(gerente.bonificacao()))

    controle = ControleDeBonificacoes()
    controle.registra(funcionario)
    controle.registra(gerente)

    print("total: {}".format(controle.total_bonificacoes))
'''

if __name__ == '__main__':
    cliente1 = Cliente('Douglas', '123')
    cliente2 = Cliente('Jaina', '456')
    cliente3 = Cliente('Mia', '789')
    cliente4 = Cliente('Nino', '134')

    c = Conta(cliente1, 1000.0)
    cc = ContaCorrente(cliente2, 1000.0)
    cp = ContaPoupanca(cliente3, 1000.0)
    cc2 = ContaCorrente(cliente4, 1500)

    #c.atualiza(0.01)
    ##cc.atualiza(0.01)
    #cp.atualiza(0.01)
    #cc.deposita(20)
    adc = AtualizadorDeContas(0.01)

    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)
    print(adc.saldo_total)
    #print(c.saldo)
    #print(cc.saldo)
    #print(cp.saldo)
