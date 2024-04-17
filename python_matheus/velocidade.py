velocidade = float(input("Digite a velocidade do carro em km/h: "))

limite_velocidade = 80
valor_multa_por_km = 5

if velocidade > limite_velocidade:
    excesso_velocidade = velocidade - limite_velocidade
    valor_multa = excesso_velocidade * valor_multa_por_km
    
    print(f"Você foi multado! Velocidade excedida: {excesso_velocidade} km/h")
    print(f"Valor da multa a pagar: R${valor_multa:.2f}")
else:
    print("Você está dentro do limite de velocidade. Dirija com segurança!")
