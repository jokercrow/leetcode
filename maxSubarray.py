def maxSubArray(nums: list) -> int:
    prefix_n = []
    s = 0
    for i in nums:
        s += i
        prefix_n.append(s)

    return prefix_n

print(maxSubArray([-2,-1]))
