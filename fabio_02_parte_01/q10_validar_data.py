# 10. Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.


def data_valida(d, m, a) -> bool:
    if (d <= 0) or (m <= 0) or (a <= 0):
        return False

    if d > 31:
        return False

    if m > 12:
        return False

    return True


if __name__ == '__main__':
    dia = int(input('Insira o dia: '))
    mes = int(input('Insira o mês: '))
    ano = int(input('Insira o ano: '))

    valida = data_valida(dia, mes, ano)

    if valida:
        print('\nData válida')
    else:
        print('\nData inválida')

