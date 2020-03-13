# Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, 
# ponto1 (x1,y1) e ponto2 (x2,y2), escreva a distância entre eles, conforme fórmula abaixo.
# d = √(x2 - x1)² + (y2 - y1)²

separador = '=========================================='

print(f'{separador}\nInsira a coordenadas do primeiro ponto')
x1 = float(input('x: '))
y1 = float(input('y: '))

print(f'{separador}\nInsira as coordenadas do segundo ponto')
x2 = float(input('x: '))
y2 = float(input('y: '))

calc = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
d = calc ** (1 / 2) # -> (2)√calc¹

print(f'{separador}\nA distância dos pontos ({x1}, {y1}) e ({x2}, {y2}) é {d}')

