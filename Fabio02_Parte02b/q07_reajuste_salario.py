"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contrataram para desenvolver o programa que calculará os reajustes. Escreva um algoritmo que leia o
salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
o salários até R$ 280,00 (incluindo) : aumento de 20%
o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
· o salário antes do reajuste;
· o percentual de aumento aplicado;
· o valor do aumento;
· o novo salário, após o aumento."""


def calcular_percentual_aumento(salario):
    if salario <= 280:
        return 20
    if salario < 700:
        return 15
    if salario < 1500:
        return 10
    return 5


if __name__ == '__main__':
    salario_atual = float(input('Insira o seu salário atual: '))

    percentual_aumento = calcular_percentual_aumento(salario_atual)
    valor_aumento = (salario_atual * percentual_aumento) / 100
    novo_salario = salario_atual + valor_aumento

    print(f'Percentual de aumento: {percentual_aumento}%')
    print(f'Valor do aumento: ${valor_aumento}')
    print(f'Seu novo salário é: ${novo_salario}')
