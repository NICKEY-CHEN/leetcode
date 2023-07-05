#题目：输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为 O(n).


# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        def sum_num(array):
            sum_n = 0
            for i in array:
                sum_ n+ =i
            return sum_n
        i = 0
        j = len(array)
        num_sum = max(array)
        while i< j:
            if sum_num(array[i:j]) > num_sum:
                num_sum = sum_num(array[i:j])
                i += 1
            else:
                j -= 1
        return num_sum

    #动态规划法
    class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        n = len(array)
        dp = [ i for i in array]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+array[i],array[i]) ’注意看这里的方程‘        
        return max(dp)
    
