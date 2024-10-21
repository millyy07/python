
#celsius para fahrenheit
def  celsius_fahrenheit(c):
    f = c * 1.8 + 32
    return  f

#celsius para kelvin
def celsius_kelvin(c):
    k = c + 273
    return k

#fahrenheit para celsius
def fahrenheit_celsius(f):
    c = (f - 32) / 1.8
    return c 

#fahrenheit para kelvin
def fahrenheit_kelvin(f):
    k = (f - 32) * 5 / 9 + 273
    return k

#kelvin para celsius
def kelvin_celsius(k):
    c = k - 273
    return c

#kelvin para fahrenheit
def kelvin_fahrenheit(k):
    f = (k - 273) * 1.8 + 32
    return f 

# Função principal
def conversor():
    print("conversor de temperaturas")
    while True:
        print("\n Escolha a operação :")
        print("1 - celsius para fahrenheit")
        print("2 - celsius para kelvin")
        print("3 - fahrenheit para celsius")
        print("4 - fahrenheit para kelvin")
        print("5 - kelvin para celsius")
        print("6 - kelvin para fahrenheit")
        print("0 - Sair")

        opcao = int(input("Digite o número da operação desejada: "))
        
        if opcao == 0:
            print("Conversor encerrada.")
            break
        
        if opcao in [1, 2, 3, 4, 5 , 6]:
            temperatura = float(input("Digite a temperatura: "))
        
        if opcao == 1:
            resultado = celsius_fahrenheit(temperatura)
            print(f"{temperatura}° C é igual a {resultado}° F")
        elif opcao == 2:
            resultado = celsius_kelvin(temperatura)
            print(f"{temperatura}° c é igual a {resultado}° k")
        elif opcao == 3:
            resultado = fahrenheit_celsius(temperatura)
            print(f"{temperatura}° f é igual a {resultado}° c")
        elif opcao == 4:
            resultado = fahrenheit_kelvin(temperatura)
            print(f"{temperatura}° f é igual a {resultado}° k")
        elif opcao == 5:
            resultado = kelvin_celsius(temperatura)
            print(f"{temperatura}° k é igual a {resultado}° c")
        elif opcao == 6:
            resultado = kelvin_fahrenheit(temperatura)
            print(f"{temperatura}° k é igual a {resultado}° f")
        else:
             print("opção invalida")
             continue


conversor()