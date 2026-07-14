class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        m = {}
        for i in range(len(s)):
            d = []
            if s[i] in t:
                for j in range(i,len(s)):
                    d.append(s[j])
                    if all(d.count(c) >= t.count(c) for c in set(t)):
                        m[len(d)] = d
                        break
        if len(m)==0:
            return ""
        else:
            return "".join(m[min(m)])