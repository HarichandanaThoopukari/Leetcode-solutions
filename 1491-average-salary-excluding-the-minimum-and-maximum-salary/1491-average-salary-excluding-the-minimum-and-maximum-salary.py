class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        s=(sum(salary)-min(salary)-max(salary))/float(len(salary)-2)
        return s
        