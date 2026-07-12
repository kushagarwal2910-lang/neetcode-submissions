class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = []
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i!=j:
                    l = min(heights[i], heights[j])
                    b = abs(j-i)
                    h.append(l*b)
        return max(h)