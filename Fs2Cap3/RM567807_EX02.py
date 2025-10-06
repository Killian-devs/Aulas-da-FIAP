# Entrada do preço do carro
preco_carro = float(input("Digite o preço do carro: "))

# 20% de desconto
preco_vista = preco_carro * 0.80
print(f"O preço final à vista com desconto 20% é: {preco_vista:.1f}")

""" # Tabela de acréscimos utilizando dicionário
tabela_acrescimos = {
    6: 3, 12: 6, 18: 9, 24: 12, 30: 15,
    36: 18, 42: 21, 48: 24, 54: 27, 60: 30
} """
# OBS: Sei que a atividade é sobre IFs, mas eu podia utilizar dicionário para evitar excesso de linhas de código?

#Opções de parcelamento
parcelas_opcoes = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]

for parcelas in parcelas_opcoes:
    percentual = parcelas # se usar dicionário: percentual = tabela_acrescimos[parcelas]
    
# Determina o percentual de acréscimo usando if
for parcelas in parcelas_opcoes:
    if parcelas == 6:
        percentual = 3
    elif parcelas == 12:
        percentual = 6
    elif parcelas == 18:
        percentual = 9
    elif parcelas == 24:
        percentual = 12
    elif parcelas == 30:
        percentual = 15
    elif parcelas == 36:
        percentual = 18
    elif parcelas == 42:
        percentual = 21
    elif parcelas == 48:
        percentual = 24
    elif parcelas == 54:
        percentual = 27
    elif parcelas == 60:
        percentual = 30

    preco_final = preco_carro * (1 + percentual/100)
    valor_parcela = preco_final / parcelas

    print(f"O preço final parcelado em {parcelas} x é de R$ {preco_final:,.2f} com parcelas de R$ {valor_parcela:,.2f}")