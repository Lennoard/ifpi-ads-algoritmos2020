# Leia um número inteiro de segundos, calcule e escreva quantas horas, 
# quantos minutos e quantos segundos ele corresponde.

total_segundos = int(input('Insira a quantidade de segundos: '))

h = (total_segundos // 60) // 60
m = (total_segundos // 60) % 60
s = total_segundos % 60

print(f'"{total_segundos}" -> {h}:{m}:{s}')
