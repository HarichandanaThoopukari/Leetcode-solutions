class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        freq={}
        
        for i in word:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            freq[i]-=1
            res=[]
            for ch in freq.values():
                if ch>0:
                    res.append(ch)
            if len(set(res))==1:
                return True
            freq[i]+=1
        return False


        