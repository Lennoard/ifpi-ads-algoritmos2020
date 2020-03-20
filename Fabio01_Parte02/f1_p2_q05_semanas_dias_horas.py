# Leia um número inteiro de horas, calcule e escreva quantas semanas, 
# quantos dias e quantas horas ele corresponde.

total_horas = int(input('Insira a quantidade de horas: '))

s = (total_horas // 24) // 7
d = (total_horas // 24) % 7
h = total_horas % 24

print(f'"{total_horas} horas" -> {s} semanas, {d} dias e {h} horas')
