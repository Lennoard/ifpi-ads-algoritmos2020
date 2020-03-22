# Leia um número e escreva se o número é inteiro ou decimal.


def eh_decimal(n: float) -> bool:
    if n >= 0:
        return n % 1 > 0
    return n % -1 < 0


if __name__ == '__main__':
    numero = float(input('Insira um número: '))

    if eh_decimal(numero):
        print(f'O número {numero} é decimal')
    else:
        print(f'O número {int(numero)} é inteiro')
