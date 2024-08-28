# algoritmo do ano bissexto
# o usuário digitará o ano e o programa informará se o ano é ou nao é bissexto
# regras do ano bissexto
# - o ano deve ser múltiplo de 4
# - o ano nao deve ser múltiplo de 100
# - exceto anos múltiplo de 400


ano = int(input("digite o ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"o ano {ano} é bissexto")
else:
    print(f"o ano {ano} não é bissexto")