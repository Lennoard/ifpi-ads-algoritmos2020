# Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
# o "Aprovado", se a média alcançada for maior ou igual a sete;
# o "Reprovado", se a média for menor do que sete;
# o "Aprovado com Distinção", se a média for igual a dez.


def status_aluno(n1, n2) -> str:
    media = (n1 + n2) / 2

    if media == 10:
        return 'Aprovado com Distinção'
    if media >= 7:
        return 'Aprovado'
    return 'Reprovado'


if __name__ == '__main__':
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))

    print(status_aluno(nota1, nota2))
