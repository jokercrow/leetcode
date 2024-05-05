def subarraySum(nums: list, k: int) -> int:
    l, res = len(nums), 0
    for i in range(l):
        j = i
        print(i)
        while j < l:
            if sum(nums[i:j+1]) == k:
                res += 1
                print(i,j)
            j += 1
    return res

print(subarraySum([1,1,1],2))