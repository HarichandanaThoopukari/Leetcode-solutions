class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        st=[]
        for i in range(len(prices)):
          for j in range(i+1,len(prices)):
            if prices[i]>=prices[j] and j>i:
                st.append(prices[i]-prices[j])
                break
          else:
            st.append(prices[i])
        return st
        