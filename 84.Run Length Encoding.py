"""Ejudge"""
def main():
    """Run Length Encoding"""
    coding = input()
    tmp = coding[0]
    roundword = 0
    stringword = ""
    for i in range(len(coding)):
        if coding[i] == tmp:
            roundword += 1
        else:
            stringword += str(roundword) + coding[i-1]
            tmp = coding[i]
            roundword = 1
    stringword += str(roundword) + coding[-1]
    print(stringword)
main()

