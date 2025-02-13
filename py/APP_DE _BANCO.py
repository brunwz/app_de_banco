menu ="""
******************
[d] Depósito
[e] Extrato
[s] Saque
[q] Sair
******************
=>"""

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        
        print("**** Opção Depósito ****")
        valor = (float (input("Por favor insira o valor de depósito: ")))
        
        if valor <= 0:
            print("Não é possível depositar um valor menor que 0")

        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
    elif opcao == "e":
        
        print("**** Opção Extrato ****")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        
    elif opcao =="s":
        
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "q":
        print("Operação cancelada") 
        break

else:
    print("Operação inválida, por favor insira uma opção disponível")
