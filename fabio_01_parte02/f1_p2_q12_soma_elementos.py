# Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem

n = int(input('Insira um número de 4 dígitos: '))

n1 = n // 1000
resto = n % 1000

n2 = resto // 100
resto = resto % 100

n3 = resto // 10
n4 = resto % 10

soma = n1 + n2 + n3 + n4

print(f'"{n}" -> {n1}+{n2}+{n3}+{n4} = {soma}')