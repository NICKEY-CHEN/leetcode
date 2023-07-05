#题目：输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。
#输入10 输出2

#题解：n*(n-1)，就是把整数减去1，并和原整数作与运算，会把该整数最右边一个1变为0
# 如果为负，则n&0xffffffff让其变正

class Solution:
    def NumberOf1(self, n):
        # write code here
        res = 0
        if n < 0:
            n = n & 0xffffffff
        while n!=0:
            res +=1
            n = (n-1) & n
        return res