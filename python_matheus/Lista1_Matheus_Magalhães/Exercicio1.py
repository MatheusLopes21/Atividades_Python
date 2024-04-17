def calcular_soma():
    sequencia = int(input("Digite o tamanho da sequência de números que você deseja somar: "))
    soma = 0
    for n in range(sequencia):
        numero = float(input(f"Digite o {n+1}º número: "))
        soma += numero
    return soma

resultado = calcular_soma()
print("A soma dos números digitados é:", resultado)
