# DESAFIO SISTEMA BANCÁRIO

saldo = 0
extrato = ""
LIMITE_SAQUE = 0

operacao = int(input(
    "Bem vindo, selecione uma das opções abaixo:\n1 - SAQUE\n2 - DEPOSITO\n3 - EXTRATO\nOpcão: "))

while operacao != 0:

    if operacao >= 0 and operacao <= 3:
        if operacao == 1:
            valor_saque = float(input("Insira o valor que deseja sacar: "))
            if valor_saque > saldo:
                while valor_saque > saldo:
                    print("Saldo insulficiente!")
                    operacao_saque = int(
                        input("DIGITE 8 - PARA VOLTAR OU 9 - PARA INSERIR UM NOVO VALOR DE SAQUE:"))
                    if operacao_saque == 8:
                        break
                    elif operacao_saque == 9:
                        valor_saque = float(
                            input("Insira o valor que deseja sacar: "))
            else:
                if LIMITE_SAQUE < 4:

                    saldo = saldo - valor_saque
                    extrato += f"Saque: R${valor_saque}\n"
                    print(f"\nSaque Realizado ! Seu saldo atual é: R${
                          saldo}\n\n")
                    LIMITE_SAQUE = LIMITE_SAQUE+1
                else:
                    print("\nSaque não realizado ! limite de saque atingido!\n")
        elif operacao == 2:
            valor_deposito = float(input("Insira o valor a ser depositado: "))
            while valor_deposito < 0:
                print("Valor invalido: ")
                valor_deposito = float(
                    input("Insira o valor a ser depositado: "))
            saldo = valor_deposito + saldo
            extrato += f"Deposito: R$ {valor_deposito:.2f}\n"
            print(f"\nDeposito realizado! Seu saldo atual é de: R${saldo}\n\n")
        elif operacao == 3:
            if extrato == "":
                print("Não há movimentações registradas!")
                print("Não foram realizadas movimentações." if not extrato else extrato)
            else:
                print(extrato)
                print(f"\nSaldo atual R${saldo}\n")
    operacao = int(input(
        "Bem vindo, selecione uma das opções abaixo:\n1 - SAQUE\n2 - DEPOSITO\n3 - EXTRATO\n0 - SAIR\nOpcão: "))
