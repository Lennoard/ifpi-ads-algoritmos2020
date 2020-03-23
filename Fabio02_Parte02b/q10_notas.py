"""Leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a
sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E."""


def calcular_media(n1, n2):
    return (n1 + n2) / 2


def atribuir_nota(media) -> str:
    if media > 9:
        return 'A'
    if media > 7.5:
        return 'B'
    if media > 6:
        return 'C'
    if media > 4:
        return 'D'
    return 'E'


if __name__ == '__main__':
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))

    media = calcular_media(nota1, nota2)
    atribuicao = atribuir_nota(media)

    print(f'\nNota 1: {nota1}')
    print(f'Nota 2: {nota2}')
    print(f'Média: {media}')
    print(f'Atribuição: {atribuicao}')

    if atribuicao == 'A' or atribuicao == 'B' or atribuicao == 'C':
        print('APROVADO')
    else:
        print('REPROVADO')

