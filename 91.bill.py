"""Ejudge"""
def main():
    """Bill"""
    num = int(input())
    service = (num*0.1)
    if service <= 50:
        vat = (50+num)*0.07
        summ = vat+num+50
    elif service >= 1000:
        vat = (1000+num)*0.07
        summ = vat+num+1000
    else:
        vat = (service+num)*0.07
        summ = vat+num+service
    print("%.2f" % summ)
main()
