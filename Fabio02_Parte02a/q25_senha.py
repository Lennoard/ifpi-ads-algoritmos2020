# 25. Verifique a validade de uma senha fornecida pelo usuário.
# A senha é 1234. O algoritmo deve escrever uma mensagem de permissão de acesso ou não.


def perguntar_senha():
    entrada = input('\nInsira sua senha: ')
    checar_senha(entrada)


def checar_senha(s):
    if s == '1234':
        print('Acesso permitido')
        pass
    else:
        print('Acesso negado')
        perguntar_senha()


if __name__ == '__main__':
    perguntar_senha()
