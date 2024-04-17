numero = float(input("Digite um número para saber se é Impar ou Par: "))
resto = numero % 2

if resto == 0:
    if (numero < 100):
        print('O número é par e menor que 100')
    else:
        print('O número é par e maior ou igual que 100')
else: 
    if (numero < 100):
        print("O número é impar e menor que 100")
    else:
        print("O número é impar e maior ou igual a 100")