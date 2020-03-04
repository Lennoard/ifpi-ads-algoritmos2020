def do_four(f):
    f()
    f()
    f()
    f()

def print_linha_regular():
    print('|         |         |')

def print_linha_divisora():
    print('+ - - - - + - - - - +')

def desenhar_grade():
    print_linha_divisora()
    do_four(print_linha_regular)
    print_linha_divisora()
    do_four(print_linha_regular)
    print_linha_divisora()

def main():
    desenhar_grade()

main()