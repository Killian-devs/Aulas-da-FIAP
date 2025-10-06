print("Escolha o tipo de investimento:")
print("1. CDB")
print("2. LCI")
print("3. LCA")

tipo_investimento = int(input("Digite o tipo de investimento (1, 2 ou 3): "))
valor_resgate = float(input("Digite o valor a ser resgatado: "))
dias_investidos = int(input("Digite o número de dias que o valor permaneceu investido: "))

if tipo_investimento not in [1, 2, 3]:
    print("Tipo de investimento inválido! Digite 1, 2 ou 3.")
else:
    if tipo_investimento == 1:
        if dias_investidos <= 180:
            aliquota = 22.5
        elif dias_investidos <= 360:
            aliquota = 20.0
        elif dias_investidos <= 720:
            aliquota = 17.5
        else:
            aliquota = 15.0

        imposto = valor_resgate * (aliquota / 100)
        print(f"O valor do imposto de renda a ser pago é: R$ {imposto:.2f}")

    else:
        print("LCI e LCA são isentos de imposto de renda!")
        print(f"Não há imposto a pagar para o resgate de R$ {valor_resgate:.2f}")