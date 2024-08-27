#IMC= recebe peso e altura apresente no final o IMC e a classificação

peso = float(input("digite seu peso (em kg): "))
altura = float(input("digite sua altura (em metros): "))
imc = peso / (altura * altura)

print(f"seu imc é {imc:.2f}.")

if(imc < 18.5):
    print("abaixo do peso")
elif(imc < 25):
    print("peso normal")
elif(imc < 30 ):
    print("sobrepeso")
else:
    print("obesidade")