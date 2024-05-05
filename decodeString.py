def decodeString( s: str) -> str:
    st = []
    for i in s:
        if i != ']':
            st.append(i)
        else:
            tmp = []
            while st[-1] != '[':
                tmp.append(st.pop())
            st.pop()
            nums = ''
            while st and st[-1].isdigit():
                nums += st.pop()
            nums = int(nums[::-1])
            st += list(reversed(tmp * nums))
    return "".join(st)


print(decodeString("10[leetcode]"))