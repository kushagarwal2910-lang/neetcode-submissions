class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        ma = {}
        for i, n in enumerate(nums):
            cmp = target - n

            if cmp in ma:
                return [ma[cmp], i]
            
            ma[n] = i
        
        return []