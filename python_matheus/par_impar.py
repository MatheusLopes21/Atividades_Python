numero = float(input("Digite um número para saber se é Impar ou Par: "))
resto = numero % 2

if resto == 0:
    if (numero < 100):
     print('O número é par ')
else:
    print('Este número é Impar')