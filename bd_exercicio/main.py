import config as con
import time
import os

def main():
    saldo = 0
    saque = 0
    depositos = []
    num_saques = 0

    while True:
        con.menu()
        opcao = input("Escolha uma opção: ")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        
        
        if opcao == "1":
            valor = float(input("Digite o valor do depósito: R$"))
            saldo = con.deposito(valor, saldo)
            depositos.append(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: R$"))
            if con.saque(valor, saldo, num_saques):
                saldo -= valor
                saque += valor
                num_saques += 1
        elif opcao == "3":
            con.extrato(saldo, saque, depositos)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()