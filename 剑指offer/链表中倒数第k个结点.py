#题目：输入一个链表，输出该链表中倒数第k个结点。
#输入：{1,2,3,4,5},1 输出：5

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self , pHead , k ):
        # write code here
        link_list = pHead
        count =0
        while pHead:
            pHead = pHead.next
            count +=1
        if k > count:
            return
        for i in range(count-k):
            link_list = link_list.next
        return link_list