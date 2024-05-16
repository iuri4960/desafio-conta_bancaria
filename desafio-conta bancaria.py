menu= '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        
        else:
            print("Operação falhou! O valor informado é inválido. ")

    elif opcao == 's':
        saque = float(input("Informe o valor de saque: "))

        excedeu_saldo = saque > saldo

        excedeu_limite = saque > limite 

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente")
        
        elif excedeu_limite:
            print("Limite excedido")

        elif excedeu_saques:
            print("Número máximo de saques excedido")

        elif saque > 0:
            saldo -= saque
            extrato += f'Saque: R$ {saque:.2f}\n'
            numero_saques += 1

        else:
            print("Operação falhou! Valor informado é inválido")
    

    elif opcao == 'e':
        print("\n######## EXTRATO ########")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print("#########################")
    elif opcao == 'q':
        break
    else:
        print("operação inválida, por favor selecione novamente a operação desejada  ") 