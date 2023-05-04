"""Ejudge"""
def main():
    """Sequence VII"""
    row = int(input())
    for i in range(0, row):
        num = 1
        for j in range(0, i+1):
            j = j
            print(num, end=" ")
            num += 1
        print()
    for i in range(row-1, 0, -1):
        num = 1
        for j in range(0, i):
            j = j
            print(num, end=" ")
            num += 1
        print()
main()
