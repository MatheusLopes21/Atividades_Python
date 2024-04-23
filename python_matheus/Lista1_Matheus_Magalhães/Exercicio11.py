soma = 0
qtd = 0
media = 0
maior = None
menor = None
soma_par = 0
qtd_par = 0
qtd_impar = 0

while True:
   num = float(input("Digite um número ou 30000 para sair: "))
   if num == 30000:
       break
   soma += num
   qtd += 1

   if maior is None or num > maior:
       maior = num

   if menor is None or num < menor:
       menor = num

   if num % 2 == 0:
       soma_par += num
       qtd_par += 1

   else:
       qtd_impar += 1

if qtd > 0:
   media = soma / qtd

print(f"Soma dos números digitados: {soma}")

print(f"Quantidade de números digitados: {qtd}")

print(f"Média dos números digitados: {media:.2f}")

print(f"Maior número digitado: {maior}")

print(f"Menor número digitado: {menor}")

if qtd_par > 0:
   media_par = soma_par / qtd_par

   print(f"Média dos números pares: {media_par:.2f}")

if qtd > 0:
   perc_impar = (qtd_impar / qtd) * 100

   print(f"Porcentagem dos números ímpares: {perc_impar:.2f}%")