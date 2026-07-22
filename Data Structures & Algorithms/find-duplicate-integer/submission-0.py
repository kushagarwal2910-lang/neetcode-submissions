class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = {}

        for i in nums:
            if i in n:
                n[i]+=1
                return i
            else:
                n[i] = 1
