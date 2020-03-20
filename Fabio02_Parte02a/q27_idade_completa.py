# Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu
# nascimento e a data (dia, mês e ano) atual.


def data_para_dias(d, m, a):
    if d > 31 or d <= 0:
        raise ValueError('Dia inválido')

    if m > 12 or m <= 0:
        raise ValueError('Mês inválido')

    if a <= 0:
        raise ValueError('D.C somente, por favor')

    dia = to_days(d, 'dia')
    meses_em_dias = to_days(m, 'mes')
    ano_em_dias = to_days(a, 'ano')

    return dia + meses_em_dias + ano_em_dias


def to_days(n: int, tipo: str = 'ano'):
    if tipo == 'ano':
        return n * 365
    elif tipo == 'mes':
        return n * 30
    elif tipo == 'dia':
        return n
    else:
        raise ValueError(f'Valor inválido para "tipo", esperado ["ano, "mes", dia"] mas obteve {tipo}')


if __name__ == '__main__':
    atual_dia = int(input('Insira o dia atual: '))
    atual_mes = int(input('Insira o mês atual: '))
    atual_ano = int(input('Insira o ano atual: '))

    nasc_dia = int(input('Insira o dia de nascimento: '))
    nasc_mes = int(input('Insira o mês de nascimento: '))
    nasc_ano = int(input('Insira o ano de nascimento: '))

    try:
        atual_dias = data_para_dias(atual_dia, atual_mes, atual_ano)
        nasc_dias = data_para_dias(nasc_dia, nasc_mes, nasc_ano)

        idade_dias = atual_dias - nasc_dias

        anos = idade_dias // 365
        resto_dias = idade_dias % 365

        meses = resto_dias // 30
        dias = resto_dias % 30

        print(f'\nVocê tem {anos} anos, {meses} meses e {dias} dias')
    except ValueError as e:
        print(f'Falha ao calcular idade: {e}')
