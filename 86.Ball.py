"""Ejudge"""
def main():
    """Ball"""
    ball = float(input())
    tmp = 0
    while ball >= 0.01:
        ball = ball/5*3
        tmp += 1
    print(tmp-1)
main()

