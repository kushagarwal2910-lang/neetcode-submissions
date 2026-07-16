class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ma = len(nums)-1
        mi = 0
        while mi<=ma:
            mid = (ma+mi)//2
            if nums[mid]>target:
                ma-=1
            elif nums[mid]<target:
                mi+=1
            else:
                return mid
        return -1