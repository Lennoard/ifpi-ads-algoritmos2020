# Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir 
# algum mecanismo para decidir o numero de notas de cada valor que deve ser 
# disponibilizado para o cliente que realizou o saque. Um possível critério 
# seria o da "distribuição ótima" no sentido de que as notas de menor valor 
# disponíveis fossem distribuídas em número mínimo possível. Por exemplo, se a
# maquina só dispõe de notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, para uma 
# quantia solicitada de R$ 87, o algoritmo deveria indicar uma nota de R$ 50, 
# três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. Escreva um algoritmo 
# que receba o valor da quantia solicitada e retorne a distribuição das notas de 
# acordo com o critério da distribuição ótima.


saque = int(input('Insira o valor do saque: '))

n_100 = saque // 100
resto = saque % 100

n_50 = resto // 50
resto = resto % 50

n_20 = resto // 20
resto = resto % 20

n_10 = resto // 10
resto = resto % 10

n_5 = resto // 5
resto = resto % 5

n_2 = resto // 2
resto = resto % 2

print('Saque:\n\n', f'100: {n_100}\n', f'50:  {n_50}\n', f'20:  {n_20}\n', f'10:  {n_10}\n', f'5:   {n_5}\n', f'2:   {n_2}')
