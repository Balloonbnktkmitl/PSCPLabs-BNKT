"""Ejudge"""
def main():
    """Pro"""
    comepro = int(input())
    paidpro = int(input())
    price = int(input())
    num = int(input())
    usepro = (num//comepro)*paidpro
    paid = (usepro+(num%comepro))*price
    print(paid)
main()
