# 13. Leia 5 (cinco) números inteiros e escreva o maior 
# e o menor deles. Considere que todos os valores são diferentes.


if __name__ == '__main__':
    n1 = int(input('Insira o número 1: '))
    n2 = int(input('Insira o número 2: '))
    n3 = int(input('Insira o número 3: '))
    n4 = int(input('Insira o número 4: '))
    n5 = int(input('Insira o número 5: '))

    menor = n1
    maior = n1

    if n2 > maior:
        maior = n2
    elif n2 < menor:
        menor = n2

    if n3 > maior:
        maior = n3
    elif n3 < menor:
        menor = n3

    if n4 > maior:
        maior = n4
    elif n4 < menor:
        menor = n4

    if n5 > maior:
        maior = n5
    elif n5 < menor:
        menor = n5

    print(f'\nMaior número: {maior}\nMenor número: {menor}')