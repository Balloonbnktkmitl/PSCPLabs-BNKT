"""Ejudge"""


def cal(oper, val):
    """Calculator"""
    value = []
    if oper == "==":
        value.append(val)
    elif oper == "!=":
        value = [int(i) for i in range(0, 10) if i != val]
    elif oper == ">":
        value = [int(i) for i in range(0, 10) if i > val]
    elif oper == "<":
        value = [int(i) for i in range(0, 10) if i < val]
    elif oper == ">=":
        value = [int(i) for i in range(0, 10) if i >= val]
    elif oper == "<=":
        value = [int(i) for i in range(0, 10) if i <= val]
    return value


def main():
    """Hint"""
    nuay = input()
    sib = input()
    roy = input()

    opnuay = nuay.split()[0]
    opsib = sib.split()[0]
    oproy = roy.split()[0]

    valnuay = cal(opnuay, int(nuay.split()[1]))
    valsib = cal(opsib, int(sib.split()[1]))
    valroy = cal(oproy, int(roy.split()[1]))

    for i in valroy:
        for j in valsib:
            for k in valnuay:
                print(str(i)+str(j)+str(k))


main()
