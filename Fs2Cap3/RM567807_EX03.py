# Entrada do valor da dívida
valor_divida = float(input("Digite um valor da dívida: "))

# Definição das opções de parcelamento
parcelas_opcoes = [1, 3, 6, 9, 12]

# Processamento para cada opção ded parcelamento
for parcelas in parcelas_opcoes:
    if parcelas == 1:
        percentual_juros = 0
    elif parcelas == 3:
        percentual_juros = 10
    elif parcelas == 6:
        percentual_juros = 15
    elif parcelas == 9:
        percentual_juros = 20
    elif parcelas == 12:
        percentual_juros = 25

    # Cálculos
    valor_juros = valor_divida * (percentual_juros / 100)
    total_divida = valor_divida + valor_juros
    valor_parcela = total_divida / parcelas

    # Resultado
    print(f"Total:R$ {total_divida:,.2f} Juros:R$ {valor_juros:,.2f} Número de parcelas:{parcelas} Valor da Parcela:R$ {valor_parcela:,.2f}")

# OBS: Acho que nesse exercício também poderia usar o dicionário como tabela_parcelas.