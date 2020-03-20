# 12. Leia 1 (um) número inteiro e escreva se este número é par ou impar.

def eh_par(n) -> int:
    return n % 2 == 0

def main():
    n = int(input('Insira um número inteiro: '))
    if eh_par(n):
        print(f'O número "{n}"" é par')
    else:
        print(f'O número "{n}"" é ímpar')
main()