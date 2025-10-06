op = -1
while op != 5:
    print("*\nMENU DO SUPER PROGRAMA MARAVILHOSO")
    print("1 - Rodar código 1")
    print("2 - Rodar código 2")
    print("3 - Rodar código 3")
    print("4 - Rodar código 4")
    print("5 - Sair do programa")
    op = int(input("*\nInforme sua opção: "))
    if op == 1:
        print("CÓDIGO 1 RODANDO!")
    elif op == 2:
        print("CÓDIGO 2 RODANDO!")
    elif op == 3:
        print("CÓDIGO 3 RODANDO!")
    elif op == 4:
        print("CÓDIGO 4 RODANDO!")
    elif op == 5:
        break
    else:
        print("DIGITE UMA OPÇÃO VÁLIDA!")
print("OK! O progrma está encerrado...")