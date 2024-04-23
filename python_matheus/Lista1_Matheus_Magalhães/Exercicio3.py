def verificar_condicao(numero):
    if (numero % 2 == 0 and numero > 10) or (numero % 2 != 0 and numero < 50):
        return "SIM"
    else:
        return "NAO"

try:
    N = int(input("Digite um número inteiro: "))
    resultado = verificar_condicao(N)
    print(resultado)
except ValueError:
    print("Por favor, digite um número inteiro válido.")