# 题目描述:给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        res = []
        while pHead:
            if pHead in res:
                return pHead
            else:
                res.append(pHead)
                pHead = pHead.next