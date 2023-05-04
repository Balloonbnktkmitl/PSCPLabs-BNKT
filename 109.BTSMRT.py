"""Ejudge"""
def main():
    """BTSMRT"""
    day = input().upper()
    age = float(input())
    height = float(input())
    if age < 14 and height < 90:
        print("FREE")
    elif age >= 60 and day == "SENIOR DAY":
        print("FREE")
    elif age < 14 and height <= 140 and day == "CHILDREN DAY":
        print("FREE")
    else:
        print("PAY")
main()

