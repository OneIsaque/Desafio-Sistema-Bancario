import config as con

def menu():
    titulo = "Menu"
    print(titulo.center(60, "="))
    print(
        "1. Depositar\n"
        "2. Sacar\n"
        "3. Extrato\n"
        "4. Novo usuário\n"
        "5. Nova conta\n"
        "6. Listar contas\n"
        "7. Sair\n"
    )

def main():
    saldo = 0.0
    extrato = ""
    numero_saques = 0

    usuarios = []
    contas = []

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                valor = float(input("Valor do depósito: R$"))
            except ValueError:
                print("Entrada inválida.")
                continue
            saldo, extrato = con.deposito(saldo, valor, extrato)

        elif opcao == "2":
            try:
                valor = float(input("Valor do saque: R$"))
            except ValueError:
                print("Entrada inválida.")
                continue

            saldo_anterior = saldo
            saldo, extrato = con.saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=con.LIMITE_SAQUE_POR_OPERACAO,
                numero_saques=numero_saques,
                limite_saques=con.LIMITE_SAQUES_DIARIOS
            )
            if saldo < saldo_anterior:
                numero_saques += 1  # incrementa apenas quando o saque efetiva

        elif opcao == "3":
            con.exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            con.criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = con.criar_conta(con.AGENCIA_PADRAO, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            con.listar_contas(contas)

        elif opcao == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
