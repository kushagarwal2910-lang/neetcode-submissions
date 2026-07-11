class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            return 1
        nums = list(sorted(set(nums)))
        nums.append(-1)
        c = []
        k = 0
        i = 0
        j = 1
        while j<len(nums):
            if nums[j]-nums[i] != 1:
                c.append(list(nums[k:j]))
                k = j
            i+=1
            j+=1
        maxi = 0
        for  i in c:
            maxi = max(len(i), maxi)
        return maxi