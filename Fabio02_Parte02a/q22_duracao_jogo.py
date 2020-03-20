# 22. Leia a hora do início de um jogo e a hora de fim do jogo 
# (cada hora é composta por 2 variáveis inteiras: hora e minuto). 
# Calcule e escreva a duração do jogo (horas e minutos), sabendo-se 
# que o tempo máximo de duração do jogo é de 24 horas e que ele pode 
# iniciar-se em um dia e terminar no dia seguinte.

def tempo_passado(hi, hf, mi, mf):
    horas = horas_passadas(hi, hf)
    minutos = minutos_passados(mi, mf)

    if (hi == hf) and (mf < mi):
        return f'23 horas e {minutos} minutos'
    else:
        return f'{horas} horas e {minutos} minutos'

def horas_passadas(inicial, final):
    if (final < inicial):
        return (24 - inicial) + final
    else:
        return final - inicial


def minutos_passados(inicial, final):
    if (final < inicial):
        return (60 - inicial) + final
    else:
        return final - inicial


def main():
    print('INSIRA A HORA DE INÍCIO DO JOGO')
    inicio_hora = int(input('Horas: '))
    inicio_minutos = int(input('Minutos: '))

    print('\nINSIRA A HORA DE TÉRMINO DO JOGO')
    termino_hora = int(input('Horas: '))
    termino_minutos = int(input('Minutos: '))

    duracao = tempo_passado(inicio_hora, termino_hora, inicio_minutos, termino_minutos)

    print(f'O jogo durou {duracao}')


main()