# 题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        n = len(s)
        if n ==1:
            return 1
        res =[]
        res.append(s[0])
        index = 0
        max_len = 0
        for i in range(1,n):
            if s[i] not in res:
                res.append(s[i])
            else:
                #找出前一个和自己数值相等位置的索引
                index = s.index(s[i],index,n-1)
                res = []
                for j in s[index+1:i+1]:
                    res.append(j)
                index+=1
            if len(res) > max_len:
                max_len = len(res)
        return max_len

a = Solution()
a.lengthOfLongestSubstring("bbbbb")