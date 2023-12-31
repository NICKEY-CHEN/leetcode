# 题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

#题解：二叉树前序遍历的顺序为：
# 先遍历根节点；
# 随后递归地遍历左子树；
# 最后递归地遍历右子树。
# ​
# 二叉树中序遍历的顺序为：
# 先递归地遍历左子树；
# 随后遍历根节点；
# 最后递归地遍历右子树。
#
# 对于任意一颗树而言，前序遍历的形式总是
# [ 根节点, [左子树的前序遍历结果], [右子树的前序遍历结果] ]
# 即根节点总是前序遍历中的第一个节点。而中序遍历的形式总是
# [ [左子树的中序遍历结果], 根节点, [右子树的中序遍历结果]

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return
        root = TreeNode(pre[0])
        index  = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:index+1], tin[:index])
        root.right = self.reConstructBinaryTree(pre[index+1:], tin[index+1:])
        return root
