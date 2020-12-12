import argparse as ap


parser = ap.ArgumentParser()
parser.add_argument('base', help='the base of degree', type=int)
parser.add_argument('exponent', help='the exponent of degree', type=int)
args = parser.parse_args()


def fastPow(bas: int, exp: int) -> int:
    pow = 1
    while exp:
        if exp % 2:
            pow *= bas
        exp //= 2
        bas *= bas
    return pow


print(fastPow(args.base, args.exponent))
