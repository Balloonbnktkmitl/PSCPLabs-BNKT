"""Ejudge"""
def main():
    """Stepper II"""
    start = int(input())
    stop = int(input())
    if start >= stop:
        for i in range(start, stop-1, -1):
            print(i)
    else:
        for i in range(start, stop+1):
            print(i)
main()

