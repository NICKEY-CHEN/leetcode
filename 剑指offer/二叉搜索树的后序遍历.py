#题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回true,否则返回false。
# 假设输入的数组的任意两个数字都互不相同。（ps：我们约定空树不是二叉搜素树）
#输入：[4,8,6,12,16,14,10]，输出True

#题解：

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        n = len(sequence)
        if n <= 0:
            return False
        #找到从左到右第一个大于sequence[-1]的值
        for i in range(n):
            if sequence[i] > sequence[-1]:
                break
        #检测是否有i后边的右子数小于sequence[-1]的值
        for ele in range(i,n):
            if sequence[ele]< sequence[-1]:
                return False
        #假定左子树为True,这一步的目的是防止【5】，这样的数字
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        #同理，【5,6】
        right = True
        if i < n - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right

