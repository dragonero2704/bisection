from math import *
from argparse import ArgumentParser, RawTextHelpFormatter
version  = "0.1.1"
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

def bisection(a, b, g, iterations=1000, precision=None):
    for _ in range(iterations):
        Ya, Yb = g(a), g(b)
        if Ya*Yb > 0:
            raise ValueError("f(a)*f(b)>0")
        Xmedian = (a+b)/2
        Ymedian = g(Xmedian)
        if precision is not None and abs(b-a)/2 <= precision:
            return Xmedian
        elif Ymedian > 0:
            b = Xmedian
        elif Ymedian < 0:
            a = Xmedian
        # print(Xmedian)
    return Xmedian

def main():
    parser = ArgumentParser(prog=__file__.split('\\')[-1],
        usage="./%(prog)s",
        formatter_class=RawTextHelpFormatter,
        description=print(title),)
    
    parser.add_argument('-f','--function', dest="f", action="store", metavar="<Espressione matematica di f(x)>", help="-f x^3+x^2-4")
    parser.add_argument('-a', dest='a', action="store", metavar="<Estremo inferiore [a,b]>", help="Estremo inferiore nell'intervallo [a,b]")
    parser.add_argument('-b', dest='b', action="store", metavar="<Estremo superiore [a,b]>", help="Estremo superiore nell'intervallo [a,b]")
    parser.add_argument('-i', '--iterations', dest='iterations', action="store", metavar="<numero di iterazioni>", help="Numero massimo di iterazioni della bisezione", default=1000)
    parser.add_argument('-p', '--precision', dest='precision', action="store", metavar="<precisione di abs(a-b)/2>",help="Minimo intervallo [a,b]", default=None)
    args = parser.parse_args()
    print(args)
    expression,a,b,i,p = args.f,args.a,args.b,args.iterations,args.precision

    if expression is None:
        expression = input("f(x): ")
    
    
    replaces = {
        "^":"**",
        "[":"(",
        "{":"(",
        "]":")",
        "}":")"
    }
    for char in replaces:
        expression = expression.replace(char, replaces[char])

    f = eval(f"lambda x:{expression}")

    if a is None:
        a = float(input("a: "))
    if b is None:
        b = float(input("b: "))
    a,b,i = float(a),float(b),int(i)
    if p is not None:
        p = float(p)
    x = bisection(a,b,f,i,p)
    print(x)
    pass

if __name__ == "__main__":
    main()
