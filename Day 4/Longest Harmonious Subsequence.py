class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=Counter(nums)
        return max([count[i]+count[i+1] for i in count if i+1 in count] or [0])
        
