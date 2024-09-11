

print("Olá! vamos ver qual será sua média")

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a primeira nota: "))
nota3 = float(input("digite a primeira nota: "))
nota4 = float(input("digite a primeira nota: "))

media =(nota1 + nota2 + nota3 + nota4) /4

print("A média final obtida: ", media)

if(media >= 80):
     print("Aluno aprovado!!!")
else:
     print("Aluno reprovado!!!")