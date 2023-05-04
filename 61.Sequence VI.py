"""Ejudge"""
def main():
    """Sequence VI"""
    row = int(input())
    for i in range(0, row):
        num = 1
        for j in range(0, i+1):
            j = j
            print(num, end=" ")
            num += 1
        print()
main()
