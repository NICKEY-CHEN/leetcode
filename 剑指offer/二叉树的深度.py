#题目：输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
#输入：{1,2,3,4,5,#,6,#,#,7}，输出4

# 题解：深度优先遍历

class Solution:
    def TreeDepth(self, pRoot):
        #该值为空返回0
        if not pRoot:
            return 0
        #该值不为空但左右为空，返回1
        if pRoot and not pRoot.left and not pRoot.right:
            return 1
        #不为空，且左右不为空，则继续往下遍历，寻找左右子节点最深的路径
        res = 1 + max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))
        return res