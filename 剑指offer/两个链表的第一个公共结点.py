#题目：输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）

# 题解：思路：首先我们要知道什么是公共节点，两个链表从某一节点开始，他们的next都指向同一个节点。但由于是单向链表的节点，每个节点只有一个next，
# 因此从第一个公共节点开始，之后他们的所有节点都是重合的，不可能再出现分叉。所以可以先遍历两个链表得到他们的长度，就能知道哪个链表比较长，
# 以及长的链表比短的链表多几个结点。在第二次遍历的时候，在较长的链表上先走若干步，接着同时在两个链表上遍历，找到的第一个相同的结点就是他们的第一个公共结点。
# 时间复杂度为O(m+n)，而暴力破解法的时间复杂度为O(mn).
# 解题思路：两个有共同节点的链表是Y型结构，也就是自第一个公共节点开始，都是重合的。题目要求，要找到第一个公共节点，可以反其道而行之，从后往前找，如果是重合节点，这两个节点一定是相等的，所以最后一个相等的节点就是第一个公共的节点。具体方法可以先将每个链表中的节点循环添加到栈中，然后从栈中弹出，一一比较即可

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code her
        if not pHead1 or not pHead2:
            return None
        stack1 =[]
        stack2 = []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        res = None
        while stack1 and stack2:
            p1 = stack1.pop()
            p2 = stack2.pop()
            if p1.val == p2.val:
                res = p1
            else:
                break
        return res