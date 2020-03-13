# Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

idade_anos = int(input('Insira os anos de idade: '))
idade_meses = int(input('Insira os meses da idade: '))
idade_dias = int(input('Insira os dias da idade: '))


idade_final = (idade_anos * 365) + (idade_meses * 30) + idade_dias

print(f'A idade final é: {idade_final}')