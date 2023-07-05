# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
#输入5,10,10，输出21

# 题解：如果机器人能够进入(i,j)的格子，则再判断能否进入4个相邻的鸽子(i-1,j),(i+1,j),(i,j+1),(i,j-1)

class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        num = 0
        for i in range(rows):
            for j in range(cols):
                if (self.calsum(i) + self.calsum(j) <= threshold):
                    num = num + 1
                elif (rows == 1 or cols == 1):
                    return num
        return num

    def calsum(self, temp):
        sum = 0
        while (temp != 0):
            sum += temp % 10
            temp = temp / 10
        return sum