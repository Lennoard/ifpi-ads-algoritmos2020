def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_twice(f, arg):
    f(arg)
    f(arg)

def print_spam():
    print('spam')

def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)

def main():
    do_twice(print_twice, "spam")
    do_four(print, "teste")

main()
