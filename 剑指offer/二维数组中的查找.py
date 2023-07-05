#在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


#题解：两个规则，(i从0开始递增)A[i,j-1]>target则往左移，A[i,j-1]<target 则往下移，知道i>row-1,j<0
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if array == []:
            return False
        num_row = len(array)
        num_col = len(array[0])
        i = 0
        j = num_col-1
        while j >= 0 and i < num_row:
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True