"""Ejudge"""
def main():
    """Grade III"""
    sub = int(input())
    tmp = 0
    for i in range(sub):
        i = i
        score = float(input())
        if 100 >= score >= 95:
            tmp += 4
        elif score >= 90:
            tmp += 3.5
        elif score >= 85:
            tmp += 3
        elif score >= 80:
            tmp += 2.5
        elif score >= 75:
            tmp += 2
        elif score >= 70:
            tmp += 1.5
        elif score >= 65:
            tmp += 1
        elif score >= 60:
            tmp += 0.5
        elif score >= 0:
            tmp += 0
    print("%.2f" %((int((tmp/sub)*100))/100))
main()

