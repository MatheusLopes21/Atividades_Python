def encontrar_maior_numero():
    maior_numero = None
    while True:
        numero = int(input("Digite um número inteiro (digite 0 para encerrar): "))
        if numero == 0:
            break
        if maior_numero is None or numero > maior_numero:
            maior_numero = numero
    return maior_numero

maior = encontrar_maior_numero()
if maior is not None:
    print("O maior número digitado foi:", maior)
else:
    print("Nenhum número foi digitado.")
