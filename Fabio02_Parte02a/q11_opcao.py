# 11. Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1;
# o valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
# possíveis para a variável opção são 1, 2 e 3.


if __name__ == '__main__':
    opcao = int(input('Opção (1/2/3): '))

    if opcao < 0 or opcao > 3:
        print('Opção inválida')
        quit()

    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    n3 = int(input('Insira o terceiro número: '))

    if opcao == 1:
        print(n1)
    elif opcao == 2:
        print(n2)
    else:
        print(n3)
