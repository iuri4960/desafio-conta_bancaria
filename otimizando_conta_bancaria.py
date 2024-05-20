import textwrap

def menu():
    menu = '''\n
    -----------------MENU-----------------
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtratp
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
    else:
            print("Operação falhou! O valor informado é inválido. ")
    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = saque > saldo
    excedeu_limite = saque > limite 
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Você não tem saldo suficiente")
        
    elif excedeu_limite:
        print("Limite de saque excedido")

    elif excedeu_saques:
        print("Número máximo de saques excedido")

    elif saque > 0:
        saldo -= saque
        extrato += f'Saque:\t\tR$ {saque:.2f}\n'
        numero_saques += 1

    else:
        print("Operação falhou! Valor informado é inválido")
    
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n######## EXTRATO ########")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print("#########################")

def criar_usuario(usuarios):
    cpf = input("digite o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("já existe usuário com esse CPF")
        return
    nome = input("nome completo: ")
    data_nascimento = input("data de nascimento(dd--mm--aaaa): ")
    endereco = input("informe o endereço(logradouro, número - bairro- cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
    print("usuário criado")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("digite o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("conta criada")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print(" usuário não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        '''
        print("=" * 100)
        print(textwrap.dedent(linha))    

def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()
        
        if opcao == 'd':
            valor = float(input("informe o valor de depósito: "))
            saldo, extrato= depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            saque = float(input("informe o valor de saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=saque, extrato=extrato, limite= limite, numero_saques=numero_saques, limite_saque=LIMITE_SAQUES,)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta =len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
        else:
            print("opreção inválida, tente outra opção")

main()