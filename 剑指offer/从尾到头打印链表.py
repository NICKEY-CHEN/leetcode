# 题目：输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
#输入：{67,0,24,58} 输出：[58,24,0,67]

# 题解：
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        node_list = []
        if listNode == None:
            return []
        while listNode != None:
            node_list.append(listNode.val)
            listNode = listNode.next
        return node_list[::-1]