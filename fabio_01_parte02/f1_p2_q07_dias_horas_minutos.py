# Leia um número inteiro de minutos, calcule e escreva quantos
# dias, quantas horas e quantos minutos ele corresponde.


total_minutos = int(input('Insira a quantidade de minutos: '))

d = (total_minutos // 60) // 24
h = (total_minutos // 60) % 24
s = total_minutos % 60

print(f'"{total_minutos} minutos" -> {d} dia(s), {h} hora(s) e {s} segundo(s)')