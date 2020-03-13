# Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:
# R + S / 2 onde 
#
# R = (A + B)²
# S = (B + C)²

a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o último número: '))

r = (a + b) ** 2
s = (b + c) ** 2

expr = (r + s) / 2

print('O resultado da expressão é: ', expr)