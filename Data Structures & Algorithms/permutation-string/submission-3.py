class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        m1 = {}
        for j in s1:
            if j in m1:
                m1[j]+=1
            else:
                m1[j] = 1

        for i in range(len(s2)-l+1):
            m = {}
            for j in range(i, i+l):
                if s2[j] in m:
                    m[s2[j]]+=1
                else:
                    m[s2[j]] = 1
            if m==m1:
                return True
        return False
            
                
                