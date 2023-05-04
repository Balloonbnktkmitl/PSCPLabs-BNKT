"""Ejudge"""
def main():
    """Regulation"""
    numa = int(input())
    numb = float(input())
    numc = input()
    print("%30d" %numa)
    print("%030d" %numa)
    print("%.2f" %numb)
    print("%.12f" %numb)
    print(numc.rjust(40))
main()
