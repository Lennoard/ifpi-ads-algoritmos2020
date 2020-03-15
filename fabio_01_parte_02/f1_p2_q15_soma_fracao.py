# Leia 2 (duas) frações (numerador e denominador), calcule e escreva 
# a soma destas frações, escrevendo o resultado em forma de fração.

num1 = int(input('Insira o numerador da primeira fração: '))
den1 = int(input('Insira o denominador da primeira fração: '))

num2 = int(input('Insira o numerador da segunda fração: '))
den2 = int(input('Insira o denominador da segunda fração: '))

den = den1 * den2
num = ((den / den1) * num1) + ((den / den2) * num2)

print(f'{num1}/{den1} + {num2}/{den2} = {num}/{den}')