# Leia uma letra e verifique se a letra digitada é vogal ou consoante.


def eh_vogal(char: str) -> bool:
    c = char.lower()
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'


if __name__ == '__main__':
    letra = input('Insira uma letra: ')

    if eh_vogal(letra):
        print(f'{letra} é uma vogal')
    else:
        print(f'{letra} é uma consoante')