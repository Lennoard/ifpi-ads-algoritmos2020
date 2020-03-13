#16. Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” 
# se a média das duas notas for maior ou igual a 7,0. Caso a média seja 
# inferior a 7,0, o programa deve ler a nota do exame e calcule a média 
# final. Se esta média for maior ou igual a 5,0, o programa deve escreva 
# “Aprovado”, caso contrário deve escrever “Reprovado”.

def calcular_media_2(n1, n2):
    return (n1 + n2) / 2

def main():
    n1 = float(input('Insira a primeira nota: '))
    n2 = float(input('Insira a segunda nota: '))
    print(' ')

    media = calcular_media_2(n1, n2)

    if (media >= 7.0):
        print('Aprovado')
    else:
        n3 = float(input('Média inferior a 7, insira a nota do último exame: '))
        if (calcular_media_2(media, n3) >= 5.0):
            print('Aprovado')
        else:
            print('Reprovado')

main()
