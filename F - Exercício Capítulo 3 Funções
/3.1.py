def right_justify(s):
    tamanho = len(s)
    falta = 70 - tamanho
    print(' ' * falta, s)

def main():
    right_justify('abc')

main()