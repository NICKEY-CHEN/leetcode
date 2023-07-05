#题目：从上往下打印出二叉树的每个节点，同层节点从左至右打印。
#输入：{5,4,#,3,#,2,#,1}， 输出：[5,4,3,2,1]

#题解：
#BFS广度优先遍历
#另外一种方式，通过队列
# 利用队列的先进先出(FIFO)特性解决。每从队列头部获取一个节点，就将该节点的左右子节点存入队列的尾部。如此往复，直至队列为空。
def PrintFromTopToBottom(self, root):
    queue = []
    result = []
    if root == None:
        return result

    queue.append(root)
    while queue:
        #删除最前面的节点，并传给newcode
        newNode = queue.pop(0)
        result.append(newNode.val)
        #左右子节点加入队列尾部
        if newNode.left != None:
            queue.append(newNode.left)
        if newNode.right != None:
            queue.append(newNode.right)
    return result
