kg_desejado = float(input('Insira a quantidade desejada de letão (em kg): '))

cobre = (kg_desejado / 100) * 70
zinco = (kg_desejado / 100) * 30

print(f'Para produzir {kg_desejado} de latão serão necessários:\n')
print(f'{cobre} kg de cobre')
print(f'{zinco} kg de zinco')