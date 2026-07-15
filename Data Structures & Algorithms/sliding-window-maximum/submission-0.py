class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m = []
        for i in range(len(nums)-k+1):
            j = i+k
            d = nums[i:j]
            m.append(max(d))
        return m
                