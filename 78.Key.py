"""Ejudge"""
def main():
    """Key"""
    num = input()
    key1 = 0
    for i in range(len(num)):
        key1 += int(num[i])
    key2 = int(num[-3:])*10
    sumkey = key1 + key2
    if sumkey < 1000:
        sumkey += 1000
    print(str(sumkey)[-4:])
main()
