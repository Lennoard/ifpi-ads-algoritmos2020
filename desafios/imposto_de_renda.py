# Usando pensamento computacional e as ferramentas de automação já conhecidas, 
# leia a matéria em anexo e faça um software que peça a renda do usuário e em 
# calcule e exiba qual o valor de imposto de renda real ele deverá pagar pela 
# tabela atual sem correção e pela tabela corrigida. 

# Quem tem renda tributável de R$ 13.800,00 - paga quanto?


def calcular_imposto_new(renda):
    if renda < 3881.65:
        return 0
    elif renda < 5714.11:
        return 7.5
    elif renda < 7654.67:
        return 15
    elif renda < 9564.42:
        return 22.5
    else:
        return 27.5


def calcular_imposto_old(renda):
    if renda < 1903.98:
        return 0
    elif renda < 2826.65:
        return 7.5
    elif renda < 3751.05:
        return 15
    elif renda < 4664.68:
        return 22.5
    else:
        return 27.5


def print_tabela(imposto):
    print('         FAIXA DE ISENÇÃO  |  TABELA ATUAL              |  TABELA CORRIGIDA')
    row2 = f'                       0%  |  Até 1.903,98              |  Até 3.881,65\n'
    row3 = f'                    7,5%  |  De 1.903,99 até 2.826,65  |  De 3.881,66 a 5.714,11\n'
    row4 = f'                     15%  |  De 2.826,66 até 3.751,05  |  De 5.714,12 a 7.654,67\n'
    row5 = f'                   22,5%  |  De 3.751,06 até 4.664,68  |  De 7.654,68 a 9.564,42\n'
    row6 = f'                   27,5%  |  Acima de 4.664,68         |  Acima de 9.564,42\n'
    indicador = '====>'

    if imposto == 0:
        row2 = indicador + row2[5:]
    elif imposto == 7.5:
        row3 = indicador + row3[5:]
    elif imposto == 15:
        row4 = indicador + row4[5:]
    elif imposto == 22.5:
        row5 = indicador + row5[5:]
    else:
        row6 = indicador + row6[5:]

    print(row2, row3, row4, row5, row6)


if __name__ == '__main__':
    renda = float(input('Insira a sua renda em R$: '))
    
    imposto_new = calcular_imposto_new(renda)
    desconto_new = (renda * imposto_new) / 100

    imposto_old = calcular_imposto_old(renda)
    desconto_old = (renda * imposto_old) / 100

    print_tabela(imposto_old)
    print(f'Seu imposto atual é {imposto_old}%, (R$ {desconto_old})')
    print(f'Seu imposto na tabela corrigida é {imposto_new}%, (R$ {desconto_new})')
