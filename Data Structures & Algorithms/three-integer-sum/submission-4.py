class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        c = []
        nums.sort()
        for i, j in enumerate(nums):                
            if i>0 and j == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l<r:
                th = j + nums[l] + nums[r]
                if th>0:
                    r -= 1
                elif th<0:
                    l += 1
                else:
                    c.append([nums[l], nums[r], j])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return c