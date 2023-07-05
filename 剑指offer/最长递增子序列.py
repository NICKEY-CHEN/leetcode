# 题目：给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
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
