class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            m = {}
            c = 0
            for j in range(i, len(s)):
                if s[j] in m:
                    m[s[j]] += 1
                else:
                    m[s[j]] = 1
                c = max(max(m.values()), c)
                if j-i+1 - c <= k:
                    res = max(res, j-i+1)
        return res