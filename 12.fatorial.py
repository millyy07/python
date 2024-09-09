#calculadora de fatorial: criar um programa que calcule o fatorial de um numero fornecido pelo usuário usando um loop while

numero = int(input("digite um numero: "))
fatorial = 1
contador = 1

while (contador <= numero):
    fatorial *= contador # fatorial = fatorial * contador
    contador += 1  # contador = contador + 1 

print(f"o fatorial de {numero} é {fatorial}")
