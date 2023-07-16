def Menu():
    print("""
    <==========MENU==========>
    - [d]      Depositar
    - [s]      Sacar
    - [e]      Extrato
    - [nc]     Nova conta
    - [lc]     Lista contas
    - [nu]     Novo usuário
    - [q]      Sair
    <========================>
    """)
    while True:
        opcao = input("=> ").upper().strip()
        try:
            if opcao not in ("D", "S", "E", "NC", "LC", "NU", "Q"):
                print("Opção inválida, tente novamente.")
            elif not opcao.isalpha():
                print("Opção inválida, tente novamente.")
            else:
                break
        except ValueError:
            print("Opção inválida, tente novamente.")
    return opcao


def Depositar(saldo, extrato):
    print("<==========DEPOSITAR==========>")
    while True:
        try:
            valor = float(input("Valor a ser depósitado (-1 para sair): "))
            if valor == -1:
                print("Voltando ao menu...")
                return
            elif valor < -1:
                print("Valor inválido, tente novamente.")
            elif valor > 0:
                break
            else:
                print("Valor inválido, tente novamente.")
        except ValueError:
            print("Valor inválido, tente novamente.")
    saldo += valor
    extrato_atualizado = f"Deposito: R${valor}. Saldo: R$ {saldo}\n"
    print("<===DEPÓSITO REALIZADO COM SUCESSO!===>")
    return saldo, extrato+extrato_atualizado


def Sacar(*, saldo, extrato, limite, LIMITE_SAQUES, saques):
    if saldo == 0:
        print("Sem saldo para sacar, retornando ao menu...")
    elif saques >= LIMITE_SAQUES:
        print("Limite de saques diarios atingido, voltando ao menu...")
    else:
        print("<==========SAQUE==========>")
        while True:
            try:
                valor = float(input("Digite o valor a ser sacado (-1 para sair): "))
                if valor == -1:
                    print("Voltando ao menu...")
                    return
                elif valor < -1:
                    print("Valor inválido, tente novamente.")
                elif saldo - valor < 0:
                    print("Saldo insuficiente, tente novamente.")
                elif valor > limite:
                    print("É permitido somente saques de até 500 reais, tente novamente.")
                elif valor > 0 and saldo - valor >= 0 and valor <= limite:
                    break
                else:
                    print("Valor inválido, tente novamente.")
            except ValueError:
                print("Valor inválido, tente novamente.")
        saldo -= valor
        saques += 1
        extrato += f"Saque: R$ {valor}. Saldo: R$ {saldo}\n"
        print("<===SAQUE REALIZADO COM SUCESSO===>")
        return saldo, extrato, saques


def Extrato(saldo, /, *, extrato):
    print("<===EXTRATO===>\n")
    print(extrato)
    print(f"\nSaldo atual: {saldo}")
    while True:
        try:
            escolha = input("Digite 'S' para sair: ").upper().strip()
            if escolha == "S":
                print("Voltando ao menu...")
                return
            else:
                print("Valor inválido, tente novamente.")
        except ValueError:
            print("Valor inválido, tente novamente.")

def NovoUsuario(usuarios):
    while True:
        try:
            cpf = int(input("Digite o CPF (Somente números, -1 para sair): "))
            if cpf == -1:
                print("Voltando ao menu...")
                return
            elif cpf < -1:
                print("Valor inválido, tente novamente.")
            else:
                usuario = FiltrarCPF(cpf, usuarios)
                if usuario:
                    print("Usuário já existente, tente novamente com outro CPF.")
                    return
                elif usuario is None:
                    print("<===CADASTRO===>")
                    nome = input("Nome completo: ").strip()
                    data_nasc = input("Data de nascimento (DD-MM-AAAA): ").strip()
                    endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()

                    usuarios.append({
                        "nome": nome,
                        "data_nasc": data_nasc,
                        "cpf": cpf,
                        "endereco": endereco
                    })
                    print("<==Novo usuário criado com sucesso!===>")
                    return usuarios


        except ValueError:
            print("Valor inválido, tente novamente.")


def FiltrarCPF(cpf,usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def NovaConta(AGENCIA,usuarios,num_contas,contas):
    while True:
        try:
            cpf = int(input("Digite o CPF (Somente números, -1 para sair): "))
            usuario = FiltrarCPF(cpf, usuarios)
            if cpf == -1:
                print("Voltando ao menu...")
                return
            elif cpf < -1:
                print("Valor inválido, tente novamente.")
            else:
                if usuario:
                    num_contas += 1
                    print("Gerando nova conta...")
                    print("<===Conta gerada com sucesso!===>")

                    contas.append({
                        "agencia": AGENCIA,
                        "num_conta": num_contas,
                        "usuario": usuario
                    })
                    return contas,num_contas

                else:
                    print("Usuário não encontrado, tente novamente.\nVoltando ao menu...")
                    return
        except ValueError:
            print("Valor inválido, tente novamente.")

def ListarContas(contas,AGENCIA):
    print("<===CONTAS===>\n")
    for conta in contas:
        print(f"Agencia: {AGENCIA}\nConta: {conta['num_conta']}\nUsuário: {conta['usuario']['nome']}\n")
    while True:
        try:
            escolha = input("Digite 'S' para sair: ").upper().strip()
            if escolha == 'S':
                print("Voltando ao menu...")
                return
            else:
                print("Valor inválido, tente novamente.")
        except ValueError:
            print("Valor inválido tente novamente.")

def main():
    saldo = 0
    extrato = ""
    usuarios = []
    contas = []
    limite = 500
    saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    num_contas = 0

    while True:
        opcao = Menu()
        match opcao:
            case "D":
                saldo, extrato = Depositar(saldo, extrato)
            case "S":
                resultado = Sacar(saldo=saldo, extrato=extrato,saques=saques, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES)
                if resultado is not None:
                    saldo, extrato, saques = resultado

            case "E":
                Extrato(saldo, extrato=extrato)
            case "NC":
                resultado = NovaConta(AGENCIA,usuarios,num_contas,contas)
                if resultado is not None:
                    contas, num_contas = resultado
            case "LC":
                ListarContas(contas,AGENCIA)
            case "NU":
                resultado = NovoUsuario(usuarios)
                if resultado is not None:
                    usuarios = resultado
            case "Q":
                print("Finalizando...")
                break
main()



