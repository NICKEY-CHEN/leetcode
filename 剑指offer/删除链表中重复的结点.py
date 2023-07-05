# 题目描述：在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
# 示例1输入：{1,2,3,3,4,4,5}返回值：{1,2,5}

#题解：不同，同加一；相同，p先不动，cur动到与下一个不同时停止，此时p指向新cur

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        p0 = ListNode(-1)
        p = p0
        p.next = pHead
        cur = pHead
        while cur and cur.next:
            if cur.val != cur.next.val:
                p = p.next
                cur = cur.next
            else:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                p.next = cur
        return p0.next