# Leia uma letra, verifique se letra é "F" ou "M" e escreva F - Feminino, M - Masculino, Sexo Inválido.


def definir_sexo(char: str) -> str:
    if char.upper() == 'F':
        return 'Feminino'
    if char.upper() == 'M':
        return 'Masculino'
    return 'Sexo inválido'


if __name__ == '__main__':
    letra = input('Insira uma letra para o sexo: ')

    print(definir_sexo(letra))

