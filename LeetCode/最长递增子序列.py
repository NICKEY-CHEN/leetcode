# 题目：给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

#题解，#如果大于最后个数，就加上；如果小于最后一个数，则通过bisect.bisect将从左到右第一个比他大的元素换掉
#说实话，牛客上超时，这道题本身即使不超时就是有问题的，比如[]1,3,5,2]用这种方法只能返回【1，2,5】,但是用暴力又肯定超时
import bisect
class Solution:
    def LIS(self , arr ):
        # write code here
        n = len(arr)
        dp = [1] * n
        lenth = 1
        array = [arr[0]]
        for i in range(1, n):
            if arr[i] > array[-1]:
                lenth += 1
                dp[i] = lenth
                array.append(arr[i])
            else:
                index = bisect.bisect(array, arr[i])
                dp[i] = index + 1
                array[index] = arr[i]
        res = []
        max_num = array[-1]
        max_num_index = arr.index(max_num)
        lenth = max(dp)
        for i in range(max_num_index, -1, -1):
            if res == [] or (arr[i] < res[-1] and dp[i] == lenth):
                res.append(arr[i])
                lenth -= 1
        return res[::-1]



