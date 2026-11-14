class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1]*(n+1)
        return self.cal(n,dp)
    def cal(self,n,dp):
        if n==0:
            return 1
        if n<0:
            return 0
        if dp[n]!=-1:
            return dp[n]
        dp[n]= self.cal(n-1,dp)+self.cal(n-2,dp)
        return dp[n]
      

        
        