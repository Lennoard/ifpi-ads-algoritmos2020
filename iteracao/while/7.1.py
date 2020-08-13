import math


def mysqrt(a):
    x = 8
    while True:
        y = (x + a / x) / 2
        if y == x:
            return y
        x = y


def test_square_root():
    print('a    mysqrt(a)           math.sqrt(a)        diff')
    print('-    ---------           ------------        ----')

    for i in range(1, 10):
        my_sqrt = mysqrt(i)
        math_sqrt = math.sqrt(i)
        diff = float(math_sqrt - my_sqrt)

        print(f'{float(i)}  {my_sqrt}{get_space(my_sqrt)}{math_sqrt}{get_space(math_sqrt)}{diff}')


def get_space(obj):
    s = str(obj)
    length = len(s)
    if (length < 20):
        return ' ' * (20-length)
    return ' '


if __name__ == "__main__":
    test_square_root()

