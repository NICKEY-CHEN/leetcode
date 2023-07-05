#题目：
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

#题解：
#关键是传递公式。今天要么操作，要么不操作，dp[i] = max(dp[i-1],price[i]-min(price)),dp存储的是过往最大
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        profit = [float('-inf')]*n
        for i in range(1,n):
            profit[i] = max(profit[i-1], prices[i] - min(prices[0:i]))
        print(profit)
        return max(profit)
a = Solution()
a.maxProfit([7,1,5,3,6,4])
