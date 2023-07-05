# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
#输入："We Are Happy" 输出："We%20Are%20Happy"

# 题解：用一个列表来复制，与在单个序列上移动相比，不用花费O（n**2）的时间
class Solution:
    def replaceSpace(self , s ):
        # write code here
        array = s
        copy_list = []
        for i in range(len(array)):
            if array[i] == ' ':
                copy_list.append('%20')
            else:
                copy_list.append(array[i])
        return ''.join(copy_list)