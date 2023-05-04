"""Ejudge"""
def main():
    """Frame"""
    word = input()
    line(word)
    print("*"+word+"*")
    line(word)
def line(num):
    """Line"""
    print("*"*(len(num)+2))
main()

