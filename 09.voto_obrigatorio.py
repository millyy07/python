#voto obrgatório
#leia a idade da pessoa e verefique se seu voto é obrigatório

nome =input("digite seu nome:")
idade = float(input("digite sua idade:"))

if(idade >= 18 and idade <= 64):
    print(nome, "seu voto é obrigatório")
else:
    print(nome, "seu voto não é obrigatório")



