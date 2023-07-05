#输入：在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）
#"google"：4

#题解：用字典（哈希表）排序
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        res = {}
        for i in s:
            if not res.get(i):
                res[i] = 1
            else:
                res[i] +=1
        res_list = []
        for keys,values in res.items():
            if values == 1:
                res_list.append(s.index(keys))
        return min(res_list)
a = Solution()
print(a.FirstNotRepeatingChar("google"))