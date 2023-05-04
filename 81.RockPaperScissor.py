"""Ejudge"""
def matchpoint(match, pointa, pointb):
    """matchpoint"""
    if match[:1] == "R":
        if match[1:] == "S":
            pointa += 1
        elif match[1:] == "P":
            pointb += 1
    elif match[:1] == "S":
        if match[1:] == "P":
            pointa += 1
        elif match[1:] == "R":
            pointb += 1
    elif match[:1] == "P":
        if match[1:] == "R":
            pointa += 1
        elif match[1:] == "S":
            pointb += 1
    return pointa, pointb
def main():
    """RockPaperScissor"""
    match = input()
    roun = []
    tmp = 0
    pointa = 0
    pointb = 0
    for i in range(int(len(match)/2)):
        if i == 0:
            roun.append(match[i]+match[i+1])
        else:
            roun.append(match[tmp:tmp+2])
        tmp += 2
    for win in range(len(roun)):
        pointa, pointb = matchpoint(roun[win], pointa, pointb)
    if pointa > pointb:
        print("A win %d-%d" % (pointa, pointb))
    elif pointa < pointb:
        print("B win %d-%d" % (pointb, pointa))
    else:
        print("DRAW %d" % (pointa))
main()

