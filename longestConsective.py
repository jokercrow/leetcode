

def longestC(nums):
    # n = len(nums)
    # num_set = set(nums)
    # for i in num_set:
    #     if (i-1) not in num_set:
    #         tem = 1
    #         while (i+1) in num_set:
    #             tem+=1
    #             i+=1
    #         n = max(n,tem)
    #
    #
    # return n
    hash_dict = dict()

    max_length = 0
    for num in nums:
        if num not in hash_dict:
            left = hash_dict.get(num - 1, 0)
            right = hash_dict.get(num + 1, 0)

            cur_length = 1 + left + right
            if cur_length > max_length:
                max_length = cur_length

            hash_dict[num] = cur_length
            hash_dict[num - left] = cur_length
            hash_dict[num + right] = cur_length

            print("当下num%s不在dict中，他左边的值num-1的长度是%s，他右边的值num+1的长度是%s"%(num,left,right))

    return max_length

n = [100,4,200,1,3,2,6,4]
l = longestC(n)
print(l)

