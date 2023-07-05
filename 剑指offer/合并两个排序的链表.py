# 题目描述:输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
# 示例1输入{1,3,5},{2,4,6},返回值{1,2,3,4,5,6}

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1 and not pHead2:
            return
        res = []
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                res.append(pHead1)
                pHead1 = pHead1.next
            else:
                res.append(pHead2)
                pHead2 = pHead2.next
        while pHead1:
            res.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            res.append(pHead2)
            pHead2 = pHead2.next
        n = len(res)
        for i in range(n):
            if i == n-1:
                res[i].next = None
            else:
                res[i].next = res[i+1]
        return res[0]