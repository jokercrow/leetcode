def findAnagrams(s: str, p: str) -> list:
    res = []
    for i in range(len(s) - len(p)+1):
        if sorted(s[i:i + len(p)]) == sorted(p):
            res.append(i)
    return res


a = findAnagrams("abab", "ab")
print(a)
