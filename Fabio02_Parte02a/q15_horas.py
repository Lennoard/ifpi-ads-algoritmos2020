#15. Leia a quantidade de horas aula dadas por dois professores e 
# o valor por hora recebido por cada um. Escreva na tela qual 
# dos professores tem salário total maior.


def calcular_salario_por_aula(ha, vh):
    return ha + vh

def main():
    horas_aula_p1 = int(input('Professor 1, insira a quantidade de horas por aula: '))
    valor_hora_p1 = float(input('Insira o valor por hora: '))
    horas_aula_p2 = int(input('\nProfessor 2, insira a quantidade de horas por aula: '))
    valor_hora_p2 = float(input('Insira o valor por hora: '))

    salario_aula_p1 = calcular_salario_por_aula(horas_aula_p1, valor_hora_p1)
    salario_aula_p2 = calcular_salario_por_aula(horas_aula_p2, valor_hora_p2)

    if salario_aula_p1 > salario_aula_p2:
        print('\nProfessor 1 tem salário maior')
    else:
        print('\nProfessor 2 tem salário maior')

main()