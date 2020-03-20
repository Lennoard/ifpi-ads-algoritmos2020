#20. Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante 
# (primeiro, segundo, terceiro ou quarto) em que o ângulo se localiza.

def determinar_quadrante(a):
    if (a < 90):
        return '1º quadrante'
    elif (a < 180):
        return '2º quadrante'
    elif (a < 270):
        return '3º quadrante'
    else:
        return '4º quadrante'

def main():
    angulo = float(input('Insira a media de um ângulo: '))

    if (angulo < 0 or angulo > 360):
        print('Ângulo inválido')
    else:
        print(determinar_quadrante(angulo))

main()