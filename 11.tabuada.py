# tabuada interativa: crie um programa que imprima a tabuada de um numero fornecido pelo usuário usando um loop while
contador = 0
numero = int(input("digite um valor da tabuada: "))

while (contador <= 10):
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
