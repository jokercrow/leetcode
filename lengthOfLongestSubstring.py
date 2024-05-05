def lengthOfLongestSubstring(s: str) -> int:
    max_num = 0
    i, j = 0, 0
    while j < len(s) :
        if len(s[i:j + 1]) == len(set(s[i:j + 1])):
            print(s[i:j + 1])
            max_num = max(len(s[i:j + 1]), max_num)
            j += 1

        else:
            print(s[i:j + 1])
            i += 1
    return max_num

m = lengthOfLongestSubstring("abcabcbb")
print(m)