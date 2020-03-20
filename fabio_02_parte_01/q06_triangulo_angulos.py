# Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
# se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). Se formam,
# verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou
# obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau).


def forma_triangulo(ang1, ang2, ang3) -> bool:
    return ang1 + ang2 + ang3 == 180


def eh_acutangulo(ang1, ang2, ang3) -> bool:
    return ang1 < 90 and ang2 < 90 and ang3 < 90


def eh_retangulo(ang1, ang2, ang3) -> bool:
    return ang1 == 90 or ang2 == 90 or ang3 == 90


def eh_obtusangulo(ang1, ang2, ang3) -> bool:
    return ang1 > 90 or ang2 > 90 or ang3 > 90


if __name__ == '__main__':
    a1 = float(input('Insira o primeiro ângulo do triângulo: '))
    a2 = float(input('Insira o segundo ângulo do triângulo: '))
    a3 = float(input('Insira o terceiro ângulo do triângulo: '))

    if a1 < 0 or a2 < 0 or a3 < 0:
        print('Não existe ângulo com tamanho 0°')
    elif forma_triangulo(a1, a2, a3):
        if eh_acutangulo(a1, a2, a3):
            print('Acutângulo')
        elif eh_retangulo(a1, a2, a3):
            print('Retângulo')
        elif eh_obtusangulo(a1, a2, a3):
            print('Obtusângulo')
    else:
        print('Os ângulos não formam um triângulo')
