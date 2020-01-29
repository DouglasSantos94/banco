from conta import Cliente, Conta
from gerente import Gerente

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