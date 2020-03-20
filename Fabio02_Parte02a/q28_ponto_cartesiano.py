# Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de
# um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área
# não pode ser negativo.


def calcular_distancia(a, b):
    if a > b:
        return a - b
    return b - a


if __name__ == '__main__':
    print('=== PRIMEIRO PONTO CARTESIANO ===')
    xa = int(input('Insira o x: '))
    ya = int(input('Insira o y: '))

    print('\n=== SEGUNDO PONTO CARTESIANO ===')
    xb = int(input('Insira o x: '))
    yb = int(input('Insira o y: '))

    distancia_x = calcular_distancia(xa, xb)
    distancia_y = calcular_distancia(ya, yb)

    if distancia_x <= 0 or distancia_y <= 0:
        print('\nOs pontos não formam um retângulo')
    else:
        area = distancia_x * distancia_y
        print(f'\nArea do retângulo {distancia_x} x {distancia_y}: {area}')
