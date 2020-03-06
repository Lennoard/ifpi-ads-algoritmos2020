def do_four(f):
    f()
    f()
    f()
    f()

def print_linha_regular():
    print('|', end = ' ')
    print(' ' * 7, end = ' ')
    print('|', end = ' ')
    print(' ' * 7, end = ' ')
    print('|')

def print_linha_divisora():
    print('+', '- ' * 4, end = '')
    print('+', '- ' * 4, end = '')
    print('+')

def desenhar_grade():
    print_linha_divisora()
    do_four(print_linha_regular)
    print_linha_divisora()
    do_four(print_linha_regular)
    print_linha_divisora()

def main():
    desenhar_grade()

main()