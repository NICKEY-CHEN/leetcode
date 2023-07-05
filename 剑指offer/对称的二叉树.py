#题目：
# 请实现一个函数，用来判断一棵二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。输入
# {8,6,6,5,7,7,5} return:True

#题解：
#基本逻辑是，如果对称，那么左节点的左节点==右节点的右节点，左节点的右节点==右节点的左节点

class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        def compare_values(pLeft,pRight):
            if not pLeft and not pRight: #这
                return True              #四
            if not pLeft or not pRight:  #行
                return False             #是防止空节点，一直判断左右（对于父节点）是否相等，如果两左右都没了，就说明之前的都通过判断了，那就return True
            if pLeft.val != pRight.val:
                return False
            return compare_values(pLeft.left,pRight.right) and compare_values(pLeft.right,pRight.left)
        return compare_values(pRoot,pRoot)
