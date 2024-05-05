#!/usr/bin/env python
# encoding: utf-8
# @author: Jokercrow
# @contact: zengchupeng@cls.cn
# @time: 2023-12-25 15:06

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    output_list = []

    def same_letter(a, b):
        return sorted(a) == sorted(b)

    for i in strs:
        if len(output_list)==0:
            output_list.append([i])
        else:
            output_list_c = output_list.copy()
            flag = 0
            for index_j,j in enumerate(output_list_c):
                if same_letter(i, j[0]):
                    output_list[index_j] = j+[i]
                    flag +=1
                elif index_j ==len(output_list_c)-1 and flag==0:
                    output_list.append([i])

        # print(output_list)
    return output_list


def groupAnagrams_1(strs):
    o_list= [strs[0]]
    strs = strs[1:]

    def same_letter(a,b):
        return sorted(a)==sorted(b)
    while strs:
        o_list_c = o_list.copy()
        for index,i in enumerate(o_list_c):
            if same_letter(i[0],strs[0]):
                o_list[index] = i+[strs[0]]
            else:
                o_list.append([strs[0]])
        strs = strs[1:]

    return o_list

a = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(a)