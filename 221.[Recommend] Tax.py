"""Ejudge"""


def main():
    """[Recommend] Tax"""
    usecar = int(input())
    engine = int(input())
    tax = 0
    if engine > 1800:
        tax += (engine-1800)*4
        engine = 1800
    if engine > 600:
        tax += (engine-600)*1.5
        engine = 600
    tax += engine*0.5
    
    if usecar == 6:
        tax = tax*(90/100)
    elif usecar == 7:
        tax = tax*(80/100)
    elif usecar == 8:
        tax = tax*(70/100)
    elif usecar == 9:
        tax = tax*(60/100)
    elif usecar >= 10:
        tax = tax*(50/100)
    print("%.2f" % (tax))


main()
