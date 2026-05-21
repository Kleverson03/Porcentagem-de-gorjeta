def calcular_gorjeta():
    try:
        # 1. TRATAMENTO DE ENTRADA (Trata vírgula por ponto)
        valor_conta_str = input("Digite o valor da conta (ex: 150.50): ").replace(',', '.')
        valor_conta = float(valor_conta_str)
        
        porcentagem_gorjeta = float(input("Qual a porcentagem de gorjeta? (ex: 10, 15, 20): "))
        
        quant_pessoas = int(input("Quantas pessoas vão dividir a conta? "))

        # Validação para impedir divisão por zero pessoas
        if quant_pessoas <= 0:
            print("\n[ERRO] A quantidade de pessoas deve ser pelo menos 1.")
            return

        # 2.  LÓGICA DE CÁLCULO UNIFICADA
        # Esse cálculo funciona para 10, 20, 30 ou QUALQUER outra porcentagem
        total_com_gorjeta = valor_conta + (valor_conta * (porcentagem_gorjeta / 100))
        valor_por_pessoa = total_com_gorjeta / quant_pessoas

        # 3. APRESENTAÇÃO FORMATADA (:.2f deixa o dinheiro com duas casas decimais)
        print(f"\nTotal com gorjeta: R$ {total_com_gorjeta:.2f}")
        print(f"Cada pessoa pagará: R$ {valor_por_pessoa:.2f}")

        # 4. SALVANDO NO LOG LOCAL
        with open("historico_gorjetas.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Conta: R$ {valor_conta:.2f} | Gorjeta: {porcentagem_gorjeta}% | Pessoas: {quant_pessoas} | Por pessoa: R$ {valor_por_pessoa:.2f}\n")
        
        print("[+] Resultado salvo no arquivo 'historico_gorjetas.txt'!")

    # Se digitarem letras onde deveria ser número
    except ValueError:
        print("\n[ERRO] Entrada inválida! Certifique-se de digitar números válidos.")


calcular_gorjeta()