from time import sleep  # <- Acho legalzinho :P

menu = """
    ______________________________
    |          Banco V1          |    
    | [D] Depósito               |
    | [S] Saque                  |
    | [E] Extrato                |
    | [Q] Sair                   |
    |____________________________|"""

saldo = 0
limite = 500
extrato = "Extrato\n"
numero_saques = 0
LIMITE_SAQUES = 3
liberar_saque = True
escolha = True
run = True

while run:
    while escolha:
        print(menu)
        opcao = input(">").upper()
        if opcao not in ("D","S","E","Q"):
            print("Opção inválida, tente novamente.")
        else:
            escolha = False

    match opcao:
        case "D":
            while True:
                print("--Depósito--")
                deposito = float(input("Digite o valor a ser depositado: "))
                if deposito < 0:
                    print("Valor inválido. Tente novamente.")
                else:
                    saldo += deposito
                    print(f"Depósito de R$ {deposito} adicionado a conta.")
                    print(f"Novo saldo: R$ {saldo}")
                    extrato += f"Depósito: R${deposito}\n"
                    sleep(1)
                    print("Voltando ao menu...")
                    escolha = True
                    sleep(1)
                    break

        case "S":
            if saldo == 0:
                print("Sem saldo para sacar. Voltando ao menu...")
                liberar_saque = False
                escolha = True
            elif numero_saques == LIMITE_SAQUES:
                print("Limite de saques diarios atigindo.")
                sleep(1)
                print("Voltando ao menu...")
                sleep(1)
                liberar_saque = False
                escolha = True
            else:
                liberar_saque = True

            while liberar_saque:
                while True:
                    print("--Saque--")
                    saque = float(input("Digite o valor a ser sacado (-1 para sair): "))
                    if saque == -1:
                        print("Voltando ao menu...")
                        liberar_saque = False
                        sleep(1)
                        break
                    elif saque < -1:
                        print("Valor inválido. Tente novamente.")
                    elif saldo - saque < 0:
                        print("Saldo insuficiente para saque, tente outro valor.")
                    elif saque > limite:
                        print("O valor máximo por saque é de R$ 500,00. Tente novamente.")
                    else:
                        break
                if saque == -1:
                    break
                else:
                    saldo -= saque
                    extrato += f"Saque: R${saque}\n"
                    print(f"Saque de R$ {saque} realizado.")
                    print(f"Novo saldo: R$ {saldo}")
                    numero_saques += 1
                    sleep(1)
                    print("Voltando ao menu...")
                    sleep(1)
                    escolha = True
                    break

        case "E":
            print("--Extrato--")
            print(extrato)
            print(f"Saldo: {saldo}")
            while True:
                sair = input("Digite S para sair: ").upper()
                if sair == "S":
                    escolha = True
                    break

        case "Q":
            print("Finalizando...")
            sleep(1)
            run = False










