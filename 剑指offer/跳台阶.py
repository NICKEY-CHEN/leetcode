#题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

#题解：跳台阶问题，但是不能用递归，用一个循环，传递函数的f(n) = f(n-1) + f(n-1)，因为假定第一步是1阶，跳法是f(n-1);假定第一步是2阶，跳法是f(n-2)
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        jump_one = 1
        jump_two = 2
        for i in range(2,number):
            count = jump_one + jump_two
            jump_one = jump_two
            jump_two = count
        return count