class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ma,mi = len(nums)-1 , 0
        while mi<=ma:
            mid = (ma+mi)//2
            if nums[mid]>target:
                ma-=1
            if nums[mid]<target:
                mi+=1
            if nums[mid]==target:
                return mid
        return -1