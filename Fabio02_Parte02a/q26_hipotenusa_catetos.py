# 26. Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.


def eh_triangulo(lado1, lado2, lado3) -> bool:
    if lado1 + lado2 < lado3:
        return False
    if lado1 + lado3 < lado2:
        return False
    if lado2 + lado3 < lado1:
        return False
    return True


def maior(x, y, z=-2 ** -100) -> int:
    if x >= y and x >= z:
        return x
    if y >= x and y >= z:
        return y
    return z


if __name__ == '__main__':
    l1 = float(input('Insira o primeiro lado do triângulo: '))
    l2 = float(input('Insira o segundo lado do triângulo: '))
    l3 = float(input('Insira o terceiro lado do triângulo: '))

    if eh_triangulo(l1, l2, l3):
        h = maior(l1, l2, l3)

        if l1 == h:
            print(f'Hipotenusa: {l1}\nCatetos: {l2}, {l3}')
        elif l2 == h:
            print(f'Hipotenusa: {l2}\nCatetos: {l1}, {l3}')
        else:
            print(f'Hipotenusa: {l2}\nCatetos: {l1}, {l2}')
    else:
        print('Os lados não formam um triângulo')

