# 23. Leia 2 datas (cada data é composta por 3 variáveis
# inteiras: dia, mês e ano) e escreva qual delas é a mais recente.


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
    print('=== PRIMEIRA DATA (dd/MM/aaaa) ===')
    data1_dia = int(input('Insira o dia (2 dígitos): '))
    data1_mes = int(input('Insira o mês (2 dígitos): '))
    data1_ano = int(input('Insira o ano (4 dígitos): '))

    print('\n=== SEGUNDA DATA  (dd/MM/aaaa) ===')
    data2_dia = int(input('Insira o dia (2 dígitos): '))
    data2_mes = int(input('Insira o mês (2 dígitos): '))
    data2_ano = int(input('Insira o ano (4 dígitos): '))

    try:
        data1_dias = data_para_dias(data1_dia, data1_mes, data1_ano)
        data2_dias = data_para_dias(data2_dia, data2_mes, data2_ano)

        if data1_dias < data2_dias:
            print('A primeira data é a mais recente')
        else:
            print('A segunda data é a mais recente')
    except Exception as e:
        print(str(e))

