# Determinar o número de colaboradores
colaboradores = int(input("Informe o número de colaboradores: "))

# Definir os dias da semana
segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

contador = 1

# Utilizei o while para evitar código maior e repetitivo
while contador <= colaboradores:
    voto = input(f"Colaborador {contador} Informe o dia da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ").lower()
    if voto == "segunda-feira":
        segunda += 1
    elif voto == "terça-feira":
        terca += 1
    elif voto == "quarta-feira":
        quarta += 1
    elif voto == "quinta-feira":
        quinta += 1
    elif voto == "sexta-feira":
        sexta += 1
    else:
        print("Dia inválido! Tente novamente.")
        continue

    contador += 1

# Validação de qual dia da semana foi escolhida
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    escolhido = "segunda-feira"
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    escolhido = "terça-feira"
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    escolhido = "quarta-feira"
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    escolhido = "quinta-feira"
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    escolhido = "sexta-feira"
else:
    escolhido = "empate"
print(f"\nO dia escolhido pelos colaboradores é: {escolhido}")

# OBS: Aqui me deparo com dificuldades de codificar o exercício por certas desculpas kkkkkk. Para me auxiliar utilizei alguns IA's e me fiz questão de reescrever letra por letra e tentar decifrar os códigos. Espero que desta maneira funcione legalmente.