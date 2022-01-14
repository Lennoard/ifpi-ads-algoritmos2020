import locale
from termcolor import colored


def main():
    locale.setlocale(locale.LC_MONETARY, '')
    v = 2_000_000
    print(f'Valor da Lamborghini do Abner: {colored(locale.currency(v), "yellow")}')
    print(f'Valor da Lamborghini do Abner em USD: {colored(locale.currency(brl_to_usd(v)), "yellow")}')
    print(f'Valor da Lamborghini do Abner em BTC: {colored(locale.currency(brl_to_btc(v)), "yellow")}')


def brl_to_usd(brl):  # 5,54?
    return brl / 5.54


def brl_to_btc(brl):  # 233.938,52
    return brl / 233_938.52


if __name__ == "__main__":
    main()
