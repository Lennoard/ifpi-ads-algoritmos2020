# Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.

n = int(input('Insira um número inteiro de 3 dígitos: '))

c = n // 100
d = (n % 100) // 10
u = n % 10

n_inverso = (u * 100) + (d * 10) + c

print(f'A diferença entre {n} e seu reverso ({n_inverso}) é {n - n_inverso}')