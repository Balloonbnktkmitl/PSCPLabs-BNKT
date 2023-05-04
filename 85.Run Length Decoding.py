"""Ejudge"""
def main():
    """Run Length Decoding"""
    coding = input()
    decode = ""
    for i in coding:
        if i.isdigit():
            decode += i
        else:
            print(i * int(decode), end="")
            decode = ""
main()



