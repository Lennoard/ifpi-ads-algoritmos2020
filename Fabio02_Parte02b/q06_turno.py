# Leia o turno em que um aluno estuda, sendo M para matutino, V para Vespertino ou N para Noturno e
# escreva a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


def greet(t: str):
    t = t.lower()

    if t == 'm':
        return 'Bom dia!'
    if t == 'v':
        return 'Boa tarde'
    if t == 'n':
        return 'Boa noite'
    return 'Valor inválido'


if __name__ == '__main__':
    turno = input('Insira o seu turno (M/V/N): ')

    print(greet(turno))

