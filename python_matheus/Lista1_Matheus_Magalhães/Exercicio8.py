def imprimir_retangulo(largura, altura):
    for i in range(altura):
        print('#' * largura)


largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))


imprimir_retangulo(largura, altura)
