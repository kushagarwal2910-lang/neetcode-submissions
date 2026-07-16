class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix)-1
        while l<=r:
            m = (l+r)//2
            d = matrix[m]
            if d[0]>target:
                r-=1
            if d[0]<target and target not in d:
                l+=1
            if d[0]==target:
                return True
            if target in d:
                return True
        return False