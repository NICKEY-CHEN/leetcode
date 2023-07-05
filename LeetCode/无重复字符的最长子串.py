# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
# 示1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


# 解题思路：从左开始，若当前字母在最优子字符串列表OL中，则从左到右删除，直至遇到当前字母为止，同时记录最优子字符串最后一个元素下标start，得到当前最优子字符串长度

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        start = 0
        max_len = 0
        char_set = []
        for i in range(n):
            while s[i] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.append(s[i])
            max_len = max(max_len, i - start + 1)
        return max_len