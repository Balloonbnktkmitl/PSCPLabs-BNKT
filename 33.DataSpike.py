"""Ejudge"""
def main():
    """DataSpike"""
    big = 0
    big = bigger(int(input()), big)
    big = bigger(int(input()), big)
    big = bigger(int(input()), big)
    big = bigger(int(input()), big)
    big = bigger(int(input()), big)
    big = bigger(int(input()), big)
    big = bigger(int(input()), big)
    big = bigger(int(input()), big)
    print(big)
def bigger(num, big):
    """bigger"""
    if num > big:
        big = num
    return big
main()

