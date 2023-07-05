#题目：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

#题解：逻辑是，如果排出队列为空，则将接收队列的填入，再判断是否为空，不为空，.pop()，为空，不返回值
class Solution:
    def __init__(self):
        self.acceptlist = []
        self.poplist = []

    def push(self, node):
        # write code here
        self.acceptlist.append(node)

    def pop(self):
        # return xx
        if not self.poplist:
            while self.acceptlist:
                self.poplist.append(self.acceptlist.pop())
        if self.poplist:
            return self.poplist.pop()
        else:
            return