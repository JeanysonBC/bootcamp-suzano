def main():
    saldo = 0.0
    extrato = []
    saques_realizados = 0
    LIMITE_SAQUES = 3
    LIMITE_POR_SAQUE = 500.0

    menu = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

    while True:
        opcao = input(menu).strip().lower()

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: R$ "))
            
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Falha na operação! O valor informado é inválido.")

        elif opcao == 's':
            if saques_realizados >= LIMITE_SAQUES:
                print("Falha na operação! Limite diário de saques atingido.")
                continue

            valor = float(input("Informe o valor do saque: R$ "))

            if valor > LIMITE_POR_SAQUE:
                print(f"Falha na operação! O valor máximo por saque é R$ {LIMITE_POR_SAQUE:.2f}.")
            elif valor > saldo:
                print("Falha na operação! Saldo insuficiente.")
            elif valor > 0:
                saldo -= valor
                extrato.append(f"Saque:    R$ {valor:.2f}")
                saques_realizados += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Falha na operação! O valor informado é inválido.")

        elif opcao == 'e':
            print("\n================ EXTRATO ================")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                for movimento in extrato:
                    print(movimento)
            print(f"\nSaldo atual: R$ {saldo:.2f}")
            print("=========================================")

        elif opcao == 'q':
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()