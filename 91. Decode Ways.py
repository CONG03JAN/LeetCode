class Solution:
    def numDecodings(self, s: str) -> int:
        s = "0" + s
        dp = [1]
        if s[1] == '0':
            dp.append(0)
        else:
            dp.append(1)
        lens = len(s)

        for i in range(2, lens):
            t = int(s[i-1])*10 + int(s[i])
            tmp = dp[i-2] if t <= 26 and t > 0 else 0
            tmp2 = dp[i-1] if int(s[i]) > 0 else 0
            dp.append(tmp2 + tmp)
        
        return dp[-1]

