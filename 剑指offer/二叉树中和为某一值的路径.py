# 题目：输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径
#输入：{10,5,12,4,7},22，输出：[[10,5,7],[10,12]]

# 题解：

class Solution:
    def __init__(self):
        self.onepath = []
        self.path_array = []
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return self.path_array
        self.onepath.append(root.val)
        expectNumber = expectNumber - root.val
        if expectNumber ==0 and (not root.left and not root.right):
            self.path_array.append(self.onepath[:])
        elif expectNumber > 0 and (root.left or root.right):
            if root.left:
                self.FindPath(root.left, expectNumber)
            if root.right:
                self.FindPath(root.right, expectNumber)
        self.onepath.pop()
        return self.path_array