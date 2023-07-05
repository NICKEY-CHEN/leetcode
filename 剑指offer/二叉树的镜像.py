# 题目：操作给定的二叉树，将其变换为源二叉树的镜像。
# 比如：    源二叉树
#             8
#            /  \
#           6   10
#          / \  / \
#         5  7 9 11
#         镜像二叉树
#             8
#            /  \
#           10   6
#          / \  / \
#         11 9 7  5
# 输入{8,6,10,5,7,9,11}
# 返回值{8,10,6,11,9,7,5}

# 题解
# 使用递归思想：
# 先镜像当前root左右节点，然后再递归镜像左孩子和右孩子即可。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Mirror(self, pRoot):
        # write code here
        while pRoot:
            pRoot.left, pRoot.right = pRoot.right, pRoot.left
            self.Mirror(pRoot.left)
            self.Mirror(pRoot.right)
            return pRoot
#二叉树常常使用递归思想        
