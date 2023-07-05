#题目：给定一棵二叉搜索树，请找出其中的第k小的TreeNode结点。

#题解:中序遍历
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.result = []

    def sort_(self,pRoot):
        # 看成是这么个过程，每次先取左边，再取中间，后取右边，对于叶节点，其左右都为空（return ）
        if not pRoot:
            return
        self.sort_(pRoot.left)
        self.result.append(pRoot)
        self.sort_(pRoot.right)

    def KthNode(self, pRoot,k):
        # write code here
        self.sort_(pRoot)
        if k > len(self.result) or k==0:
            return
        return self.result[k-1]
a = Solution()
a.KthNode({5,3,7,2,4,6,8},3)
