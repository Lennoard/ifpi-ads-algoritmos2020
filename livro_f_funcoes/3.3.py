def do_four(f):
    f()
    f()
    f()
    f()

def print_linha_regular():
    for _ in range(4):
        print('|', end = ' ')
        print(' ' * 7, end = ' ')
    print('|')

def print_linha_divisora():
    for _ in range(4):
        print('+', '- ' * 4, end = '')
    print('+')

def print_linha_completa():
    print_linha_divisora()
    do_four(print_linha_regular)

def desenhar_grade():
    do_four(print_linha_completa)
    print_linha_divisora()

def main():
    desenhar_grade()

main()