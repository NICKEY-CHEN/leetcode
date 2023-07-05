# 给出一个仅包含字符'('和')'的字符串，计算最长的格式正确的括号子串的长度。
# 对于字符串"(()"来说，最长的格式正确的子串是"()"，长度为2.
# 再举一个例子：对于字符串")()())",来说，最长的格式正确的子串是"()()"，长度为4.

class Solution:
    def longestValidParentheses(self , s ):
        # write code here
        if not s:
            return 0
        n=len(s)
        dp=[0]*n
        for i in range(1,n):
            if s[i]=='(':
                continue
            else:
                j=i-1-dp[i-1]
                if s[j]=='(':
                    if j>0:
                        dp[i]=2+dp[i-1]+dp[j-1]
                    else:
                        dp[i]=2+dp[i-1]
        return max(dp)
