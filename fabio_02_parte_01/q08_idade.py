# 8. Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa,
# calcule e escreva sua idade exata (em anos).


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


def calcular_idade_em_anos(atual_dia, atual_mes, atual_ano, nasc_dia, nasc_mes, nasc_ano):
    atual_dias = data_para_dias(atual_dia, atual_mes, atual_ano)
    nasc_dias = data_para_dias(nasc_dia, nasc_mes, nasc_ano)

    atual_anos = atual_dias // 365
    nasc_anos = nasc_dias // 365

    anos_de_idade = atual_anos - nasc_anos

    if atual_mes > nasc_mes:
        return anos_de_idade
    elif atual_mes == nasc_mes:
        if atual_dia > nasc_dia:
            return anos_de_idade
        else:
            return anos_de_idade - 1
    else:
        return anos_de_idade - 1


if __name__ == '__main__':
    atual_dia = int(input('Insira o dia atual: '))
    atual_mes = int(input('Insira o mês atual: '))
    atual_ano = int(input('Insira o ano atual: '))

    nasc_dia = int(input('Insira o dia de nascimento: '))
    nasc_mes = int(input('Insira o mês de nascimento: '))
    nasc_ano = int(input('Insira o ano de nascimento: '))

    try:
        anos_de_idade = calcular_idade_em_anos(atual_dia, atual_mes, atual_ano, nasc_dia, nasc_mes, nasc_ano)
        print(f'Você tem {anos_de_idade} anos de idade')
    except ValueError as e:
        print(f'Falha ao calcular idade: {e}')
