"""Ejudge"""
def main():
    """CompositeFunction"""
    number = int(input())
    print("%.2f" %(funcf(funcg(number))))
    print("%.2f" %(funcg(funcf(number))))
def funcf(number):
    """CompositeFunction"""
    return number*2
def funcg(number):
    """CompositeFunction"""
    return (number/2)+1
main()

