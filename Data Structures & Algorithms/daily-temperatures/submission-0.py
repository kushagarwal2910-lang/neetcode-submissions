class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        for i in range(len(temperatures)):
            s.append(0)
            for j in range(i, len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    s[-1]=j-i
                    break
        return s