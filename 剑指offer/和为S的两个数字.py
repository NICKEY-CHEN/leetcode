# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        n = len(array)
        if n< 0:
            return 0
        res = {}
        for i in range(int(n/2)+1):
            if (tsum - array[i]) in array:
                res[(array[i],tsum-array[i])] = array[i]*(tsum-array[i])

        #以下可以直接打印第一组相和为tsum，由于i*(tsum-i)在i = tsum/2时最大
        
        min_value = float('inf')
        res_list = []
        for keys,values in res.items():
            if values < min_value:
                min_value = values
                res_list = list(keys)
        return res_list
a = Solution()
a.FindNumbersWithSum([1,2,4,7,11,15],15)