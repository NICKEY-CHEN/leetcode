# 题目描述：输入一个链表，反转链表后，输出新链表的表头。
# 输入：{1,2,3}返回值{3,2,1}

#题解：
# 我们先定义三个指针left，mid，right
# left = pHead
# mid = left.next
# right = mid.next
# 然后掐断4指向1的next指针
# left.next = None
# 让mid.next转身指向left
# 然后让left，mid，right集体往右走一步，继续让mid.next转身指向left
# 直到right走到None上
# while right：
#     mid.next = left
#     left = mid
#     mid = right
#     right = right.next
# 让mid.next指向left,\
# 然后输出表头mid
# mid.next = left
# return mid

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return
        if not pHead.next:
            return pHead
        left = pHead
        mid = left.next
        right = mid.next
        left.next = None
        while right:
            mid.next = left
            left = mid
            mid = right
            right = right.next
        mid.next = left
        return mid