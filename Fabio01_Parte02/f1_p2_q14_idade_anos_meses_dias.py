# Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

idade = int(input('Insira a idade em dias: '))

idade_anos = idade // 365
idade_meses = (idade % 365) // 30
idade_dias = (idade % 365) % 30

print(idade_anos, idade_meses, idade_dias)