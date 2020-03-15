#17. Leia valores inteiros em duas variáveis distintas e se o resto da divisão 
# da primeira pela segunda for 1 escreva a soma dessas variáveis mais o resto da divisão; 
# se for 2 escreva se o primeiro e o segundo valor são pares ou ímpares; 
# se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; 
# se for igual a 4 divida a soma dos números lidos pelo segundo, 
# se este for diferente de zero. Em qualquer outra situação escreva o quadrado dos números lidos.

def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

def get_impar_ou_par_str(n):
    if (eh_par(n)):
        return f'"{n}" é par'
    else: 
        return f'"{n}" é ímpar'

def main():
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))

    resto = n1 % n2
    soma = n1 + n2

    if resto == 1:
        print(soma + resto)
    elif resto == 2:
        print(get_impar_ou_par_str(n1))
        print(get_impar_ou_par_str(n2))
    elif resto == 3:
        print(soma * n1)
    elif resto == 4:
        valor = soma / n2 
        if (valor != 0):
            print(valor)
    else:
        print(n1**2)
        print(n2**2)

main()