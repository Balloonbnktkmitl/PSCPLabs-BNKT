"""Ejudge"""
def main():
    """Day I"""
    years = int(input())
    if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
        print("Yes")
    else:
        print("No")
main()

