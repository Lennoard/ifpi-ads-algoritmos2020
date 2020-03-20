# Leia um número inteiro de metros, calcule e escreva
# quantos Km e quantos metros ele corresponde.

m_total = int(input('Insira um valor em metros: '))

km = m_total // 1000
m = (m_total % 1000)
print(f'{m_total}m corresponde a {km} quilômetro(s) e {m} metro(s)')