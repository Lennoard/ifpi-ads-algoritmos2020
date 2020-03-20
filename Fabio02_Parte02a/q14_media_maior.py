# 14. Leia 5 (cinco) números inteiros, calcule a 
# sua média e escreva os que são maiores que a média.

def calcular_media_5(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5) / 5

def main():
    n1 = int(input('Insira o número 1: '))
    n2 = int(input('Insira o número 2: '))
    n3 = int(input('Insira o número 3: '))
    n4 = int(input('Insira o número 4: '))
    n5 = int(input('Insira o número 5: '))

    media = calcular_media_5(n1, n2, n3, n4, n5)

    print(f'================================\nNúmeros maiores que a média ({media}): ')
    if (n1 > media):
        print(n1)
    elif (n2 > media):
        print(n2)
    elif (n3 > media):
        print(n3)
    elif (n4 > media):
        print(n4)
    elif (n5 > media):
        print(n5)
    else:
        print('Nenhum número é maior que a média')


main()