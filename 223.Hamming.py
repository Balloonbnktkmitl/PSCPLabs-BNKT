"""Ejudge"""
def main():
    """Hamming"""
    word1 = input()
    word2 = input()
    ans = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            ans += 1
    print(ans)
main()
