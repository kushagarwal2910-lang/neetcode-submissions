class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        c = []
        while i<j:
            if numbers[i]+numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                c.append(i+1)
                c.append(j+1)
                return c
        return False