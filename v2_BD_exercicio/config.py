# Parâmetros gerais
AGENCIA_PADRAO = "0001"
LIMITE_SAQUE_POR_OPERACAO = 500
LIMITE_SAQUES_DIARIOS = 3

# ------- Operações financeiras -------

def deposito(saldo, valor, extrato, /):
    """Depósito: argumentos apenas por posição. Retorna saldo e extrato."""
    if valor <= 0:
        print("Valor de depósito inválido.")
        return saldo, extrato

    saldo += valor
    extrato += f"Depósito: R${valor:.2f}\n"
    print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Saque: argumentos apenas por nome. Retorna saldo e extrato.
    A função valida limites, mas não altera 'numero_saques'.
    """
    if numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")
        return saldo, extrato

    if valor <= 0:
        print("Valor de saque inválido.")
        return saldo, extrato

    if valor > limite:
        print(f"Limite por saque excedido (máx R${limite:.2f}).")
        return saldo, extrato

    if valor > saldo:
        print("Saldo insuficiente.")
        return saldo, extrato

    saldo -= valor
    extrato += f"Saque:    R${valor:.2f}\n"
    print("Saque realizado com sucesso.")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    """Extrato: saldo por posição; extrato por nome (exibição)."""
    print("\n=== EXTRATO ===")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato.rstrip())
    print(f"\nSaldo atual: R${saldo:.2f}")
    print("==============\n")


# ------- Usuários e contas -------

def filtrar_usuario(cpf, usuarios):
    """Retorna o usuário (dict) com o CPF informado, ou None."""
    usuarios_filtrados = [u for u in usuarios if u["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario(usuarios, /):
    """Cria usuário garantindo CPF único."""
    cpf = input("CPF (somente números): ").strip()
    if filtrar_usuario(cpf, usuarios):
        print("Usuário já cadastrado com esse CPF.")
        return

    nome = input("Nome completo: ").strip()
    data_nasc = input("Data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ").strip()

    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nasc,
        "endereco": endereco
    })
    print("Usuário criado com sucesso.")


def criar_conta(agencia, numero_conta, usuarios, /):
    """
    Cria conta vinculada a um usuário existente.
    Retorna o dict da conta ou None.
    """
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        return None

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    print(f"Conta criada com sucesso: ag {agencia} conta {numero_conta}.")
    return conta


def listar_contas(contas, /):
    """Lista contas cadastradas."""
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    print("\n=== CONTAS ===")
    for c in contas:
        print(f"Agência: {c['agencia']} | Conta: {c['numero_conta']} | Titular: {c['usuario']['nome']} (CPF {c['usuario']['cpf']})")
    print("==============\n")
