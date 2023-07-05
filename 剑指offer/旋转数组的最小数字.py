#题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
#输入：[3,4,5,1,2] 输出1

#题解：关键是利用最小值后的数都递增，最小值前的序列也递增，且最小值序列的最后面的值小于前面序列的任何一个值
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here

        left = 0
        right = len(rotateArray) - 1
        while right - left > 1:
            if rotateArray[int((left + right) / 2)] > rotateArray[right]:
                left = int((left + right) / 2)
            else:
                right = int((left + right) / 2)
        return rotateArray[right]
