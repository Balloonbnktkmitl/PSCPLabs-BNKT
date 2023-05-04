"""Ejudge"""
def main():
    """PrasomSib"""
    num = input()
    tmp = 0
    ans = 0
    for i in range(len(num)):
        for j in range(len(num)):
            tmp = int(num[i])+int(num[j])
            if tmp == 10:
                ans += 1
                break
            elif tmp > 10:
                tmp = int(num[j])
                
             
    print(ans)      
main()

