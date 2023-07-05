#给定两个字符串str1和str2,输出两个字符串的最长公共子串
#题目保证str1和str2的最长公共子串存在且唯一。

#题解，我的方法：
#另加一个指针cur，如果short[cur:i]能够在long中找到，则添加到res中；否则，不添加，cur+1，这种方法算是暴力解，不好
#动态规划：
#当A[i] = B[i],res[i][j]=res[i-1][j-1]+1;A[i] ！= B[i],res[i][j]= 0，因为当A[i] != B[j]时，res[i][j]就直接等于0了，因为子串必须连续


class Solution:
    def LCS(self, str1, str2):
        # write code here
        short = []
        long = []
        if len(str1) >= len(str2):
            short = str2
            long = str1
        else:
            short = str1
            long = str2
        cur = 0
        n = len(short)
        res = []
        for i in range(n+1):
            print(i)
            if short[cur:i] in long:
                res.append(short[cur:i])
            else:
                cur+=1
        return res[-1]
a = Solution()
a.LCS("1AB234CD56789","1234EF56789")

#动态规划解
#如果目前位置对应的前个点相等，那么dp[i-1][j-1]+1
'1AB2345' -- '12345'
长这样：
0 0
0 1
    0 0 1
          2
            3
              4

def LCstring(string1,string2):
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1+1)] for j in range(len2+1)]
    result = 0
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if string2[i-1] == string1[j-1]:
                res[i][j] = res[i-1][j-1]+1
                result = max(result,res[i][j])  
    return result
print(LCstring("helloworld","loop"))
# 输出结果为：2



