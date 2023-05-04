"""Ejudge"""
def main():
    """AscendingSort"""
    check = []
    for _ in range(5):
        num = input()
        check.append(int(num))
        check.sort()
    for i in check:
        print(i)
main()
