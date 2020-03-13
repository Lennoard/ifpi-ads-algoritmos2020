# Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: 
# 
# o número de anos que ele fuma, 
# o no de cigarros fumados por dia e 
# o preço de uma carteira (1 carteira tem 20 cigarros).

anos_fumando = int(input('Insira há quantos anos você fuma: '))
cigarros_por_dia = int(input('Insira a quantidade de cigarros fumados por dia: '))
preco_carteira = int(input('Insira o preco da carteira de cigarros: '))

dias_fumando = anos_fumando * 365
preco_por_cigarro = preco_carteira / 20
dinheiro_gasto = preco_por_cigarro * (dias_fumando * cigarros_por_dia)

print(f'\nQuantidade de dinheiro gasto nesses {anos_fumando} ano(s) fumando: R${dinheiro_gasto}')