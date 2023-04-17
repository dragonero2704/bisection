from dependencyCheck import depCheck

depCheck(__file__)


from math import *
from argparse import ArgumentParser, RawTextHelpFormatter
import numpy as np
import matplotlib.pyplot as plt
import tabulate



version = "1.1.1"
title = f"""
 /$$$$$$$  /$$                               /$$
| $$__  $$|__/                              |__/
| $$  \ $$ /$$  /$$$$$$$  /$$$$$$  /$$$$$$$$ /$$  /$$$$$$  /$$$$$$$   /$$$$$$
| $$$$$$$ | $$ /$$_____/ /$$__  $$|____ /$$/| $$ /$$__  $$| $$__  $$ /$$__  $$
| $$__  $$| $$|  $$$$$$ | $$$$$$$$   /$$$$/ | $$| $$  \ $$| $$  \ $$| $$$$$$$$
| $$  \ $$| $$ \____  $$| $$_____/  /$$__/  | $$| $$  | $$| $$  | $$| $$_____/
| $$$$$$$/| $$ /$$$$$$$/|  $$$$$$$ /$$$$$$$$| $$|  $$$$$$/| $$  | $$|  $$$$$$$
|_______/ |__/|_______/  \_______/|________/|__/ \______/ |__/  |__/ \_______/


author: dragonero2704
version: {version}
"""
debug = False
data = []

def bisection(a, b, g, iterations=1000, precision=None):
    global data
    for _ in range(iterations):
        if a == b:
            return a
        Ya, Yb = g(a), g(b)
        if Ya == 0:
            return a
        if Yb == 0:
            return b
        # if debug:
        #     print(f"g({a}) = {Ya} g({b}) = {Yb}")
        if Ya*Yb > 0:
            raise ValueError(f"f(a)*f(b)>0 on iteration {_}")
        Xmedian = (a+b)/2
        Ymedian = g(Xmedian)
        tolerance = abs(b-a)/2

        data.append({"a":a,"b":b,"f(a)":Ya,"f(b)":Yb,"Xm":Xmedian, "f(Xm)":Ymedian,"error":tolerance})

        if precision is not None and tolerance <= precision:
            return Xmedian
        elif Ymedian > 0:
            if Ya < 0:
                b = Xmedian
            else:
                a = Xmedian
        else:
            if Ya < 0:
                a = Xmedian
            else:
                b = Xmedian
            # Ymedian < 0

        # print(Xmedian)
    
    return Xmedian


def main():
    parser = ArgumentParser(prog=__file__.split('\\')[-1],
        usage="./%(prog)s",
        formatter_class=RawTextHelpFormatter,
        description=print(title),)

    parser.add_argument('-f', '--function', dest="f", action="store",
                        metavar="<Espressione matematica di f(x)>", help="-f x^3+x^2-4")
    parser.add_argument('-a', dest='a', action="store",
                        metavar="<Estremo inferiore [a,b]>", help="Estremo inferiore nell'intervallo [a,b]")
    parser.add_argument('-b', dest='b', action="store",
                        metavar="<Estremo superiore [a,b]>", help="Estremo superiore nell'intervallo [a,b]")
    parser.add_argument('-i', '--iterations', dest='iterations', action="store",
                        metavar="<numero di iterazioni>", help="Numero massimo di iterazioni della bisezione", default=1000)
    parser.add_argument('-p', '--precision', dest='precision', action="store",
                        metavar="<precisione di abs(a-b)/2>", help="Minimo intervallo [a,b]", default=None)
    parser.add_argument('-g', '--graph', dest='graph',
                        action="store_true", help="Grafico di f(x)")
    parser.add_argument('--print', dest='print',
                        action="store_true", help="Stampa le iterazione")

    args = parser.parse_args()
    # print(args)
    expression, a, b, i, p = args.f, args.a, args.b, args.iterations, args.precision
    global debug
    debug = args.print
    if expression is None:
        expression = input("f(x): ")

    replaces = {
        "^": "**",
        "[": "(",
        "{": "(",
        "]": ")",
        "}": ")"
    }
    for char in replaces:
        expression = expression.replace(char, replaces[char])

    f = eval(f"lambda x:float({expression})")
    # print(expression)
    if a is None:
        a = float(input("a: "))
    if b is None:
        b = float(input("b: "))
    a, b, i = float(a), float(b), int(i)
    if p is not None:
        p = float(p)
    print()
    try:
        x = bisection(a, b, f, i, p)
    except ValueError as e:
        print(e)
        x = None
    if debug:
        table = tabulate.tabulate(data, headers="keys", tablefmt="presto",showindex="always",stralign="center")
        print(table)
    print(x)

    if args.graph:
        print(f"Inserire dominio [A,B] di {expression}")
        A = float(input("A: "))
        B = float(input("B: "))
        xArr = np.linspace(A, B, 100)
        # print(xArr)
        yArr = [f(x) for x in xArr]
        # print(yArr)
        # plt.axes()
        plt.grid(True, "both")
        plt.plot(xArr, yArr, color="red")
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.scatter([x],[0], c="blue", zorder=5)
        plt.show()
    pass

if __name__ == "__main__":
    main()
