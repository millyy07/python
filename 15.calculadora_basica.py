print("CALCULADORA DAS OPERAÇÕES BÁSICAS ")
print("menu de escolha: ")
# Função para somar dois números
def somar(num1, num2):
    return num1 + num2

# Função para subtrair dois números
def subtrair(num1, num2):
    return num1 - num2

# Função para multiplicar dois números
def multiplicar(num1, num2):
    return num1 * num2

# Função para dividir dois números
def dividir(num1, num2):
    if num2 == 0:
        return "Erro! Divisão por zero."
    return num1 / num2

# Função principal
def calculadora():
    print("Calculadora Básica")
    while True:
        print("\nEscolha a operação:")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")

        opcao = int(input("Digite o número da operação desejada: "))
        
        if opcao == 0:
            print("Calculadora encerrada.")
            break
        elif opcao < 0 or opcao > 4:
            print("Opção inválida. Escolha uma opção válida.")
            continue
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            resultado = somar(num1, num2)
        elif opcao == 2:
            resultado = subtrair(num1, num2)
        elif opcao == 3:
            resultado = multiplicar(num1, num2)
        elif opcao == 4:
            resultado = dividir(num1, num2)

        print(f"O resultado da operação é: {resultado}")

# Chamando a função principal
calculadora()