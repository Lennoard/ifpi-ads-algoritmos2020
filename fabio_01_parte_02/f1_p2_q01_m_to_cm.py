km = 10
ml = km / 1.61
sec = (42 * 60) + 42

sec_por_ml = (sec / ml)

print('Correu 10km em 42 min e 24 sec...\n')
print('10km -> %.2f ml\n' % ml)
print(f'Passo médio: {int(sec_por_ml / 60)} minutos e {int(sec_por_ml % 60)} segundos')

h = (sec / 60) / 60
print('Velocidade média: %.2f ml/h' % (ml / h))
