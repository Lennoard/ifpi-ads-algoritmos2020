# Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.

n1 = int(input('Insira o primeiro número binário: '))
n2 = int(input('Insira o segundo número binário: '))
n3 = int(input('Insira o terceiro número binário: '))
n4 = int(input('Insira o quarto número binário: '))

decimal = (n1 * (2 ** 3)) + (n2 * (2 ** 2)) + (n3 * (2 ** 1)) + (n4 * (2 ** 0))

print(decimal)