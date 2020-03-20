#19. Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o 
# índice de massa corpórea (IMC = peso / altura2). 
# Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), 
# obeso (IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).

def calcular_imc(h, w):
    return w / h**2

def main():
    altura = float(input('Insira a sua altura (em metros): '))
    peso = float(input('Insira o seu peso (em KG): '))

    imc = calcular_imc(altura, peso)
    print(f'\n{imc}')

    if (imc > 30):
        print('Obesidade mórbida')
    elif (imc >= 25):
        print('Obeso')
    else:
        print('Peso normal')

main()