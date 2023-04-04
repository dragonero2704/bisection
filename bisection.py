from math import *
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
    return Xmedian

def main():
    expression = input("f(x): ")
    expression = expression.replace('^','**')
    expression = expression.replace('[','(')
    expression = expression.replace(']',')')
    expression = expression.replace('{','(')
    expression = expression.replace('}',')')

    f = eval(f"lambda x:{expression}")
    a = float(input("a: "))
    b = float(input("b: "))

    x = bisection(a,b,f)
    print(x)
    pass

if __name__ == "__main__":
    main()
