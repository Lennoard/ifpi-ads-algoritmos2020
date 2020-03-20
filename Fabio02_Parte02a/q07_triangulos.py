# Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
# (três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
# formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
#escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).


def eh_triangulo(lado1, lado2, lado3) -> bool:
    if lado1 + lado2 < lado3:
        return False
    if lado1 + lado3 < lado2:
        return False
    if lado2 + lado3 < lado1:
        return False
    return True


def eh_equilatero(lado1, lado2, lado3) -> bool:
    return lado1 == lado2 == lado3


def eh_isosceles(lado1, lado2, lado3) -> bool:
    if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return True
    return False


if __name__ == '__main__':
    l1 = float(input('Insira o primeiro lado do triângulo: '))
    l2 = float(input('Insira o segundo lado do triângulo: '))
    l3 = float(input('Insira o terceiro lado do triângulo: '))

    if eh_triangulo(l1, l2, l3):
        if eh_equilatero(l1, l2, l3):
            print('Triângulo equilátero')
        elif eh_isosceles(l1, l2, l3):
            print('Triângulo isósceles')
        else:
            print('Triângulo escaleno')
    else:
        print('Os lados não formam um triângulo')
