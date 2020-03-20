n1 = float(input('Insira a nota #1: '))
p1 = float(input('Insira o peso #1: '))

n2 = float(input('\nInsira a nota #2: '))
p2 = float(input('Insira o peso #2: '))

n3 = float(input('\nInsira a nota #3: '))
p3 = float(input('Insira o peso #3: '))

media_p = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3)

print(f'A media do aluno eeh {media_p}')