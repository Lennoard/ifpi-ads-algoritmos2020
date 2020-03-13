# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a 
# percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). 
# Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, 
# escreva um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

custo_fabrica = float(input('Insira o custo de fábrica do carro: '))

imposto = ((custo_fabrica / 100) * 45)
porcentagem_distribuidor = ((custo_fabrica / 100) * 28)
total = custo_fabrica + imposto + porcentagem_distribuidor

print(f'Custo total do carro ao consumidor: R$ {total}')
