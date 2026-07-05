class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        f = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in t:
            if j in f:
                f[j] += 1
            else:
                f[j] = 1
        for k in d:
            if k not in f:
                return False
            if d[k]!=f[k] :
                return False
        return True