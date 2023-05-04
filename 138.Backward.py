"""Ejudge"""
def main():
    """Backward"""
    tmp = []
    while True:
        word = input()
        if word == "NULL":
            break
        tmp.append(word)
    for i in range(1, len(tmp)+1):
        print(tmp[-i])
main()
