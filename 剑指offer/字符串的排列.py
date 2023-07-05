# 题目：输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

class Solution:
    def Permutation(self, ss):
        # write code here
        n = len(ss)
        res = []
        if len(ss)<=1:
            return ss
        for i in range(n):
            all_str = self.Permutation(ss[:i]+ss[i+1:])
            for j in all_str:
                tem = ss[i] + j
                res.append(tem)
        res = set(res)
        return sorted(res)
    
#动态规划法：
class Solution:
    def Permutation(self, ss):
        # write code here
        #有新值'd'，加入abc时，怎么个加法
        def mix(array,word):
            res = []
            for i in range(len(array)+len(word)):
                a = ['']*(len(array)+len(word))
                a[i] = word
                if i > 0:
                    a[:i] = array[:i]
                if i+1 < len(array)+len(word):
                    a[i+1] = array[i:]
                res.append(''.join(a))
            return res
        dp = [0]*len(ss)
        dp[0] = [ss[0]]
        for i in range(1,len(ss)):
            res = []
            #将新值与备忘录中的所有值组合
            for j in dp[i-1]:
                res += mix(j,ss[i])
            dp[i] = list(set(res))
        return sorted(dp[-1])
