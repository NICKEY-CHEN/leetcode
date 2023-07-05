#题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

#题解：创造一个哈希表--字典，记录所有出现值得频数，再找出最大频数的和int(num_len/2)比较


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        num_len = len(numbers)
        if num_len==1:
            return numbers[0]
        if num_len == 0:
            return 0
        res =  dict()
        for i in range(1,num_len):
            if numbers[i] in numbers[:i]:
                if not res.get(numbers[i]) and (res.get(numbers[i])!=0):
                    res[numbers[i]] = 1
                else:
                    res[numbers[i]] = res[numbers[i]] + 1
        max_num = 0
        key = 0

        for keys in res:
            if res.get(keys) > max_num:
                max_num = res.get(keys)
                key = keys
        if key:
            if (res[key]+1) > int(num_len/2):
                return key
            else:
                return 0
        else:
            return 0

#更简洁的做法
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        num=map(str,numbers)
        s=list(set(num))
        for i in s:
            if num.count(i)>len(numbers)/2:
                return int(i)
        return 0
a = Solution()
a.MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3])