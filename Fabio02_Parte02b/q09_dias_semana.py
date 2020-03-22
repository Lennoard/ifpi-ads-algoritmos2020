# Leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda etc.), se digitar outro
# valor deve aparecer valor inválido.


def dia_semana_from(n: int) -> str:
    if n == 1:
        return 'Domingo'
    if n == 2:
        return 'Segunda'
    if n == 3:
        return 'Terça'
    if n == 4:
        return 'Quarta'
    if n == 5:
        return 'Quinta'
    if n == 6:
        return 'Sexta'
    if n == 7:
        return 'Sábado'
    return 'Valor inválido'


if __name__ == '__main__':
    n = int(input('Insira um dia da semana em número: '))

    print(dia_semana_from(n))
