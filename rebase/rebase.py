import locale
from termcolor import colored


def main():
    locale.setlocale(locale.LC_MONETARY, '')
    v = 2_000_000
    print(f'Valor da Lamborghini do Abner: {colored(locale.currency(v), "yellow")}')


def brl_to_usd(brl):  # 5,54
    raise NotImplementedError()


def brl_to_btc(brl):  # 233.938,52
    raise NotImplementedError()


if __name__ == "__main__":
    main()
