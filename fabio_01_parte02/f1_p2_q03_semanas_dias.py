# Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

total_dias = int(input('Insira a quantidade de dis: '))

semanas = total_dias // 7
dias = total_dias %  7

print(f'{total_dias} corresponde a {semanas} semana(s) e {dias} dia(s)')
