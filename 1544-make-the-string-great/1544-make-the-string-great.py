class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        for i in range(len(s)): 
            ch=s[i]
            if st and st[-1]!=ch and st[-1].upper()==ch.upper():
                st.pop()
            else:
                st.append(s[i])
        for i in s:
            return "".join(st)







            
        