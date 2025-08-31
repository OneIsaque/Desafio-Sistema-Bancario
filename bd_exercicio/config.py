# Operação de deposito
LIMITE_SAQUE_UNICO = 500
LIMITE_SAQUES_DIARIOS = 3


def deposito(valor, saldo):
    saldo += valor
    print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    return saldo


# Operação de saque
def limite_saque(valor):
    limite = 500
    if valor > limite:
        print("Limite de saque de R$500 excedido.")
        return False
    return True


def saque(valor_para_saque, valor_disponivel, num_saques_realizados):

    if num_saques_realizados >= LIMITE_SAQUES_DIARIOS:
        print("Limite de saques diários atingido.")
    
    if valor_para_saque > valor_disponivel:
        print("Saldo insuficiente.")
        return False
    
    if valor_para_saque > LIMITE_SAQUE_UNICO:
        return False
    
    print("Saque realizado com sucesso.")
    return True


# Operação de extrato
    #Listar depositos e saques anteriores
def extrato(saldo, saque, depositos):
    print("\n=== EXTRATO ===")
    if not depositos and saque == 0:
        print("Não foram realizadas movimentações.")
    else:
        for i, valor in enumerate(depositos, start=1):
            print(f"Depósito {i}: R${valor:.2f}")
        if saque > 0:
            print(f"Saque: R${saque:.2f}")
    print(f"\nSaldo atual: R${saldo:.2f}")
    print("================\n")
    

def controle_saques_diarios():
    limite = 0
    if limite >= 3:
        print("Limite de saque atingido.")
        return True
    else:
        limite += 1
        return False
    

def menu():
    t1 = "Menu"
    print(t1.center(22, "="))
    
    print('''
    1. Depositar
    2. Sacar
    3. Extrato
    4. Sair
    ''')

