# Leia um número inteiro de meses, calcule e escreva quantos 
# anos e quantos meses ele corresponde.

total_meses = int(input('Insira a quantidade de meses: '))

a = (total_meses // 12)
m = (total_meses % 12)

print(f'"{total_meses} meses" -> {a} anos e {m} meses')