class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        w=set(word1)|set(word2)
        
        for i in w:
            if abs(word1.count(i)-word2.count(i))>3:
                return False
        return True
               

        