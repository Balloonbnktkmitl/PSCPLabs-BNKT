"""Ejudge(Midterm)"""
def main():
    """Calculator"""
    num = int(input())
    cal = 0
    for i in range(1, num+1):
        if num == 1:
            cal += 1
            break
        else:
            cal += len(str(i))
    if cal == 1:
        print("1")
    else:
        print(num+cal)
main()
