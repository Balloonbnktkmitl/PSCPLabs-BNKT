"""Ejudge"""
import hashlib
def main():
    """BreakPassword"""
    word = input()
    for i in range(0, 100000):
        tmp = hashlib.sha512(str(i).zfill(5).encode('utf-8')).hexdigest().upper()
        if tmp == word:
            print(str(i).zfill(5))
            break
main()
